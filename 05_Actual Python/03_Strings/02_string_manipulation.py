## 01: WHAT IS STRINGS MANIPULATION?
"""
 It is the process of changing, parsing, slicing or analyzing strings to achieve a desired outcome.
"""

## 02:STRING SLICING.
"""
 * Slicing allows you to grab a specific piece of a string using index numbers.

 * Basic Syntax of slicing: string[start:stop:step]
"""
text = "Python"

# Normal slicing
print(text[0]) # Get the character at position 0

# Basic slicing 
print(text[0:4]) # Slice from index 0 up to (but not including) index 4

# Step slicing
print(text[0:6:2]) # Slice from index 0 to 6 with a step of 2

# Omitting Indices
print(text[:4])   # Output: 'PYTH' (Defaults to start at 0; indices 0 to 3)
print(text[2:])   # Output: 'THON' (Defaults to stop at the end; indices 2 to 5)
print(text[:])    # Output: 'PYTHON' (Copies the entire string)

# Negative Slicing & Reversing
print(text[-4:-1]) # Output: 'THO' (Indices -4, -3, -2)
print(text[::-1])  # Output: 'NOHTYP' (Reverses the string using a step of -1)