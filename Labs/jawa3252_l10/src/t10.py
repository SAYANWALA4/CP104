"""
-------------------------------------------------------
Counts the number of appearances of a word in the file.
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-22"
-------------------------------------------------------
"""
# Imports
from functions import count_frequency_word

fh = open("words.txt", "r")

# Print the result from the count_frequency_word function
print(count_frequency_word(fh, "apple"))

fh.close()
