

class vehicle:

    def __init__(self, make, model, year, speed):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0

    def getMake(self):
        return self.make
    def getModel(self):
        return self.model
    def getYear(self):
        return self.year
    def getSpeed(self):
        return self.speed

    def accelerate(self):
        self.speed = self.speed + 5

    def decelerate(self):
        if self.speed > 5:
            self.speed = self.speed - 5
        elif self.speed <= 5:
            self.speed = 0

    def __str__(self):
        return "The " + self.getYear() + " " + self.getMake() + " " + self.getModel() + " is traveling at " + str(self.getSpeed()) + " MPH."

def main():
    print("Vehicle Class Test Program\n")
    myvehicle = vehicle("Chevy", "Spark", "2015", 0)


    print("Accelerating...")
    for _ in range(5):
        myvehicle.accelerate()
        print("Current speed: " + str(myvehicle.getSpeed()))


    print("\nBraking...")
    for _ in range(5):
        myvehicle.decelerate()
        print(myvehicle)

main()