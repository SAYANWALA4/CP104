"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-10-06"
-------------------------------------------------------
"""
# Imports
from functions import falling_distance

# falling_distance(15) -> 1102.5
time = 15
distance = falling_distance(time)
print(f"falling_distance({time}) -> {distance}")

time = 17
distance = falling_distance(time)
print(f"falling_distance({time}) -> {distance}")

time = 150
distance = falling_distance(time)
print(f"falling_distance({time}) -> {distance}")
