
#
# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 2024
# }
#
# print(car["model"])
#
# car["color"] = "red"
# car.pop("brand")
#
# print(car)

student = {
    "name": "Alex",
    "age": 20,
    "course": "Python",
    "score": 85
}

print("Name:", student["name"])
print("Course:", student["course"])

student["score"] = 92
student["level"] = "Intermediate"

print("\nStudent:")
for key, value in student.items():
    print(f"{key}: {value}")

if student["score"] >= 80:
    print("\nGrade: A")
else:
    print("\nGrade: B")

print("Has email:", "email" in student)
print("Total fields:", len(student))