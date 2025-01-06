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
from functions import read_integers

# numbers file original
file = open("numbers.txt", "r", encoding="utf-8")
print(read_integers(file))
print()

# mixed numbers file
file2 = open("numbers2.txt", "r", encoding="utf-8")
print(read_integers(file2))
print()

# empty file
file3 = open("empty.txt", "r", encoding="utf-8")
print(read_integers(file3))
print()
