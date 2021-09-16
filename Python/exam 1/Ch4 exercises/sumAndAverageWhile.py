

counter = 0
total = 0
print("This program totals and averages given numbers")
print("\nEnter a negative number to stop\n")

number = float(input("number " + str(counter + 1) + ": ")) 

while number >= 0:
    total += number
    counter += + 1

    number = float(input("number " + str(counter + 1) + ": ")) 

print("\nTotal is:", total)
print("Average is:", total / counter)
