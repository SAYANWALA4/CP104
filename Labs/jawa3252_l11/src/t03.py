"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-29"
-------------------------------------------------------
"""
# Imports
from functions import generate_matrix_num
from functions import print_matrix_num
# Constants

matrix = generate_matrix_num(3, 4, -10, 10, "float")
print_matrix_num(matrix, 'float')
