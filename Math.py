import math

numbers = [16, 25, 36, 49, 64]

for number in numbers:
    print(f"Number: {number}")
    print(f"Square root: {math.sqrt(number)}")
    print(f"Square: {math.pow(number, 2)}")
    print(f"Ceiling of sqrt: {math.ceil(math.sqrt(number))}")
    print()

print("Pi:", math.pi)
print("Factorial:", math.factorial(5))