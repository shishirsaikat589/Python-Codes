# colors = ["red", "green", "blue"]
#
# print(colors[0])
#
# colors[1] = "yellow"
# colors.append("purple")
# colors.remove("red")
#
# print(colors)

fruits = ["apple", "banana", "orange", "mango"]

fruits.append("grape")
fruits.remove("banana")

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("Total fruits:", len(fruits))

for fruit in fruits:
    print(fruit.upper())

fruits.sort()
print("Sorted:", fruits)

if "mango" in fruits:
    print("Mango is available.")
else:
    print("Mango is not available.")