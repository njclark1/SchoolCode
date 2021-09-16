from random import choice

class Coin:

    def _init_():
        self._denomination = "Penny"
        self._worth = 0.01
        self._sideUp = "Heads"
        self._sideDown = "Tails"

    def setDenomination(self, denomination):
        self._denomination = denomination

        if denomination.lower() == "penny":
            self.worth = 0.01
        elif denomination.lower() == "nickel":
            self.worth = 0.05
        elif denomination.lower() == "dime":
            self.worth = 0.10
        elif denomination.lower() == "quarter":
            self.worth = 0.25


        #accesors
    def getDenomination(self):
        return self._denomination

    def getWorth(self):
        return self.worth

    def getSideUp(self):
        return self.sideUp

    def toss(self):
        self.sideUp = choice(["Heads", "Tails"])
        




def main():
    myCoin = Coin()

    myCoin.setDenomination("Quarter")

    print(myCoin.getDenomination())
    print(myCoin.getWorth())

    #for _ in range(10):
     #   myCoin.toss()
      #  print(myCoin.getSideUp())
main()