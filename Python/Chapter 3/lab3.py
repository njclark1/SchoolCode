#Program's purpose
print("""This program calculates a dog's approximate age in "dog years" based on human years.\n""")

#Get dog age from user in human years
age = float(input("Dog's age in human years? "))

if age <0:
    print("\nHuman years must be a positive number.")

elif age <1:
    print("\nA dog with a human age of" , age, "years is", (age*15), "in dog years.")

elif age >= 1 and age < 2:
    print("\nA dog with a human age of" , age, "years is", 15 + ((age-1)*9), "in dog years.")

elif age >= 2:
    print("\nA dog with a human age of" , age, "years is", ((age-2)*5)+24, "in dog years.")

#Please ignore if left. Just playing with the program.
    input('\nPress ENTER to exit')