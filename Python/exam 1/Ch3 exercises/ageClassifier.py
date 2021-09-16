def main():

    repeat = "Y"
    while repeat == "Y":

        age = int(input("please input age: "))

        classi = ""

        while age < 0:
            print("\nAge must be a positive number.")
            age = int(input("please input age: "))

        if age <= 1:
            classi = "infant"

        elif age > 1 and age < 13:
            classi = "child"

        elif age >= 13 and age < 18:
            classi = "teenager"

        elif age >= 18:
            classi = "adult"

        print("This person is a", classi)

        repeat = input("Would you like to convert another number? (Y/n): ").upper()

main()