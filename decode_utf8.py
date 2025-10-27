#!/usr/bin/env python3
"""Try UTF-8 and other character encoding interpretations"""

import glob

def decode_punchcard(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    byte1 = int(lines[0].strip().replace('→', '').replace(' ', ''), 2)
    byte2 = int(lines[1].strip().replace('→', '').replace(' ', ''), 2)
    return (byte1, byte2)

# Read all cards
cards = []
for filepath in sorted(glob.glob('data/*.txt')):
    b1, b2 = decode_punchcard(filepath)
    cards.append((b1, b2))

cards.sort(key=lambda x: x[0])

print("=" * 60)
print("EXAMINING POSITION 5 (the unusual character)")
print("=" * 60)
b1, b2 = cards[5]
print(f"Position 5: byte1={b1} (0x{b1:02x} binary:{bin(b1)})")
print(f"           byte2={b2} (0x{b2:02x} binary:{bin(b2)})")
print(f"\n226 decimal = 0xE2 hex = 0b11100010 binary")
print(f"\nIn various encodings:")
print(f"  ASCII: N/A (>127)")
print(f"  Latin-1/ISO-8859-1: {chr(226)} (â)")
print(f"  Windows-1252: {chr(226)} (â)")
print(f"  UTF-8: Typically first byte of multi-byte sequence")

print("\n" + "=" * 60)
print("TRYING AS BYTES OBJECT (UTF-8)")
print("=" * 60)
byte_array = bytes([b2 for _, b2 in cards])
print(f"Raw bytes: {byte_array}")
try:
    decoded = byte_array.decode('utf-8', errors='replace')
    print(f"UTF-8 decoded: {decoded}")
except:
    print("UTF-8 decoding failed")

try:
    decoded = byte_array.decode('latin-1')
    print(f"Latin-1 decoded: {decoded}")
except:
    print("Latin-1 decoding failed")

print("\n" + "=" * 60)
print("WHAT IF 226 IS MEANT TO BE APOSTROPHE?")
print("=" * 60)
# Manually replace 226 with apostrophe (39)
message = []
for i, (b1, b2) in enumerate(cards):
    if b2 == 226:
        message.append("'")
    else:
        message.append(chr(b2))
result = ''.join(message)
print(f"Message with 226→': {result}")

print("\n" + "=" * 60)
print("ALL POSITIONS WITH THEIR VALUES")
print("=" * 60)
for i, (b1, b2) in enumerate(cards):
    char = chr(b2) if b2 < 128 else f'[{b2}]'
    print(f"Pos {i:2d}: {b2:3d} (0x{b2:02x}) = {char}")
