import random

class Deck:
    def __init__(self, cards):
        self.cards = []
        if(type(cards) == int):
            match(cards):
                #Default Deck
                case 0:
                    self.addCard("Ace of Hearts", "AH")
                    self.addCard("Two of Hearts", "2H")
                    self.addCard("Three of Hearts", "3H")
                    self.addCard("Four of Hearts", "4H")
                    self.addCard("Five of Hearts", "5H")
                    self.addCard("Six of Hearts", "6H")
                    self.addCard("Seven of Hearts", "7H")
                    self.addCard("Eight of Hearts", "8H")
                    self.addCard("Nine of Hearts", "9H")
                    self.addCard("Ten of Hearts", "10H")
                    self.addCard("Jack of Hearts", "JH")
                    self.addCard("Queen of Hearts", "QH")
                    self.addCard("King of Hearts", "KH")

                    self.addCard("Ace of Clubs", "AC")
                    self.addCard("Two of Clubs", "2C")
                    self.addCard("Three of Clubs", "3C")
                    self.addCard("Four of Clubs", "4C")
                    self.addCard("Five of Clubs", "5C")
                    self.addCard("Six of Clubs", "6C")
                    self.addCard("Seven of Clubs", "7C")
                    self.addCard("Eight of Clubs", "8C")
                    self.addCard("Nine of Clubs", "9C")
                    self.addCard("Ten of Clubs", "10C")
                    self.addCard("Jack of Clubs", "JC")
                    self.addCard("Queen of Clubs", "QC")
                    self.addCard("King of Clubs", "KC")

                    self.addCard("Ace of Diamonds", "AD")
                    self.addCard("Two of Diamonds", "2D")
                    self.addCard("Three of Diamonds", "3D")
                    self.addCard("Four of Diamonds", "4D")
                    self.addCard("Five of Diamonds", "5D")
                    self.addCard("Six of Diamonds", "6D")
                    self.addCard("Seven of Diamonds", "7D")
                    self.addCard("Eight of Diamonds", "8D")
                    self.addCard("Nine of Diamonds", "9D")
                    self.addCard("Ten of Diamonds", "10D")
                    self.addCard("Jack of Diamonds", "JD")
                    self.addCard("Queen of Diamonds", "QD")
                    self.addCard("King of Diamonds", "KD")

                    self.addCard("Ace of Spades", "AS")
                    self.addCard("Two of Spades", "2S")
                    self.addCard("Three of Spades", "3S")
                    self.addCard("Four of Spades", "4S")
                    self.addCard("Five of Spades", "5S")
                    self.addCard("Six of Spades", "6S")
                    self.addCard("Seven of Spades", "7S")
                    self.addCard("Eight of Spades", "8S")
                    self.addCard("Nine of Spades", "9S")
                    self.addCard("Ten of Spades", "10S")
                    self.addCard("Jack of Spades", "JS")
                    self.addCard("Queen of Spades", "QS")
                    self.addCard("King of Spades", "KS")
                    pass
        elif(type(cards) == list):
            self.cards = cards
    
    def cardDisplay(self):
        outputString = ""
        for card in self.cards:
            outputString = outputString + card.getAbrev() + " "
        return outputString

    def shuffle(self):
        random.shuffle(self.cards)

    def empty(self):
        self.cards = []

    def addCard(self, name, abrev):
        self.cards.append(Card(name, abrev))

    def drawCard(self):
        return self.cards.pop(0)

    def viewTopCard(self):
        return self.cards[0]

class Card:
    def __init__(self, name, abrev):
        self.name = name
        self.abrev = abrev

    def getName(self):
        return self.name
    
    def getAbrev(self):
        return self.abrev