"""
-------------------------------------------------------
Copies the contents of one file to another.
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""
# Imports
from functions import file_copy

fh_1 = open("words.txt", "r")
fh_2 = open("new_words.txt", "w")

# Copy the contents from source to destination
file_copy(fh_1, fh_2)

fh_1.close()
fh_2.close()
