#programmers: Jonathan, Nick, Craig
#date: 11 11 2021
#this program holds a conversation with Jonathan's wife

#initial variables
#facts


wife = "peyton"
age = 25
occupation = "nurse"
exclamation = "fuck your coworkers!"

#emotions

#say hi to user
print("This program holds a conversation with Jonathan's wife")
#ask user for name
name = str(input("Hi! What is your name?"))
#confirm user name
if  name.lower() == wife:
    print("You are Peyton!")
else:
    print("you are not peyton") 

#get user age
givenAge = int(input("What is your age?"))
#confirm age
if  givenAge == age:
    print("Very cool, enjoy your 20s")
elif givenAge > age:
    print("You're not that old, you lier")
else:
    print("Nice try, you old fart")

#get user occupation
givenOccupation = str(input("What do you do for a living?"))

if  givenOccupation.lower() == occupation:
    print("That's great, I hope you like it")
elif  givenOccupation.lower() == "nursing":
    print("That's great, I hope you like it")
else:
    print("Nice try, you lier")

#after asking what she does for work, ask if she worked today
#if she did, ask her if it went well, yes or no
#if no, console her

#have it ask how she is doing in general