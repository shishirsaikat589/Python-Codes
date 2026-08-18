age = int(input("Enter your age: "))
has_id = input("Do you have a valid ID? (yes/no): ").lower()
is_member = input("Are you a member? (yes/no): ").lower()

has_valid_id = has_id == "yes"
member = is_member == "yes"

can_enter = age >= 18 and has_valid_id

if can_enter:
    print("Access granted!")

    if member:
        print("Welcome, valued member!")
    else:
        print("You can enter as a regular visitor.")
else:
    print("Access denied.")

print("\nBoolean Results")
print("Age is 18 or older:", age >= 18)
print("Has valid ID:", has_valid_id)
print("Is a member:", member)
print("Can enter:", can_enter)