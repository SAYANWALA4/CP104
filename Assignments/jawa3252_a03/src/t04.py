"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-10-06"
-------------------------------------------------------
"""
"""
------------------------------------------------------------------------
Assignment 3, Task 4
------------------------------------------------------------------------
Author: Mike Bangar
ID:     169073786
Email:  bang3786@mylaurier.ca
__updated__ = '2023-10-21'
------------------------------------------------------------------------
"""

from functions import multiply_fractions
# multiply_fractions(1, 2, 3, 4) -> (3, 8, 0.375)
num1, den1, num2, den2 = 3, 8, 10, 17
num, den, divided = multiply_fractions(num1, den1, num2, den2)
print(f"multiply_fractions{num1, den1, num2, den2} -> {num, den, divided}")

num1, den1, num2, den2 = -5, 12, 7, 6
num, den, divided = multiply_fractions(num1, den1, num2, den2)
print(f"multiply_fractions{num1, den1, num2, den2} -> {num, den, divided}")

num1, den1, num2, den2 = -7, 2, -9, 4
num, den, divided = multiply_fractions(num1, den1, num2, den2)
print(f"multiply_fractions{num1, den1, num2, den2} -> {num, den, divided}")
