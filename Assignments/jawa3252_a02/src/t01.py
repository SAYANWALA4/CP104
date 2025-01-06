"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-09-27"
-------------------------------------------------------
"""

# Constants
TAX = 18.5

total_sales = float(input("Enter the total sales: "))
projected_taxes = total_sales * (TAX / 100)

print(f"""
Projected Tax Report
{'-':-^26s}
Total Sales: ${total_sales:.2f}
Annual Tax:  %{TAX:.2f}
{'-':-^26s}
Tax:         ${projected_taxes:.2f}
""")
