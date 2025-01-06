"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-16"
-------------------------------------------------------
"""

subtotal = float(input("Food Charge: $"))
sales_tax = float(input("Sales Tax in (%): "))
tip = float(input("Tip in (%): "))

user_tax = subtotal * (sales_tax/100)
user_tip = subtotal * (tip/100)
final_total = subtotal+user_tax+user_tip

print("Cost of meal:")
print(f"Subtotal: $ {subtotal}")
print(f"    Tax: $ {user_tax}")
print(f"    Tip: $ {user_tip}")
print("------------------")
print(f"Total: $ {final_total}")
