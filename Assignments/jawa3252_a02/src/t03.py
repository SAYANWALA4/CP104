"""
-------------------------------------------------------
Assignment 2, task 3
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-10-27"
-------------------------------------------------------
"""

unformated_date = int(input("Enter a date in the format YYYYMMDD: "))

year = (unformated_date // 10000)
month = (unformated_date // 100) - (year * 100)
day = unformated_date % 100

print(f"The reformatted date: {year:0>4d}/{month:0>2d}/{day:0>2d}")
