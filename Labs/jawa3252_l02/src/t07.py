"""
-------------------------------------------------------
[program description]
a program that prompts the user to enter the number of flyers 
and the number of volunteers, and prints the number 
of flyers per volunteer and the number of flyers left over.
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-16"
-------------------------------------------------------
"""

no_of_flyers = int(input("Number of flyers: "))
no_of_vol = int(input("Number of volunteers: "))

flyers_per_vol = no_of_flyers//no_of_vol
flyers_left = no_of_flyers % no_of_vol

print("Flyers per volunteer: ", flyers_per_vol)
print("Flyers left over: ", flyers_left)
