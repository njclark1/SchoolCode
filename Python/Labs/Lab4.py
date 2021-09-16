#Output program purpose
print ("This program calculates the total cost of a series of items based on the Canadian payment method.")

#Output how to stop entering values
print("Enter -1 to stop entering item prices\n")

# Set variables equal to zero
counter = 0
total = 0

# input the price of an item
price = float(input("item " + str(counter + 1) + ": $ "))
while price >= 0:
    total +=price
    counter += 1

    price = float(input("item " + str(counter + 1) + ": $ "))

#Output total cost Debit/Credit
print("\nCredit/debit: $", format(total, ".2f"))

#Output total cost Cash
