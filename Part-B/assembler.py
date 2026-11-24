import sys
from pathlib import Path


def clean_lines(file_path):
    """
    Remove comments and blank lines
    from the assembly file.
    """

    instructions = []

    with open(file_path, "r") as file:
        for line in file:

            # Remove comments
            line = line.split("//")[0].strip()

            # Ignore blank lines
            if line:
                instructions.append(line)

    return instructions


def first_pass(instructions):
    """
    Identify labels and build the symbol table.
    """

    symbol_table = {
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576
    }

    # Predefined registers R0 to R15
    for i in range(16):
        symbol_table[f"R{i}"] = i

    rom_address = 0
    clean_instructions = []

    for instruction in instructions:

        # Check for label declaration
        if instruction.startswith("(") and instruction.endswith(")"):

            label = instruction[1:-1].strip()

            if not label:
                raise ValueError("Empty label declaration")

            if label in symbol_table:
                print(
                    f"Warning: Duplicate label '{label}' detected."
                )
            else:
                symbol_table[label] = rom_address

        else:
            clean_instructions.append(instruction)
            rom_address += 1

    return clean_instructions, symbol_table



def encode_a_instruction(instruction, symbol_table, next_variable):
    """
    Convert an A-instruction into 16-bit binary.
    Automatically allocate RAM addresses to new variables.
    """

    # Remove the @ symbol
    symbol = instruction[1:].strip()

    # Check whether the value is numeric
    if symbol.isdigit():
        address = int(symbol)

    # Check whether the symbol already exists
    elif symbol in symbol_table:
        address = symbol_table[symbol]

    # Allocate a new RAM address for unknown variables
    else:
        address = next_variable
        symbol_table[symbol] = address
        next_variable += 1

    # Validate address
    if address < 0 or address > 32767:
        raise ValueError(f"Address out of range: {address}")

    # Convert to 16-bit binary
    machine_code = format(address, "016b")

    return machine_code, next_variable




# Computation bits
COMP = {
    "0":   "0101010",
    "1":   "0111111",
    "-1":  "0111010",
    "D":   "0001100",
    "A":   "0110000",
    "M":   "1110000",
    "!D":  "0001101",
    "!A":  "0110001",
    "!M":  "1110001",
    "-D":  "0001111",
    "-A":  "0110011",
    "-M":  "1110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "M+1": "1110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "M-1": "1110010",
    "D+A": "0000010",
    "D+M": "1000010",
    "D-A": "0010011",
    "D-M": "1010011",
    "A-D": "0000111",
    "M-D": "1000111",
    "D&A": "0000000",
    "D&M": "1000000",
    "D|A": "0010101",
    "D|M": "1010101"
}


# Destination bits
DEST = {
    "":    "000",
    "M":   "001",
    "D":   "010",
    "MD":  "011",
    "A":   "100",
    "AM":  "101",
    "AD":  "110",
    "AMD": "111"
}


# Jump bits
JUMP = {
    "":    "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}



def encode_c_instruction(instruction):
    """
    Convert a C-instruction into 16-bit binary.

    Format:
    111 + comp(7 bits) + dest(3 bits) + jump(3 bits)
    """

    dest = ""
    jump = ""

    # Separate jump part
    if ";" in instruction:

        if instruction.count(";") != 1:
            raise ValueError(f"Invalid instruction: {instruction}")

        instruction, jump = instruction.split(";")

    # Separate destination and computation
    if "=" in instruction:

        if instruction.count("=") != 1:
            raise ValueError(f"Invalid instruction: {instruction}")

        dest, comp = instruction.split("=")

    else:
        comp = instruction

    # Remove whitespace
    dest = dest.strip()
    comp = comp.strip()
    jump = jump.strip()

    # Normalize destination order to A, D, M
    # For example: DM becomes MD, and MA becomes AM
    if len(set(dest)) != len(dest) or any(
    register not in "ADM" for register in dest
  ):
     raise ValueError(f"Invalid destination: {dest}")

    dest = "".join(
    register for register in "AMD"
    if register in dest
)

    
    # Validate instruction fields
    if comp not in COMP:
        raise ValueError(f"Invalid computation: {comp}")

    if dest not in DEST:
        raise ValueError(f"Invalid destination: {dest}")

    if jump not in JUMP:
        raise ValueError(f"Invalid jump: {jump}")

    # Combine all binary fields
    machine_code = (
        "111"
        + COMP[comp]
        + DEST[dest]
        + JUMP[jump]
    )

    return machine_code


def assemble_file(file_path):
    """
    Assemble a Hack assembly file and
    generate its corresponding .hack file.
    """

    # Read and clean the assembly file
    instructions = clean_lines(file_path)

    # First pass: build symbol table
    clean_instructions, symbol_table = first_pass(instructions)

    # Start variable allocation from RAM address 16
    next_variable = 16

    machine_code = []

    # Second pass: encode all instructions
    for instruction in clean_instructions:

        if instruction.startswith("@"):
            binary, next_variable = encode_a_instruction(
                instruction, symbol_table, next_variable
            )

        else:
            binary = encode_c_instruction(instruction)

        machine_code.append(binary)

    # Create output directory
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Generate output filename
    output_file = output_dir / (Path(file_path).stem + ".hack")

    # Write machine code to file
    with open(output_file, "w") as file:
        for instruction in machine_code:
            file.write(instruction + "\n")

    print(f"\nAssembly successful!")
    print(f"Output file: {output_file}")
    print(f"Total instructions: {len(machine_code)}")




if __name__ == "__main__":

    # Check command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python assembler.py <filename.asm>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    # Check whether the input file exists
    if not file_path.is_file():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)

    try:

        # Assemble the file and generate .hack output
        assemble_file(file_path)

    except (ValueError, OSError) as error:
        print(f"\nError: {error}")
        sys.exit(1)
