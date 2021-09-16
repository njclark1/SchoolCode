# chapter 4
# exercise 2: C to F

#Constants
CALORIES_BURNED_PER_MINUTE = 4.2

#OUTPUT the purpose/description
print("Celsius to Fahrenheit Table\n")

print("Celsius\t\tFahrenheit")
print("-------\t\t----------")

for celsiusTemp in range(21):
    fahrenheitTemp = 9 / 5 * celsiusTemp + 32

#end for



# FOR each temperature between 0 and 20
#   SET fahrenheit equal to 9 divided by 5 multiplied by this Celsius temperature plus 32
#   OUTPUT this Celsius temperature and f
# END FOR

# F = ((9 / 5) * C) + 32