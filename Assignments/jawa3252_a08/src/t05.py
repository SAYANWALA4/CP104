"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-17"
-------------------------------------------------------
"""
# Imports
from functions import has_word_chain

# Test Case 1
word_chain1 = ["apple", "elephant", "tiger", "rabbit"]
result1 = has_word_chain(word_chain1)
print(result1)  # Output: True

# Test Case 2
word_chain2 = ["python", "node", "nope", "tiger"]
result2 = has_word_chain(word_chain2)
print(result2)  # Output: False

# Test Case 3
word_chain3 = ["book", "kite", "egg", "giraffe"]
result3 = has_word_chain(word_chain3)
print(result3)  # Output: True
