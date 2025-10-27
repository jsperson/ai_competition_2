#!/usr/bin/env python3
"""Analyze filenames for hidden patterns"""

import os
import glob
import re

def decode_punchcard(filepath):
    """Read a punch card file"""
    with open(filepath, 'r') as f:
        lines = f.readlines()
    byte1 = int(lines[0].strip().replace('→', '').replace(' ', ''), 2)
    byte2 = int(lines[1].strip().replace('→', '').replace(' ', ''), 2)
    return (byte1, byte2, os.path.basename(path))

# Read all cards
cards = []
for filepath in glob.glob('data/*.txt'):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    byte1 = int(lines[0].strip().replace('→', '').replace(' ', ''), 2)
    byte2 = int(lines[1].strip().replace('→', '').replace(' ', ''), 2)
    fname = os.path.basename(filepath).replace('.txt', '')
    cards.append((byte1, byte2, fname))

cards.sort(key=lambda x: x[0])

print("=" * 60)
print("FILENAME ANALYSIS")
print("=" * 60)

# Try extracting first letter of each filename
first_letters = ''.join([fname[0] for _, _, fname in cards])
print(f"\nFirst letters of filenames (in order): {first_letters}")

# Try extracting last letter
last_letters = ''.join([fname[-1] for _, _, fname in cards])
print(f"Last letters of filenames (in order): {last_letters}")

# Try extracting uppercase letters only
upper_letters = ''.join([''.join([c for c in fname if c.isupper()]) for _, _, fname in cards])
print(f"\nUppercase letters only: {upper_letters}")

# Try extracting lowercase letters only
lower_letters = ''.join([''.join([c for c in fname if c.islower()]) for _, _, fname in cards])
print(f"Lowercase letters only: {lower_letters}")

# Try extracting digits only
digits = ''.join([''.join([c for c in fname if c.isdigit()]) for _, _, fname in cards])
print(f"Digits only: {digits}")

# Check if filenames encode positions differently
print("\n" + "=" * 60)
print("ALTERNATIVE POSITION ENCODING")
print("=" * 60)

# Sort by filename alphabetically
cards_alpha = sorted(cards, key=lambda x: x[2])
msg_alpha = ''.join([chr(b2) if b2 < 128 else '?' for b1, b2, _ in cards_alpha])
print(f"Sorted alphabetically by filename: {msg_alpha}")

# Try numeric sorting by extracting numbers from filenames
def extract_number(fname):
    nums = re.findall(r'\d+', fname)
    return int(nums[0]) if nums else 0

cards_numeric = sorted(cards, key=lambda x: extract_number(x[2]))
msg_numeric = ''.join([chr(b2) if b2 < 128 else '?' for b1, b2, _ in cards_numeric])
print(f"Sorted by first number in filename: {msg_numeric}")

print("\n" + "=" * 60)
print("CHECKING FOR PATTERN IN POSITION BYTE")
print("=" * 60)
for b1, b2, fname in cards:
    char = chr(b2) if b2 < 128 else f'[{b2}]'
    print(f"{fname:15s} -> pos={b1:2d} char='{char}' | b1&0x1F={b1&0x1f} b1>>3={b1>>3}")
