# Chapter 3 Lab - Human to Dog Years

# Constants
ONE_YEAR = 15
TWO_YEARS = 9
MORE_THAN_TWO_MULTIPLIER = 5


# Output program's purpose
print("This program calculate's a dog's approximate age in \"dog years\" based on human years.\n")

# Get human years from user
humanYears = float(input("Dog's age in human years? "))

# Determine output
if humanYears < 0:
    print("\nHuman years must be a positive number.")
else:
    if humanYears <= 1:
        dogYears = ONE_YEAR * humanYears
    elif humanYears <= 2:
        dogYears = ONE_YEAR + (TWO_YEARS * (humanYears - 1))
    else:
        dogYears = ONE_YEAR + TWO_YEARS + (MORE_THAN_TWO_MULTIPLIER * (humanYears - 2))
    # end if

    print("\nA dog with a human age of", format(humanYears, ",.1f"), "years is", format(dogYears, ",.1f"), "in dog years.")
# end if