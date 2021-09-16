#chapter 4, exercise 1
#calories burned

#Constants
CALORIES_BURNED_PER_MINUTE = 4.2

#OUTPUT the purpose/description
print("This program calculates the number of calories burned in 5-minute intervals.\n")


for interval in range(5, 31, 5):
    print("Calories burned in ", interval, "minutes:", interval * CALORIES_BURNED_PER_MINUTE)
#end for



# FOR each interval between 5 and 30 minutes in multiples of 5
#   OUTPUT calories burned for this particular interval
# END FOR

