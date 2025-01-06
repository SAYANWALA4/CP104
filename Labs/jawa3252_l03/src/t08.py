"""
-------------------------------------------------------
Lab 3, task 8
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-23"
-------------------------------------------------------
"""

dirt = float(input("Enter amount of dirt (m^3): "))
gravel = float(input("Enter amount of gravel (m^3): "))
sand = float(input("Enter amount of sand (m^3): "))
total = dirt+gravel+sand

print()
print(f"Material   Cubic Metres")
print(f"Dirt        {dirt: 5.1f}")
print(f"Gravel      {gravel: 5.1f}")
print(f"Sand        {sand: 5.1f}")
print(f"Total       {total: 5.1f}")
