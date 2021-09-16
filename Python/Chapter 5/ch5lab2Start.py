def convertDecimalTo(number, base):
    result = ""
    
    while number > 0:
        remainder = number % base 
    
        if remainder< 10:
            result = str(remainder) + result
        # ELSE IF remainder is equal to 10 THEN
        #   LET result be the result with "A" at the beginning
        # ELSE IF remainder is equal to 11 THEN
        #   LET result be the result with "B" at the beginning
        # ELSE IF do the same for 12, 13, 14, and 15
        # END IF
        
        number = number // base
    return result
# end function
def main():
    print("Decimal to Base 2-16 converter\n")
    number = int(input("Enter a number to convert: "))

    example = convertDecimalTo(number, 2)
    
    print(example)
# end function
main()