"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""
# Imports
from functions import append_max_num

fh = open("numbers.txt", "a+")
print(append_max_num(fh))
fh.close()
