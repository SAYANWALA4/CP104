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
from functions import valid_isbn

# Test Case 1
isbn1 = "978-3-16-148410-0"
result1 = valid_isbn(isbn1)
print(result1)  # Output: True

# Test Case 2
isbn2 = "979-1-25-678902-3"
result2 = valid_isbn(isbn2)
print(result2)  # Output: True

# Test Case 3
isbn3 = "123-4-56-789012-3"
result3 = valid_isbn(isbn3)
print(result3)  # Output: False
