#Chapter 6 Lab

#create writeBiography function
def writeBiography(filename, name, major, college, gradyear, hobbies):
    #create try...except
    try:
        fileobject = open(filename, "w")
    except:
        print("An error occurred")

    #write to file
    fileobject.write("<html>")
    fileobject.write("<head><title>" + college + " student: " + name + "</title></head>")
    fileobject.write("<body>")
    fileobject.write("<center><h1>" + name + "<h1></center>")
    fileobject.write("<hr />")
    fileobject.write("My name is " + name + ". I am a " + major + " major at " + college + ". I expect to graduate in " + gradyear + ".")
    fileobject.write("<br /><br />")
    fileobject.write(hobbies + ".")
    fileobject.write("<hr />")
    fileobject.write("</body>")
    fileobject.write("<html>")

    fileobject.close()

    print("Done!")

#create main function
def main():

    #output program purpose
    print("Student Web Page Generator\nThis program generates a web page based on entered information.")
    
    filename = "biography.html"

    name = input("\nEnter your name: ")
    while len(name) <= 0:
        name = input("A name must have more than one character. Enter your name: ")

    major = input("Enter your major: ")
    while len(major) <= 0:
        major = input("A major must have more than one character. Enter your major: ")

    college = input("Enter your college: ")
    while len(college) <= 0:
        college = input("A college must have more than one character. Enter your college: ")

    gradyear = input("Enter your expected graduation year: ")
    while len(gradyear) <= 0:
        gradyear = input("An expected graduation year must have more than one character. Enter your expected graduation year: ")

    hobbies = input("Enter a sentance stating your hobbies and interests: ")

    print("Writing web page to " + '"'+ filename + '"' + ".")

    #call writeBiography function
    writeBiography(filename, name, major, college, gradyear, hobbies)


#call main
main()