"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-17"
-------------------------------------------------------
"""
# user defined quanity and price of a dosa
user_cost = float(input("Cost of 1 dosa: $"))
user_ammount = int(input("Number of dosa: "))

total_due = user_cost * user_ammount

print(f"Total cost of {user_ammount} dosas: $ {total_due}")
