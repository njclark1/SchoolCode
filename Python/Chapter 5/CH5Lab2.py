def convertDecimalTo(number, base):
    result = ""
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    
    #while loop
    while number > 0:
        remainder = number % base 
    
        if remainder< 10:
            result = str(remainder) + result
            pass
        elif remainder == 10:
            result = A + result
            pass
        elif remainder == 11:
            result = B + result
            pass
        elif remainder == 12:
            result = C + result
            pass
        elif remainder == 13:
            result = D + result
            pass
        elif remainder == 14:
            result = E + result
            pass
        elif remainder == 15:
            result = F + result
            pass
    #end while loop    
        
        number = number // base
    return result
# end function

# main function
def main():
    # print program purpose to user
    print("Decimal to Base 2-16 converter\n")

    # get input from user
    number = int(input("Enter a number to convert: "))

    # validation loop
    while number < 0:
            print("\nplease enter a positive whole number.")
            number = int(input("Enter a number to convert: "))
    # end validation loop
    
    # for loop
    for base in range(2, 17):
        returnvalue = convertDecimalTo(number, base)
        print("base ", base,": ", returnvalue, sep="")
    # end for loop

# end function

# call main function
main()