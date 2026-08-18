
# age = 20
#
# if age < 13:
#     print("Child")
# elif age < 18:
#     print("Teenager")
# else:
#     print("Adult")

score = float(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}")
print(f"Grade: {grade}")

if score >= 60:
    print("Status: Passed")
else:
    print("Status: Failed")