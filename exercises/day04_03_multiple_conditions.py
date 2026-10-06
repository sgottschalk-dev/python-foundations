# Multiple Conditions include if, elif, and else
score = int(input("Enter your score: "))

if score >= 90:
    print("Excellent!")
elif score >= 80:
    print("Good job!")
elif score >= 60:
    print("You passed!")
else:
    print("Keep trying!")