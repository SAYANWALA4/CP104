"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from functions import time_split

days, hours, minutes, seconds = time_split(956000)

print (f"{days}, {hours}, {minutes}, {seconds}")

days, hours, minutes, seconds = time_split(956)

print (f"{days}, {hours}, {minutes}, {seconds}")

days, hours, minutes, seconds = time_split(9000)

print (f"{days}, {hours}, {minutes}, {seconds}")
