# Part C – Draw the Box

Personal requirements for K=8:
- Starting row: 8
- Height: 20 rows
- Width: 16 pixels

Write `Box.asm`, assemble it using the project's own `Part-B/assembler.py`, and save the generated `Box.hack` here.

Expected behavior:
- While a key is pressed: draw the black box.
- When no key is pressed: clear the box.
- Repeat continuously.

Screen memory hint from the brief: row r starts at SCREEN + 32*r; each row has 32 words and each word represents 16 pixels.
