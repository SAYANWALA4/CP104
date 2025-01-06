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
from functions import common_end

# Test Case 1
str1 = "programming"
str2 = "mingling"
result1 = common_end(str1, str2)
print(result1)  # Output: ming

# Test Case 2
str3 = "apple"
str4 = "table"
result2 = common_end(str3, str4)
print(result2)  # Output: e

# Test Case 3
str5 = "hello"
str6 = "world"
result3 = common_end(str5, str6)
print(result3)  # Output: empty string (no common end)
