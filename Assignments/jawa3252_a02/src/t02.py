"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-25"
-------------------------------------------------------
"""

pos_dig = int(input("Enter a postive digit number: "))

first_digit = pos_dig // 10
second_digit = pos_dig % 10
answer = first_digit - second_digit

print(f"The difference of the digits of {pos_dig} is {answer}")
