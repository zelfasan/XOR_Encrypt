XOR Encryption

This CLI tool is designed to encrypt binary files used a given key. It outputs the encrypted data in either .bin, .c or .py format

To run, simply call the file from within the terminal:
python projekt.py xor <args>

--in : The path to the input file.
--out : The desired path to the output file. NOTE: It will overwrite the file if it exists.
--key : Hex key. 1+ bytes.

A few examples of commands:
xor --in "infile.bin" --out "outfile.bin" --key "4243"
xor --in "infile.bin" --out "outfile.py" --key "0x4243"
xor --in "infile.bin" --out "outfile.c" --key "0x42 0x43"

Example outputs: 
.bin: vtzqv
.py: data = [118, 116, 122, 113, 118]
.c: unsigned char data[] = { 118, 116, 122, 113, 118 };