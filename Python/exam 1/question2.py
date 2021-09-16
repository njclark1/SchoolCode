grade = float(input("What is your grade?: "))

if grade >= 70 and grade <= 100:
    print("passed")
elif grade >= 0 and grade < 70:
    print("failed")
elif grade < 0 or grade > 100:
    print("A grade cannot be less than zero or more than 100")