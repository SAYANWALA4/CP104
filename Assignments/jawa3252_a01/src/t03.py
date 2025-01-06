"""
-------------------------------------------------------
[program description]
A program that asks the user for a length in miles and prints 
the equivalent length in kilometres.
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-15"
-------------------------------------------------------
"""

# One mile is equal to 1.61 Kilometers
# Constant
KM_CONV = 1.61

# User inputs the length and then the program multiples it with the conversion rate
user_length = float(input("Length in miles:"))
conv_length = user_length*KM_CONV

# prints the converted length in kilometers
print("Length in km:", conv_length)
