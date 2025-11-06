""""""
from encodings import undefined

num1 =float(input("Enter a number 1: "))
num2 =float(input("Enter a number 2: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

if num1 !=0:
    division = num1 / num2
else:
    division = undefined

print("\nresults:")
print("addition",addition)
print("subtraction",subtraction)
print("multiplication",multiplication)
print("division",division)
