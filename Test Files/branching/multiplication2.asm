ADD R1, R1, 0     
GE  3,  R1, 0      
NOR R1, R1, R1     
ADD R1, R1, 1      
ADD R0, R0, 1      
ADD R2, R2, -3     
GE  3,  R2, 0      
NOR R2, R2, R2     
ADD R2, R2, 1      
ADD R0, R0, 1      
AND R3, R3, 0      
AND R5, R5, 0      
AND R4, R2, 1      
EQ 2, R4, 0        
NE -4, R5, 0        
ADD R3, R3, R1     
LSL R1, R1, 1      
NE -4, R5, 0       
LSR R2, R2, 1      
ADD R5, R5, R2     
NE -4, R5, 0       
NE 2, R0, 1        
NOR R3, R3, R3     
ADD R3, R3, 1      
ADD R3, R3, 0      
EQ -1, R0, R0 