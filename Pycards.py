import random

class Deck:
    def __init__(self, cards):
        self.cards = []
        if(type(cards) == int):
            match(cards):
                #No Deck
                case -1:
                    pass
                #Default Deck
                case 0:
                    self.createCard("Ace of Hearts", "AH")
                    self.createCard("Two of Hearts", "2H")
                    self.createCard("Three of Hearts", "3H")
                    self.createCard("Four of Hearts", "4H")
                    self.createCard("Five of Hearts", "5H")
                    self.createCard("Six of Hearts", "6H")
                    self.createCard("Seven of Hearts", "7H")
                    self.createCard("Eight of Hearts", "8H")
                    self.createCard("Nine of Hearts", "9H")
                    self.createCard("Ten of Hearts", "10H")
                    self.createCard("Jack of Hearts", "JH")
                    self.createCard("Queen of Hearts", "QH")
                    self.createCard("King of Hearts", "KH")

                    self.createCard("Ace of Clubs", "AC")
                    self.createCard("Two of Clubs", "2C")
                    self.createCard("Three of Clubs", "3C")
                    self.createCard("Four of Clubs", "4C")
                    self.createCard("Five of Clubs", "5C")
                    self.createCard("Six of Clubs", "6C")
                    self.createCard("Seven of Clubs", "7C")
                    self.createCard("Eight of Clubs", "8C")
                    self.createCard("Nine of Clubs", "9C")
                    self.createCard("Ten of Clubs", "10C")
                    self.createCard("Jack of Clubs", "JC")
                    self.createCard("Queen of Clubs", "QC")
                    self.createCard("King of Clubs", "KC")

                    self.createCard("Ace of Diamonds", "AD")
                    self.createCard("Two of Diamonds", "2D")
                    self.createCard("Three of Diamonds", "3D")
                    self.createCard("Four of Diamonds", "4D")
                    self.createCard("Five of Diamonds", "5D")
                    self.createCard("Six of Diamonds", "6D")
                    self.createCard("Seven of Diamonds", "7D")
                    self.createCard("Eight of Diamonds", "8D")
                    self.createCard("Nine of Diamonds", "9D")
                    self.createCard("Ten of Diamonds", "10D")
                    self.createCard("Jack of Diamonds", "JD")
                    self.createCard("Queen of Diamonds", "QD")
                    self.createCard("King of Diamonds", "KD")

                    self.createCard("Ace of Spades", "AS")
                    self.createCard("Two of Spades", "2S")
                    self.createCard("Three of Spades", "3S")
                    self.createCard("Four of Spades", "4S")
                    self.createCard("Five of Spades", "5S")
                    self.createCard("Six of Spades", "6S")
                    self.createCard("Seven of Spades", "7S")
                    self.createCard("Eight of Spades", "8S")
                    self.createCard("Nine of Spades", "9S")
                    self.createCard("Ten of Spades", "10S")
                    self.createCard("Jack of Spades", "JS")
                    self.createCard("Queen of Spades", "QS")
                    self.createCard("King of Spades", "KS")
                    pass
                #Default Deck + Jokers
                case 1:
                    self.createCard("Ace of Hearts", "AH")
                    self.createCard("Two of Hearts", "2H")
                    self.createCard("Three of Hearts", "3H")
                    self.createCard("Four of Hearts", "4H")
                    self.createCard("Five of Hearts", "5H")
                    self.createCard("Six of Hearts", "6H")
                    self.createCard("Seven of Hearts", "7H")
                    self.createCard("Eight of Hearts", "8H")
                    self.createCard("Nine of Hearts", "9H")
                    self.createCard("Ten of Hearts", "10H")
                    self.createCard("Jack of Hearts", "JH")
                    self.createCard("Queen of Hearts", "QH")
                    self.createCard("King of Hearts", "KH")

                    self.createCard("Ace of Clubs", "AC")
                    self.createCard("Two of Clubs", "2C")
                    self.createCard("Three of Clubs", "3C")
                    self.createCard("Four of Clubs", "4C")
                    self.createCard("Five of Clubs", "5C")
                    self.createCard("Six of Clubs", "6C")
                    self.createCard("Seven of Clubs", "7C")
                    self.createCard("Eight of Clubs", "8C")
                    self.createCard("Nine of Clubs", "9C")
                    self.createCard("Ten of Clubs", "10C")
                    self.createCard("Jack of Clubs", "JC")
                    self.createCard("Queen of Clubs", "QC")
                    self.createCard("King of Clubs", "KC")

                    self.createCard("Ace of Diamonds", "AD")
                    self.createCard("Two of Diamonds", "2D")
                    self.createCard("Three of Diamonds", "3D")
                    self.createCard("Four of Diamonds", "4D")
                    self.createCard("Five of Diamonds", "5D")
                    self.createCard("Six of Diamonds", "6D")
                    self.createCard("Seven of Diamonds", "7D")
                    self.createCard("Eight of Diamonds", "8D")
                    self.createCard("Nine of Diamonds", "9D")
                    self.createCard("Ten of Diamonds", "10D")
                    self.createCard("Jack of Diamonds", "JD")
                    self.createCard("Queen of Diamonds", "QD")
                    self.createCard("King of Diamonds", "KD")

                    self.createCard("Ace of Spades", "AS")
                    self.createCard("Two of Spades", "2S")
                    self.createCard("Three of Spades", "3S")
                    self.createCard("Four of Spades", "4S")
                    self.createCard("Five of Spades", "5S")
                    self.createCard("Six of Spades", "6S")
                    self.createCard("Seven of Spades", "7S")
                    self.createCard("Eight of Spades", "8S")
                    self.createCard("Nine of Spades", "9S")
                    self.createCard("Ten of Spades", "10S")
                    self.createCard("Jack of Spades", "JS")
                    self.createCard("Queen of Spades", "QS")
                    self.createCard("King of Spades", "KS")

                    self.createCard("Red Joker", "JR")
                    self.createCard("Black Joker", "JB")
                    pass
        elif(type(cards) == list):
            self.cards = cards
    
    def cardDisplay(self):
        outputString = ""
        for card in self.cards:
            outputString = outputString + card.getAbrev() + " "
        outputString = outputString + "\nCount: " + str(len(self.cards))
        print(outputString)

    def shuffle(self):
        random.shuffle(self.cards)

    def empty(self):
        self.cards = []

    def createCard(self, name, abrev):
        self.cards.append(Card(name, abrev))

    def addCard(self, Card):
        self.cards.append(Card)

    def combineDeck(self, mergeDeck):
        for card in mergeDeck.cards:
            self.addCard(card)

    def drawCard(self):
        return self.cards.pop(0)

    def isEmpty(self):
        if(self.cards == []):
            return True
        else:
            return False

    def viewTopCard(self):
        return self.cards[0]
    
    def splitDeck(self, cardsInSplit):
        splitPartDeck = Deck(-1)
        for i in range(cardsInSplit):
            splitPartDeck.addCard(self.drawCard())
        return splitPartDeck
    def size(self):
        return len(self.cards)

    def getCards(self):
        return self.cards
        
    def getDisplayString(self):
        if(self.cards == []):
            return "[]"
        output = []
        for card in self.cards:
            output.append(card.getAbrev())
            output.append(" ")
        output.pop(-1)
        return ''.join(output)
    
    def removeCopyOfCards(self, cardAbrev):
        cardList = Deck(-1)
        for x in range(len(self.cards)):
            if(self.cards[x].getAbrev()[0:-1] == cardAbrev):
                cardList.addCard(self.cards[x])
        for card in cardList.getCards():
            self.removeCard(card.getAbrev()[0:-1])
        return cardList

    def removeCard(self, cardAbrev):
        for x in range(len(self.cards)):
            if(str(self.cards[x].getAbrev()[0:-1]) == str(cardAbrev)):
                self.cards.pop(x)
                break


class Card:
    def __init__(self, name, abrev):
        self.name = name
        self.abrev = abrev

    def getName(self):
        return self.name
    
    def getAbrev(self):
        return self.abrev
    
    def getValue(self):
        return self.getAbrev()[:-1]
    
    #Only works with default deck(0)
    def isHigherValue(self, compareCard):
        valueRanking = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
        thisCardRank = self.getValue()
        otherCardRank = compareCard.getValue()

        if(valueRanking.index(thisCardRank) > valueRanking.index(otherCardRank)):
            return True
        else:
            return False
    




