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
from functions import line_numbering

fileread = open("wilde.txt", "r", encoding="utf-8")
filewrite = open("wildewrite.txt", "w", encoding="utf-8")
line_numbering(fileread, filewrite)
print("Success")
print()

fileread2 = open("wilde2.txt", "r", encoding="utf-8")
filewrite2 = open("wildewrite2.txt", "w", encoding="utf-8")
line_numbering(fileread2, filewrite2)
print("Success")
print()

fileread3 = open("empty.txt", "r", encoding="utf-8")
filewrite3 = open("wildewrite3.txt", "w", encoding="utf-8")
line_numbering(fileread3, filewrite3)
print("Success")
print()
