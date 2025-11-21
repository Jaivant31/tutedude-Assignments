from random import sample


def factorial(n):
    factorial = 1
    for i in range(1 ,n + 1):
        factorial = factorial * i
    return factorial

sample_number = 5
result = factorial(sample_number)

print(f"factorial of {sample_number} is: {result}")