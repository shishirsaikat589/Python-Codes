# colors = {"red", "green", "blue"}
# #
# # print(colors)
# #
# # colors.add("yellow")
# # colors.discard("green")
# #
# # print(len(colors))

python = {"Alex", "John", "Emma", "David"}
java = {"John", "Emma", "Sarah", "Michael"}

print("Python:", python)
print("Java:", java)

print("Both:", python & java)
print("All students:", python | java)
print("Python only:", python - java)
print("Java only:", java - python)

python.add("Sarah")
python.discard("David")

print("Updated Python:", python)
print("Has Emma:", "Emma" in python)
print("Total Python students:", len(python))