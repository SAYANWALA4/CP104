"""
-------------------------------------------------------
task 8, lab 4
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-10-04"
-------------------------------------------------------
"""
# Imports
from functions import computer_costs
# Constants

computer_cost, computers_bought = computer_costs(1399, 87, 8.5)

print (f"{computer_cost: .2f}, {computers_bought: .2f}")

computer_cost, computers_bought = computer_costs(13, 87, 8.5)

print (f"{computer_cost: .2f}, {computers_bought: .2f}")

computer_cost, computers_bought = computer_costs(199, 87, 8.5)

print (f"{computer_cost: .2f}, {computers_bought: .2f}")

