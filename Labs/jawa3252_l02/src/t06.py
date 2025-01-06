"""
-------------------------------------------------------
[program description]
program calculates the monthly payments for the 
mortgage.
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-20"
-------------------------------------------------------
"""


principal = float(input("Mortgage principal ($): "))
no_of_payments = int(input("Number of years: "))
no_of_payments *= 12
interest = int((input("Yearly interest rate (%): ")))
monthly_interest = (interest/100)/12

monthly_payment = (principal * (monthly_interest * (1 + monthly_interest) ** no_of_payments) /
                   ((1 + monthly_interest) ** no_of_payments - 1))

monthly_payments = principal * \
    ((monthly_interest*(1+monthly_interest)**no_of_payments) /
     ((1+monthly_interest)**no_of_payments)-1)

print("The monthly payments are: $ ", monthly_payment)
