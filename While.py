# i = 0
#
# while i < 6:
#     i += 1
#
#     if i == 3:
#         continue
#
#     print(i)

number = 1
total = 0

while number <= 10:
    total += number

    if number % 2 == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

    number += 1

print("Total:", total)