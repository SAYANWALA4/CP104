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

from functions import footage_to_acres

intial = 15
acres = footage_to_acres(intial)
print(f"footage_to_acres({intial}) -> {acres}")

intial = 15000
acres = footage_to_acres(15000)
print(f"footage_to_acres({intial}) -> {acres}")

intial = 100000.0
acres = footage_to_acres(100000.0)
print(f"footage_to_acres({intial}) -> {acres}")
