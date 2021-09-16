# Chapter 3 Lab - Human to Dog Years

# Constants
ONE_YEAR_AGE = 15
TWO_YEARS_AGE = 9
MORE_THAN_TWO_MULTIPLIER = 5

# Output program's purpose
print("This program calculate's a dog's approximate age in \"dog years\" based on human years.\n")

# Get human years from user
humanAge = float(input("Dog's age in human years? "))

if humanAge < 0:
    print("\nHuman age must be a positive number.")
else:
    # Human age to dog age calculation
    if humanAge <= 1:
        dogAge = ONE_YEAR_AGE * humanAge
    elif humanAge <= 2:
        dogAge = ONE_YEAR_AGE + (TWO_YEARS_AGE * (humanAge - 1))
    else:
        dogAge = ONE_YEAR_AGE + TWO_YEARS_AGE + (MORE_THAN_TWO_MULTIPLIER * (humanAge - 2))
    # end if

    print("\nA dog with a human age of", format(humanAge, ",.1f"), "years is", 
          format(dogAge, ",.1f"), "in dog years.")
# end if