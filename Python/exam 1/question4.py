def getSeason(month):

    season = ""
    if month < 1 or month > 12:
        print("The specified value isn't a valid month.")
        month = int(input("What is the numeric Month? "))

    if month == 1 or month == 2 or month == 12:
        season = "Winter"
    elif month >= 3 and month <= 5:
        season = "Spring"
    elif month >= 6 and month <= 8:
        season = "Summer"
    elif month >= 9 and month <= 11:
        season = "Fall"

    return season


def main():
    month = int(input("What is the numeric Month? "))
    season = getSeason(month)
    print(season)

main()


