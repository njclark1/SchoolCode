
total = 0
count = int(input("How many grades to enter? "))

for value in range(count):
    grade = float(input("Grade " + str(value + 1) + ": "))
    total += grade

print("Average:", total / count)