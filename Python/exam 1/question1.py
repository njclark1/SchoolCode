print("This program asks the user for their name and age, and returns it in a sentence")

name_placeholder = ""  
age_placeholder = ""

name_placeholder = str(input("What is your name?: "))
age_placeholder = str(input("What is your age?: "))

print("\"My name is ", name_placeholder, ";", " I am ", age_placeholder, " years old.\"", sep="")