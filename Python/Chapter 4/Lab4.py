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
print("\nCredit/debit: $", format(total, ".2f"), sep="")

#Output total cost Cash
print("Cash: $", round(total, 2), sep="")

#I was close to figuring out the Cash part and ran out of time to submit
#Completely my fault for procrastinating and I'm sad about it
#Here's where I was going with it
#cash_remain = (price * 100) % 5
#if cash_remain > .025 print("Cash:", price)