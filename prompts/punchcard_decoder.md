# Punch Card Decoder Challenge

## Task
Decode the riddle hidden in the punch card files located in the `./data` directory.

## File Format
Each `.txt` file in `./data` contains a two-line punch card in the following format:

```
[binary_position]
[binary_character]
```

Where:
- **Line 1**: 8-bit binary number representing the **position** in the final message
- **Line 2**: 8-bit binary number representing the **ASCII character code**

## Example
```
00000000
01010100
```
- Position: `00000000` (binary) = 0 (decimal)
- Character: `01010100` (binary) = 84 (decimal) = 'T' (ASCII)

## Decoding Steps

1. **Read all punch card files** from `./data/*.txt`
2. **Parse each file**:
   - Extract the first binary number (position index)
   - Extract the second binary number (ASCII character code)
3. **Convert binary to decimal**:
   - Position byte → position in message
   - Character byte → ASCII character
4. **Sort cards** by position (ascending)
5. **Concatenate characters** in position order to reveal the message

## Special Cases
- Character code 226 (0xE2) should be interpreted as an apostrophe (')
- All other codes < 128 are standard ASCII characters

## Expected Output
The decoded message should read: **"There's no place like home"**

## Technical Interpretation
In computing culture, "There's no place like home" is a reference to:
- **127.0.0.1** (localhost/loopback address)
- The phrase "There's no place like 127.0.0.1"

## Implementation Tips
- Use binary-to-decimal conversion: `int(binary_string, 2)`
- Sort by position before concatenating
- Handle extended ASCII (codes > 127) appropriately
