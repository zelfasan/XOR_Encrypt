**XOR Encryption**

This CLI tool is designed to encrypt binary files using a given key. It outputs the encrypted data in either **.bin**, **.c**, or **.py** format.

**Usage**

To run the tool, simply call the file from within the terminal:

python projekt.py xor

**Arguments**

• **\--in**: The path to the input file.• **\--out**: The desired path to the output file.Note: The file will be overwritten if it already exists.• **\--key**: Hex key (1 or more bytes).

**Example Commands**

xor --in "infile.bin" --out "outfile.bin" --key "4243"xor --in "infile.bin" --out "outfile.py" --key "0x4243"xor --in "infile.bin" --out "outfile.c" --key "0x42 0x43"

**Example Outputs**

• **.bin**: vtzqv• **.py**: data = \[118, 116, 122, 113, 118\]• **.c**: unsigned char data\[\] = { 118, 116, 122, 113, 118 };
