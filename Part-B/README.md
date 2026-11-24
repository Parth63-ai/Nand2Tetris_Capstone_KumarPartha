# Part B – Python Assembler

Implement a two-pass assembler:
1. Strip comments and blank lines; record label addresses.
2. Translate A- and C-instructions to 16-bit machine code; allocate variables from RAM address 16.

Personal extra feature for K=8:
- K mod 3 = 2
- Print a warning when a label is declared more than once.

Test against Add.asm, Max.asm, Rect.asm and Pong.asm, comparing output with the official assembler.
