#programmers: Jonathan, Nick Craig
#date 11 11 2021
#this program holds a conversation with Jonathan's wife

#initial variables
#facts
wife = "peyton"
age = 25
occupation = "nurse"
exclamation = "screw your lazy classmates"
mood = "unpredictable"
diet = "vegan"

#say hi to user
print ("this program holds a conversation with Jonathan's wife")

#greeting user
name = str(input("Hi! What is your name?"))
if name == wife:
    print("hi peyton!")

else:
    print("you are not Peyton! Self Destructing in 3....2....1....")


#ask user age


givenAge = int(input("Nice to see you! What is your age?"))
if givenAge == age:
    print("25 years young!")

elif givenAge> age:
    print("you are not that old yet! calm down!") 
else:
    print("Nice try, you old granny")

#get user occupation

givenOccupation = str(input("what do you do for a living?"))

if givenOccupation.lower() == occupation:
    print("so you are sexy AND smart!")
elif givenOccupation.lower() == "nursing":
    print("what a nice career choice!")
else: 
    print("thats not what i heard from ETSU!")