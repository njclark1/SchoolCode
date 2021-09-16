# Chapter 4 Lab - No more Canadian Pennies!

from math import floor

# Output program's purpose
print("This program calculates the total cost of a series of items based on payment method.")
print("Enter -1 to stop entering item prices.\n")

# Sentinel value
STOP_VALUE = -1

total = 0       # Holds the running total
counter = 1     # Holds the number of items entered

# Get first item prices from user
itemPrice = float(input("Item " + str(counter) + ": $"))

# Make sure first value entered isn't the sentinel
if itemPrice != STOP_VALUE:

    while itemPrice != STOP_VALUE:
        total += itemPrice      # Add item price to running total
        counter += 1            # Increment number of items entered

        # Get another item price from user
        itemPrice = float(input("Item " + str(counter) + ": $"))
    # end while 

    pennies = round((total - floor(total)) * 100)       # Calculate number of pennies in total
    remainingPennies = pennies % 5                      # Determine how cash total should be rounded
    
    # Determine if the remaining pennies should be added or removed from total
    if remainingPennies < 2.5:
        cashTotal = total - (remainingPennies / 100)            # Round down
    else:
        cashTotal = total + ((5 - remainingPennies) / 100)      # Round up
    # end if

    # Output price based on payment method
    print("\nCredit/debit: $" + format(total, ",.2f"))
    print("Cash: $" + format(cashTotal, ",.2f"))
# end if