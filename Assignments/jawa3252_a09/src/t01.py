"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
from functions import file_top

# Printing 5 Lines
file_handle = open("mnm.txt", "r", encoding="utf-8")
file_top(file_handle, 5)

print()

# Printing No Lines

file_handle = open("mnm.txt", "r", encoding="utf-8")
file_top(file_handle, 0)

print()

# Printing too many lines

file_handle = open("mnm.txt", "r", encoding="utf-8")
file_top(file_handle, 28)

print()
