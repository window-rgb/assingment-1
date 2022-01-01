# write a program to print the following string in the given order

print("twinkle twinkle little star ")
print("        how i wonder what you are")
print("                up above the world so high")
print("                like a diamond in the sky")
print("twinkle twinkle little star ")
print("        how i wonder what you are")
# ==========================================

# write a program to get the current version of python

import sys

print(sys.version)
# =========================================

# write a program to get the current date and time

from datetime import datetime

Current_time = datetime.now()
date_time = Current_time.strftime("%d/%m/%Y %H:%M:%S")
print("Current time and date is", date_time)
# ==============================================

# write a program to get area

import math

radius = int(input("Enter the Radius:"))
Rad_square = radius * radius
area = math.pi * (Rad_square)
print(area)
# ===============================================

# write a program to get the entered name in reverse

name = input("Enter your name:")
reversed_name = name[::-1]
print(reversed_name)
# ============================================

# wwrite a program to add to numbers

Num1 = float(input("Enter first number:"))
Num2 = float(input("Enter second number:"))
print(Num1, "+", Num2, "=", Num1 + Num2)
# ===========================================
