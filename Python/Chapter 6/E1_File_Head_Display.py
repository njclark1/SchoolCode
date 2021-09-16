# chapter 6 
# exercise 1


from pathlib import Path

LINES_TO_OUTPUT = 6


def main():
    print("This program outputs the first " + str(LINES_TO_OUTPUT) + " lines of a text file")

    # get filepath and verify if file exists
    filepath = input("file path: ")

    while not Path(filepath).is_file():
        print("This specified file does not exist")
        filepath = input("file path: ")
    # end while

    fileobj = open(filepath, "r")

    print()
    counter = 0
    for line in fileobj:
        if counter == LINES_TO_OUTPUT:
            break   #break for loop
        
        #end if
        print(line, end="")
        counter += 1
    #end for


main()