#!/usr/bin/env python3
"""Decode punch card riddle from data directory"""

import os
import glob

def decode_punchcard(filepath):
    """Read a punch card file and return (position, character)"""
    with open(filepath, 'r') as f:
        lines = f.readlines()

    # First line is position (binary)
    position = int(lines[0].strip().replace('→', ''), 2)

    # Second line is ASCII character (binary)
    char_code = int(lines[1].strip().replace('→', ''), 2)
    character = chr(char_code) if char_code < 128 else f'[{char_code}]'

    return (position, character, filepath)

def main():
    # Read all .txt files in data directory
    cards = []
    for filepath in glob.glob('data/*.txt'):
        try:
            pos, char, path = decode_punchcard(filepath)
            cards.append((pos, char, os.path.basename(path)))
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

    # Sort by position
    cards.sort(key=lambda x: x[0])

    # Print the decoded message
    print("Decoded Punch Cards:")
    print("-" * 50)
    for pos, char, filename in cards:
        print(f"Position {pos:2d}: '{char}' (from {filename})")

    print("\n" + "=" * 50)
    print("THE MESSAGE:")
    print("=" * 50)
    message = ''.join([char for _, char, _ in cards])
    print(message)
    print("=" * 50)

if __name__ == '__main__':
    main()
