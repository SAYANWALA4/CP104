"""
-------------------------------------------------------
[program description]
This program calculates and prints compound interest.
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-17"
-------------------------------------------------------
"""

# Takes in user input for the principal, interest, term and compound
principal = float(input("Principal: $"))
interest = float(input("Interest (%): "))
term = int((input("Number of years: ")))
compound = int(input("Number of times interest compounded per year: "))
interest /= 100

# Computes the compound interest accumulated
balance = principal * (1 + (interest/compound))**(compound*term)


print(f"""
Balance: $ {balance}""")
