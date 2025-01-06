"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-10"
-------------------------------------------------------
"""
from functions import verify_sorted

numbers_asc = [1, 2, 3, 4, 5]
in_order_asc, index_asc = verify_sorted(numbers_asc)
print(f"List {numbers_asc} is sorted: {in_order_asc}, First unsorted index: {index_asc}")

numbers_desc = [5, 4, 3, 2, 1]
in_order_desc, index_desc = verify_sorted(numbers_desc)
print(f"List {numbers_desc} is sorted: {in_order_desc}, First unsorted index: {index_desc}")

numbers_unsorted = [3, 1, 4, 1, 5, 9, 2]
in_order_unsorted, index_unsorted = verify_sorted(numbers_unsorted)
print(f"List {numbers_unsorted} is sorted: {in_order_unsorted}, First unsorted index: {index_unsorted}")
