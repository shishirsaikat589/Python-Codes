# a = 15
# b = 4
#
# print(a % b)
# print(a // b)
# print(a ** b)
#
# a += 10

age = int(input("Enter your age: "))
score = float(input("Enter your score: "))
is_verified = input("Are you verified? (yes/no): ").lower() == "yes"

eligible = age >= 18 and score >= 70 and is_verified

if eligible:
    print("You are eligible.")
else:
    print("You are not eligible.")

print("Age requirement:", age >= 18)
print("Score requirement:", score >= 70)
print("Verified:", is_verified)
print("Eligible:", eligible)