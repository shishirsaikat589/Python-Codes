age = 25
price = 19.99
name = "Alex"

fruits = ["apple", "banana"]

user = {"id": 101, "role": "admin"}
unique_ids = {101, 102, 101}

print("Variable Types")

variables = [age, price, name, fruits, user, unique_ids]

for item in variables:
    print(f"Value: {str(item):<25} Type: {type(item).__name__}")

print("\nType Conversion")
print(f"Float to Int:    {price} -> {int(price)}")
print(f"Int to String:   {age} -> '{str(age)}'")
print(f"List to Set:     {fruits} -> {set(fruits)}")
