import argparse
from pathlib import Path
import sys
from isHex import isHex
import base64

# Calls other functions in order to perform the XOR encryption
def cmd_xor(args: argparse.Namespace):
    ensure_bin_file(args.infile)
    key = parse_key(args.key)
    data = Path(args.infile).read_bytes()
    encrypted = xor_bytes(data, key)
    result = format_output(encrypted, args.out)
    isbin = args.out.endswith("bin")
    write_output(result, Path(args.out), isbin)

# Arguments
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="xorcrypt", description="XOR CLI tool")
    sub = p.add_subparsers(dest="cmd", required=True)

    px = sub.add_parser("xor", help="XOR input with key and output in chosen format")
    px.add_argument("-i", "--in", dest="infile", required=True,
                    help="Input file path. Only accepts .bin")
    px.add_argument("-o", "--out", dest="out", required=True,
                    help="Output file path. Formats accepted: .bin, .py, .c")
    px.add_argument("-k", "--key", required=True, help="Key. At least one byte")
    px.set_defaults(func=cmd_xor)

    return p

# Prepares encrypted file content according to desired output
def format_output(encrypted: bytes, out: str) -> bytes:
    out = out.lower()
    if out.endswith("bin"):
        return encrypted
    if out.endswith("py"):
        return to_python_array(encrypted)
    if out.endswith("c"):
        return to_c_array(encrypted)
    raise ValueError("Output format must be one of: raw, py, c")

# If desired output is .py
def to_python_array(data: bytes) -> str:
    return f"data = [{', '.join(str(b) for b in data)}]"

# If desired output is .c
def to_c_array(data: bytes, var_name="data") -> str:
    return f"unsigned char {var_name}[] = {{ {', '.join(str(b) for b in data)} }};"

# Validates input file
def ensure_bin_file(path_str: str) -> Path:
    p = Path(path_str)
    if p.suffix.lower() != ".bin":
        raise argparse.ArgumentTypeError("Only .bin files are accepted for input.")
    if not p.is_file():
        raise argparse.ArgumentTypeError(f"Input file not found: {p}")
    return p

# Turns key into bytes
def parse_key(key_str: str) -> bytes:
    key_str = key_str.lower().replace("0x", "")
    key_str = key_str.replace(" ", "")
    if len(key_str) % 2 != 0:
        raise ValueError("Hex key must have an even number of characters.")
    return bytes.fromhex(key_str)


# Encryption algorithm
def xor_bytes(data: bytes, key: bytes) -> bytes:
    if not key:
        raise ValueError("Key must not be empty.")
    klen = len(key)
    return bytes(b ^ key[i % klen] for i, b in enumerate(data))

# Writes encrypted file
def write_output(payload: bytes, out_path: Path, is_binary: bool):
    if is_binary:
        out_path.write_bytes(payload)
    else:
        out_path.write_text(payload, encoding="utf-8")

def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        args.func(args)
    except Exception as e:
        print(f"error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
