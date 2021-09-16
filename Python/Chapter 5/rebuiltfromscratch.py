    # Output program's purpose
print("Decimal to Base 2-16 converter\n")

def main():
    print("Decimal to Base 2-16 converter\n")

    number = int(input("Enter a number to convert: "))

    for base in range(1, 17):
        print (convertDecimalTo(number, base))
    
#end main function

def convertDecimalTo(number, base):

    result = ""
    number = number // base

    while number > 0: 
        remainder = number % base 

        if remainder < 10:
            result = (remainder) + number
            return result

        else:
            result = 8
            return result


main()

#    while number > 0: remainder = number % base 