# remember and, or, and not are logical operators
age = int(input("Enter your age: "))
has_permission = bool(input("Do you have permission? (True/Blank): ")) #error with string conversion evaluated as False if blank
if age >= 18 and has_permission:
    print("You can enter the club.")
else:
    print("You cannot enter the club.")
