# Logisim RISC-V CPU

This project is an extension of Lab 1 for ECSE 324 - Computer Organization at McGill University.

## Overview

The project consists of a 16-bit RISC-V Logisim CPU, an assembler for ARM-style assembly, and test files for various CPU components.

### Logisim CPU

The Logisim CPU directory contains the CPU file named `cpu.circ`. Open this file using `Logisim 3.8.0`, included in the directory, or use the modified version `Logisim 3.9.0dev`, better suited for the lab.

### Test Files

The `Test Files` directory includes test files for the CPU components, such as the ALU, Register File, Programmable CPU, Data Memory, and Branching.

### Assembler

The `Assembler` directory contains a Python script that converts ARM-style assembly into hexadecimal code. The script writes the output to `output.rom`, which can be loaded into the CPU's ROM in Logisim.

## Supported Instructions

The CPU, along with its assembler, can process the following instructions:

### ALU Instructions

- `ADD` (Signed Integer Addition)
- `SUB` (Signed Integer Subtraction)
- `AND` (Bitwise AND)
- `OR`  (Bitwise OR)
- `NOR` (Bitwise NOR)
- `LSL` (Logical Shift Left)
- `LSR` (Logical Shift Right)
- `ASR` (Arithmetic Shift Right)

### Memory Instructions

- `LD` (Load)
- `ST` (Store)

### Branching Instructions

- `EQ` (Equal)
- `NE` (Not Equal)
- `LT` (Signed Less Than)
- `LE` (Signed Less or Equal)
- `GT` (Signed Greater Than)
- `GE` (Signed Greater or Equal)

## How to Use

1. **Logisim CPU:**
   - Open `cpu.circ` using Logisim 3.8.0 or the modified version `Logisim 3.9.0dev`.

2. **Assembler:**
   - Run the Python script in the `Assembler` directory to convert ARM-style assembly into hexadecimal code.
   - Load the output (`output.rom`) into the ROM module of the CPU in Logisim.

3. **Simulation:**
   - Simulate the CPU by enabling and disabling `Auto-Tick` to process the code in ROM or by using manual click cycles.

## Project Details

- **Created:** September 2022
- **Last Updated:** December 2023 (or specify the last update date)
- **Update:** Added Python assembler script (`assembler.py`) to convert ARM-style assembly to hexadecimal instructions.
