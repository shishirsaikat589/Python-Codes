
#
# for i in range(6):
#     print(i)
#
# for i in range(2, 6):
#     print(i)

numbers = range(1, 11)

for number in numbers:
    print(number, number ** 2)

print("Total:", sum(numbers))
print("Count:", len(numbers))
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))