# x = 1
# a = float(x)
# b = str(x)
#
# print(a)
# print(b)


num_str = "123"
float_str = "45.67"
int_val = 8
float_val = 9.99

print("String to Numbers")
print(f"To Int   : int('{num_str}') -> {int(num_str)}")
print(f"To Float : float('{float_str}') -> {float(float_str)}")

print("\nNumber to Number")
print(f"To Int (Truncates) : int({float_val}) -> {int(float_val)}")
print(f"To Float   : float({int_val}) -> {float(int_val)}")
print(f"To Complex     : complex({int_val}) -> {complex(int_val)}")

print("\nAny to String")
print(f"To String : str({float_val}) -> '{str(float_val)}'")

print("\nBoolean Casting")
print(f"Zero is False     : bool(0) -> {bool(0)}")
print(f"Any number is True: bool(-5) -> {bool(-5)}")
print(f"Empty text is False: bool('') -> {bool('')}")
