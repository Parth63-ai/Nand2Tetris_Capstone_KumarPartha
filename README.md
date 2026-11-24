
# Nand2Tetris Capstone — Make the Computer Draw a Box

A computer architecture capstone project based on **Nand2Tetris-I (ETCCNT301)** at K.R. Mangalam University.

This project demonstrates the complete journey from hardware construction to machine-code execution by implementing a Hack computer, developing a custom Python assembler, and creating a keyboard-controlled graphics program.

## 📌 Project Overview

The project is divided into three parts:

| Part | Description | Status |
|---|---|---|
| Part A | Building the Hack Computer using HDL | Completed |
| Part B | Developing a Two-Pass Assembler in Python | Completed |
| Part C | Creating a Keyboard-Controlled Box using Hack Assembly | Completed |

## 🛠️ Technologies Used

- HDL (Hardware Description Language)
- Python
- Hack Assembly Language
- Nand2Tetris Hardware Simulator
- Nand2Tetris CPU Emulator
- Visual Studio Code
- Git and GitHub

---

## 🔹 Part A — Building the Hack Computer

Implemented the main components of the Hack computer.

### Components Implemented

- **CPU.hdl:** Executes Hack instructions and handles arithmetic, logic, registers and control flow.
- **Memory.hdl:** Integrates RAM, Screen and Keyboard memory-mapped components.
- **Computer.hdl:** Connects the CPU, Memory and instruction ROM.

### Testing

The following official test scripts were executed successfully:

- `CPU.tst`
- `Memory.tst`
- `ComputerAdd.tst`
- `ComputerMax.tst`
- `ComputerRect.tst`

**Result:** All five tests passed successfully.

---

## 🔹 Part B — Python Two-Pass Assembler

Developed a custom Python assembler to translate Hack assembly programs (`.asm`) into 16-bit binary machine code (`.hack`).

### Pass 1 — Symbol Resolution

- Removes comments and blank lines.
- Identifies and records labels with their ROM addresses.
- Initializes predefined Hack symbols such as R0–R15, SP, LCL, ARG, THIS, THAT, SCREEN and KBD.
- Detects duplicate label declarations.

### Pass 2 — Machine Code Generation

- Converts A-instructions into 16-bit binary.
- Converts C-instructions using computation, destination and jump fields.
- Resolves labels and symbols.
- Allocates variables starting from RAM address 16.
- Reuses previously allocated variable addresses.
- Generates `.hack` output files.

### Additional Feature

**Personal Number: K = 8**

Since `8 mod 3 = 2`, the required additional feature is **duplicate-label detection**.

The assembler displays a warning when the same label is declared more than once and retains its first recorded address.

### Test Programs

| Program | Testing Focus |
|---|---|
| `Add.asm` | Basic instruction encoding |
| `Max.asm` | Labels and conditional jumps |
| `Rect.asm` | Variables, labels and loops |
| `Pong.asm` | Larger assembly program |
| `test.asm` | Label resolution and duplicate-label warning |
| `variables.asm` | Variable allocation and reuse |

Generated machine-code files are stored in the `output/` directory.

---

## 🔹 Part C — Keyboard-Controlled Box

Created a Hack assembly program that displays a black rectangular box while a keyboard key is pressed and clears it when the key is released.

### Box Specifications

| Property | Value |
|---|---|
| Personal Number (K) | 8 |
| Starting Row | 8 |
| Height | 20 rows |
| Width | 16 pixels |
| Words per Row | 1 |
| Starting Screen Address | 16640 |

### Program Logic

1. Continuously reads the keyboard memory address (`KBD`).
2. If a key is pressed, sets the color variable to `-1`, representing sixteen black pixels.
3. If no key is pressed, sets the color variable to `0`, clearing the box.
4. Uses a loop to draw or clear 20 screen rows.
5. Advances the screen memory pointer by 32 words to reach the next row.
6. Repeats the keyboard check continuously.

### Assembly and Execution

- **Source File:** `Box.asm`
- **Generated File:** `Box.hack`
- **Assembler:** Custom Python two-pass assembler
- **Total Instructions:** 36
- **Execution Environment:** Nand2Tetris CPU Emulator

**Result:** The box appears when a key is pressed and disappears when the key is released.

---

## 📁 Project Structure

```text
capstone/
│
├── Part-A/
│   ├── CPU.hdl
│   ├── Memory.hdl
│   ├── Computer.hdl
│   └── evidence/
│
├── Part-B/
│   ├── assembler.py
│   ├── test.asm
│   ├── variables.asm
│   ├── test_files/
│   │   ├── Add.asm
│   │   ├── Max.asm
│   │   ├── Rect.asm
│   │   └── Pong.asm
│   └── output/
│       ├── Add.hack
│       ├── Max.hack
│       ├── Rect.hack
│       ├── Pong.hack
│       └── ...
│
├── Part-C/
│   ├── Box.asm
│   └── Box.hack
│
├── report/
│
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_NAME>/capstone
```

### 2. Run the Python Assembler

Navigate to Part-B:

```bash
cd Part-B
```

Run the assembler on an assembly program:

```bash
python assembler.py test_files/Add.asm
```

To assemble the Part-C Box program:

```bash
python assembler.py ../Part-C/Box.asm
```

The generated `.hack` file is saved in the configured output directory.

### 3. Run the Box Program

1. Open the Nand2Tetris CPU Emulator.
2. Load the generated `Box.hack` file.
3. Start the program.
4. Enable keyboard input.
5. Press and hold any key to display the box.
6. Release the key to clear the box.

---

## 📚 Key Learnings

- Digital logic and computer architecture.
- CPU and memory integration.
- Hack instruction formats and binary encoding.
- Two-pass assembler development.
- Symbol-table management and variable allocation.
- Assembly loops and conditional jumps.
- Memory-mapped input/output.
- Screen memory addressing.
- Keyboard interaction.
- Debugging and testing low-level programs.

## 🎯 Conclusion

This project demonstrates the complete journey from hardware-level computer construction to software-level machine-code execution. By implementing the Hack computer, developing a custom Python assembler, and creating a keyboard-controlled graphics program, the capstone provided practical experience with computer architecture, low-level programming, memory management and debugging.

---

## 👨‍💻 Project Information

- **Project:** Make the Computer Draw a Box
- **Course:** Nand2Tetris-I (ETCCNT301)
- **Institution:** K.R. Mangalam University
- **Student:** Kumar Partha
- **Roll Number:** 2501410008
- **Personal Number (K):** 8
