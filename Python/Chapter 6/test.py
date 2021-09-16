def main():
    name = input("what is the name?: ")
    return name
    

def writeBiography(name):

    fileObj = open("biography.html", "w")

    fileObj.write(name)


#in thewriteBiography() function, use a try...except statement to open the specified file for outputand write the data to the output file.






main()