

# fruits = ("apple", "banana", "cherry")
#
# print(fruits[1])
# print(len(fruits))
#
# a, b, c = fruits
#
# print(b)

student = ("Alex", 20, "Python", 85)

name, age, course, score = student

print("Name:", name)
print("Age:", age)
print("Course:", course)
print("Score:", score)

print("First:", student[0])
print("Last:", student[-1])
print("Length:", len(student))

if score >= 80:
    print("Grade: A")
else:
    print("Grade: B")

print("Python" in student)