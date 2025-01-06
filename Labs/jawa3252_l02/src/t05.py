"""
-------------------------------------------------------
[program description]
Tells user total pay for the week.
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-16"
-------------------------------------------------------
"""

hour_rate = float(input("Hourly rate of pay: $"))
hour_worked = float(input("Hours worked in the week: "))
week_pay = hour_rate*hour_worked

print("Total pay for the week: $", week_pay)
