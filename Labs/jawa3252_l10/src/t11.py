"""
-------------------------------------------------------
Finds the last word with the longest length in the file.
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""
# Imports
from functions import find_longest

fh = open("words.txt", "r")

# Print the result from the find_longest function
print(find_longest(fh))

fh.close()
