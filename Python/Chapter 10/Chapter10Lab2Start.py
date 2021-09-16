from random import shuffle

class Card:

    def __init__(self, rank, color, suit, value):

        self.rank = rank
        self.color = color
        self.suit = suit
        self.value = 0

    def getrank(self):
        return self.rank

    def getcolor(self):
        return self.color

    def getsuit(self):
        return self.suit

    def getvalue(self):
        return self.value

    def __str__(self):
        return self.getrank() + " " + "of" + " " + self.getsuit()

class Deck:
    
    __cards = []

    def __init__(self):
        self.__buildDeck()
    
    def __buildDeck(self):

        faces = ['Ace'] + list(range(2,11)) + [ 'Jack', 'Queen', 'King']
        suits = ['Diamonds', 'Hearts', 'Clubs', 'Spades']
        for suit in suits: 
            for ind, face in enumerate(faces): 
                color = ""                   
                # print(color + ' ' + str(face) + ' of ' + suit + ' : ' + str(ind+1))
                if (suit == 'Diamonds' or suit == 'Hearts'): 
                    color = 'Red'
                else: 
                    color = 'Black'
                
                self.__cards.append(Card(str(face), color, suit, ind+1))
                #print(self.__cards[5])


    def shuffle(self):

        shuffle(self.__cards)
        
    def drawCard(self):
    
        cardtoberemoved = (self.__cards[0])
        self.__cards.remove(cardtoberemoved)
        return cardtoberemoved
        

    def __str__(self):
        numcards = len(self.__cards)
        rv = ("There are " + str(numcards) + " cards remaining in the deck.")
        return rv

def main():
    counter = 0
    mydeck = Deck()

    print("\nPlaying Cards Test Program\n")

    mydeck.shuffle()

    for _ in range(10):
        counter += 1
        print("Card " + str(counter) + ": " + str(mydeck.drawCard()))
        print(mydeck)


main()