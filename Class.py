
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def greet(self):
#         print("Hello, my name is " + self.name)
#
# p1 = Person("John", 36)
#
# p1.greet()


class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 80:
            return "B"
        elif self.score >= 70:
            return "C"
        return "F"

    def display(self):
        print(f"Name: {self.name}")
        print(f"Score: {self.score}")
        print(f"Grade: {self.get_grade()}")


student = Student("Alex", 85)
student.display()