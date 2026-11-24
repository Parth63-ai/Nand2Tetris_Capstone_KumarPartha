
// =====================================
// Box.asm
// K = 8
// Starting row = 8
// Height = 20 rows
// Width = 16 pixels (1 word)
// =====================================

(LOOP)
    // Check whether any key is pressed
    @KBD
    D=M
    @BLACK
    D;JNE

    // No key pressed: set color to white
    @color
    M=0
    @PAINT
    0;JMP

(BLACK)
    // Key pressed: set color to black
    @color
    M=-1

(PAINT)
    // Starting address = SCREEN + (32 * 8)
    @SCREEN
    D=A
    @256
    D=D+A
    @addr
    M=D

    // Height = 20 rows
    @20
    D=A
    @count
    M=D

(ROW)
    // Paint one word (16 pixels)
    @color
    D=M
    @addr
    A=M
    M=D

    // Move to the same column in the next row
    @32
    D=A
    @addr
    M=D+M

    // Decrease row counter
    @count
    M=M-1
    D=M

    // Repeat until all 20 rows are processed
    @ROW
    D;JGT

    // Continuously check the keyboard
    @LOOP
    0;JMP
