"""
-------------------------------------------------------
[program description]
Program converts celsius temperature to fahrenheit
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-16"
-------------------------------------------------------
"""
# Imports

# Constants
FREEZING = 32

temp_celsius = int(input("Temperature (C):"))
temp_fahrenheit = int((9/5)*temp_celsius + FREEZING)

print("Temperature (F):", temp_fahrenheit)
