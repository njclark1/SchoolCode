



value = float(input("please enter a numeric value between 0 and 100: "))

while value < 0 or value > 100:
    print("\nYou must enter a value between 0 and 100.")
    value = float(input("\nvalue? "))

print(value)
