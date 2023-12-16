def process_line(line):
    """
    Process a line by converting it to uppercase and removing comments.

    Args:
        line (str): The input line.

    Returns:
        str: The processed line.
    """
    line = line.upper()
    if "//" in line:
        line = line.split("//")[0].strip()
    if "#" in line:
        line = line.split("#")[0].strip()
    return line

def process_operations(operations):
    """
    Process a list of operations by removing spaces from each element.

    Args:
        operations (list): A list of operation elements.

    Returns:
        list: A new list with spaces removed from each element.
    """
    return [element.replace(" ", "") for element in operations]

def alu_operations(op_code, immediate_flag, destination, source1, source2):
    """
    Generate a binary line for ALU operations based on provided parameters.

    Args:
        op_code (int): The operation code and the ALU operation (5 bits).
        immediate_flag (bool): True if immediate value is used, False otherwise.
        destination (str): The destination register (2nd element of a list, assumed to be a string).
        source1 (str): The first source register (2nd element of a list, assumed to be a string).
        source2 (str or int): The second source register or immediate value.

    Returns:
        str: Binary representation of the ALU operation.
    """
    binary_line = f'{op_code:05b}'
    binary_line += '1' if immediate_flag else '0'
    binary_line += format(int(destination[1]), '03b')
    binary_line += format(int(source1[1]), '03b')
    if (immediate_flag):
        binary_line += bin(int(source2) & 0b1111)[2:].zfill(4)
    else:
        binary_line += format(int(source2[1]), '04b')
    return binary_line

def branch_operations(op_code, immediate_flag, displacement, source1, source2):
    """
    Generate a binary line for branch operations based on provided parameters.

    Args:
        op_code (int): The operation code and the condition (5 bits).
        immediate_flag (bool): True if immediate value is used, False otherwise.
        displacement (int): The displacement value for branch (3 bits).
        source1 (str): The first source register (2nd element of a list, assumed to be a string).
        source2 (str or int): The second source register or immediate value.

    Returns:
        str: Binary representation of the branch operation.
    """
    binary_line = f'{op_code:05b}'
    binary_line += '1' if immediate_flag else '0'
    binary_line += bin(int(displacement) & 0b111)[2:].zfill(3)
    binary_line += format(int(source1[1]), '03b')
    if (immediate_flag):
        binary_line += bin(int(source2) & 0b1111)[2:].zfill(4)
    else:
        binary_line += format(int(source2[1]), '04b')
    return binary_line

def main(input_file, output_file):
    """
    Process input lines, convert assembly-like language to hexadecimal,
    and write the results to an output file.

    Args:
        input_file (str): The input file path.
        output_file (str): The output file path.
    """
    
    # Reads input file
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    # Opens output file
    with open(output_file, 'w') as hexFile:
        # Writes header to output file
        hexFile.write('v2.0 raw' + '\n')
    
        # Loops through each line and processes it
        for line in lines:
            binary_line = ''
            line = process_line(line)

            if len(line) == 0:
                continue

            line_array = line.strip().split(" ", 1)
            try:
                operations = process_operations(line_array[1].split(","))
            except IndexError:
                continue
            
            # ALU operations
            if line_array[0] == "ADD":
                binary_line += alu_operations(0b00000, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "SUB":
                binary_line += alu_operations(0b00001, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "AND":
                binary_line += alu_operations(0b00010, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "OR":
                binary_line += alu_operations(0b00011, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "NOR":
                binary_line += alu_operations(0b00100, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "LSL":
                binary_line += alu_operations(0b00101, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "LSR":
                binary_line += alu_operations(0b00110, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "ASR":
                binary_line += alu_operations(0b00111, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            
            # Load operation
            elif line_array[0] == "LD":
                binary_line += '100001' + str(format(int(operations[0][1]), '03b')) + str(format(int(operations[1][1]), '03b'))
                try:
                    offset = format(int(operations[2]), '04b')
                    binary_line += str(offset)
                except IndexError:
                    binary_line += '0000'
            
            # Store operation
            elif line_array[0] == "ST":
                binary_line += '110001' + str(format(int(operations[0][1]), '03b')) + str(format(int(operations[1][1]), '03b'))
                try:
                    offset = format(int(operations[2]), '04b')
                    binary_line += str(offset)
                except IndexError:
                    binary_line += '0000'
            
            # Branch operations
            elif line_array[0] == "EQ":
                binary_line += branch_operations(0b01000, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "NE":
                binary_line += branch_operations(0b01001, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "LT":
                binary_line += branch_operations(0b01010, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "LE":
                binary_line += branch_operations(0b01011, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "GT":
                binary_line += branch_operations(0b01100, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            elif line_array[0] == "GE":
                binary_line += branch_operations(0b01101, operations[2][0] != 'R', operations[0], operations[1], operations[2])
            
            # Syntax Error detected
            else:
                raise Exception("Syntax Error:", line)
            
            # Converts binary string to hex string
            binary_num = hex(int(binary_line, 2))
            hex_line = f"{int(binary_num, 16):04X}"
            
            # Writes hex string to output file
            hexFile.write(str(hex_line).lower()  + '\n')

if __name__ == "__main__":
    input_file = 'intputFile.asm'
    output_file = 'outputFile.rom'
    main(input_file, output_file)