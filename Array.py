
# cars = ["Ford", "Volvo", "BMW"]
#
# print(cars[0])
#
# cars[1] = "Toyota"
#
# print(cars)

numbers = [12, 7, 25, 4, 18, 9]

numbers.append(30)
numbers.remove(4)

for number in numbers:
    print(number)

print("First:", numbers[0])
print("Last:", numbers[-1])
print("Total:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
print("Largest:", max(numbers))
print("Smallest:", min(numbers))