"""
-------------------------------------------------------
Assignment 2, Task 4
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-25"
-------------------------------------------------------
"""
flyers = int(input("Number of flyers: "))
people = int(input("Number of delivery people: "))

flyers_per_person = flyers // people
flyers_left_over = flyers % people

print(f"""
Flyers per delivery person: {flyers_per_person}
Flyers left over: {flyers_left_over}
""")
