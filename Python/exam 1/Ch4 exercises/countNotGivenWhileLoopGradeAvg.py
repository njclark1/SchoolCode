
total = 0   #accumulator    
counter = 0    #counter

print("Gradebook\n")
print("Enter -99 to stop entering grades.\n")

grade = float(input("Grade " + str(counter + 1) + ": ")) 
while not (grade >= 0 or grade == -99):
    print("A grade must be zero or more. Enter -99 to stop.")
    grade = float(input("Grade " + str(counter + 1) + ": "))

#counter + 1 is just for the print output Grade 1, Grade 2, ect

while grade != -99:
    total += grade
    counter += 1

    
    grade = float(input("Grade " + str(counter + 1) + ": "))
    while not (grade >= 0 or grade == -99):
        print("A grade must be zero or more. Enter -99 to stop.")
        grade = float(input("Grade " + str(counter + 1) + ": "))


print("\nAverage:", total / counter)