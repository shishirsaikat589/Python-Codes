
#
# def greet(name):
#     print("Hello, " + name)
#
# greet("Emil")


def calculate_average(numbers):
    return sum(numbers) / len(numbers)


def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


scores = [85, 92, 78, 96, 88]

average = calculate_average(scores)

print("Scores:", scores)
print("Average:", average)
print("Grade:", get_grade(average))