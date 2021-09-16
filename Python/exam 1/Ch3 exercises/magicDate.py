def main():
    month = int(input("Enter a month: "))
    day = int(input("Enter a day: "))
    year = int(input("Enter a year: "))

    if (month * day) == year:
        print("the date ", month, "/", day, "/", year, " is a magic date, hooray!", sep='')
    else:
        print("the date ", month, "/", day, "/", year, " is not a magic date, sorry", sep='')

main()