int_num = 42
float_num = 3.14159
complex_num = 3 + 4j

numbers = [int_num, float_num, complex_num]

print("Types")
for num in numbers:
    print(f"Value: {str(num):<12} Type: {type(num).__name__}")

print("\nDivision Operators")
print(f"Standard /  : 10 / 3  = {10 / 3}")
print(f"Floor //    : 10 // 3 = {10 // 3}")
print(f"Modulo %    : 10 % 3  = {10 % 3}")

print("\nFunctions & Properties")
print(f"Absolute    : abs(-7) = {abs(-7)}")
print(f"Round       : round({float_num}, 2) = {round(float_num, 2)}")
print(f"Complex     : Real={complex_num.real}, Imag={complex_num.imag}")
