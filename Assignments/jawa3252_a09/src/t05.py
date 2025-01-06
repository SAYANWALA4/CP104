"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Jaspreet Jawanda
ID:      169083252
Email:   jawa3252@mylaurier.ca
__updated__ = "2024-11-24"
-------------------------------------------------------
"""
from functions import student_stats

file = open("students.txt", "r", encoding="utf-8")
l_id, h_id, avg = student_stats(file)
print(f"Lowest Mark Student ID: {l_id}")
print(f"Highest Mark Student ID: {h_id}")
print(f"Average Mark: {avg}")
print()

file = open("students2.txt", "r", encoding="utf-8")
l_id, h_id, avg = student_stats(file)
print(f"Lowest Mark Student ID: {l_id}")
print(f"Highest Mark Student ID: {h_id}")
print(f"Average Mark: {avg}")
print()

file = open("empty.txt", "r", encoding="utf-8")
l_id, h_id, avg = student_stats(file)
print(f"Lowest Mark Student ID: {l_id}")
print(f"Highest Mark Student ID: {h_id}")
print(f"Average Mark: {avg}")
