# Chapter 3 Lab - Human to Dog Years

# Constants
ONE_YEAR_AGE = 15
TWO_YEARS_AGE = 9
MORE_THAN_TWO_MULTIPLIER = 5


def main():

    # Output program's purpose
    print("This program calculate's a dog's approximate age in \"dog years\" based on human years.\n")

    # Get human years from user
    repeat = "Y"
    while repeat == "Y":

        #                                               SET UP VALIDATION LOOP
        humanAge = float(input("Dog's age in human years? "))

        while humanAge < 0:
            print("\nTo calculate a dog's age in human years, please enter a value of zero or greater.")
            humanAge = float(input("\nDog's age in human years? "))
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
                format(dogAge, ",.1f"), "in dog years.\n")

            repeat = input("do another? (Y/n): ").upper()
    #end while

# end main function

# call main function
main()
