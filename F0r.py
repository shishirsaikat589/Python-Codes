# fruits = ["apple", "banana", "cherry"]
#
# for fruit in fruits:
#     if fruit == "banana":
#         break
#     print(fruit)

numbers = [12, 7, 25, 4, 18, 9]

total = 0

for number in numbers:
    total += number

    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

print("Total:", total)
print("Average:", total / len(numbers))