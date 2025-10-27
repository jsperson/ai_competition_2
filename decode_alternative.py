#!/usr/bin/env python3
"""Try alternative decoding methods for punch cards"""

import os
import glob

def decode_punchcard(filepath):
    """Read a punch card file and return both bytes"""
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # Parse both binary numbers
    byte1 = int(lines[0].strip().replace('→', '').replace(' ', ''), 2)
    byte2 = int(lines[1].strip().replace('→', '').replace(' ', ''), 2)

    return (byte1, byte2, filepath)

def main():
    # Read all .txt files
    cards = []
    for filepath in glob.glob('data/*.txt'):
        try:
            b1, b2, path = decode_punchcard(filepath)
            cards.append((b1, b2, os.path.basename(path)))
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

    # Sort by first byte (position)
    cards.sort(key=lambda x: x[0])

    print("=" * 60)
    print("METHOD 1: Second byte only (original)")
    print("=" * 60)
    msg1 = ''.join([chr(b2) if b2 < 128 else f'[{b2}]' for b1, b2, _ in cards])
    print(msg1)

    print("\n" + "=" * 60)
    print("METHOD 2: XOR of both bytes")
    print("=" * 60)
    msg2 = ''.join([chr(b1 ^ b2) for b1, b2, _ in cards])
    print(msg2)

    print("\n" + "=" * 60)
    print("METHOD 3: First byte only")
    print("=" * 60)
    msg3 = ''.join([chr(b1) if b1 < 128 else f'[{b1}]' for b1, b2, _ in cards])
    print(msg3)

    print("\n" + "=" * 60)
    print("METHOD 4: 16-bit values (byte1 << 8 | byte2)")
    print("=" * 60)
    for b1, b2, fname in cards:
        val = (b1 << 8) | b2
        print(f"{fname}: {val} (0x{val:04x})")

    print("\n" + "=" * 60)
    print("METHOD 5: Sum of both bytes")
    print("=" * 60)
    msg5 = ''.join([chr((b1 + b2) % 256) for b1, b2, _ in cards])
    print(msg5)

    print("\n" + "=" * 60)
    print("METHOD 6: Difference (byte2 - byte1)")
    print("=" * 60)
    msg6 = ''.join([chr(abs(b2 - b1)) for b1, b2, _ in cards])
    print(msg6)

    print("\n" + "=" * 60)
    print("Raw data for analysis:")
    print("=" * 60)
    for i, (b1, b2, fname) in enumerate(cards):
        xor = b1 ^ b2
        print(f"Pos {i:2d}: b1={b1:3d} (0x{b1:02x}), b2={b2:3d} (0x{b2:02x}), XOR={xor:3d} ('{chr(xor)}')")

if __name__ == '__main__':
    main()
