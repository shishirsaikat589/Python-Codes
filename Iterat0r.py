
# mytuple = ("apple", "banana", "cherry")
#
# myit = iter(mytuple)
#
# print(next(myit))

numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)

while True:
    try:
        number = next(iterator)
        print(number)
    except StopIteration:
        break