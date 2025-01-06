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
from functions import lawn_mow_time

# lawn_mow_time(20.0, 50.0, 4.0) -> 250.0

width, length, speed = 10, 20, 37
time = lawn_mow_time(width, length, speed)
print(f"lawn_mow_time({width},{length},{speed}) -> {time}")

width, length, speed = 12, 200, 10
time = lawn_mow_time(width, length, speed)
print(f"lawn_mow_time({width},{length},{speed}) -> {time}")

width, length, speed = -4.0, 100.0, 4.0
time = lawn_mow_time(width, length, speed)
print(f"lawn_mow_time({width},{length},{speed}) -> {time}")

