import Pycards

class Blackjack:
    def __init__(self):
        deck = Pycards.Deck(0)
        self.deck = deck
        deck.shuffle()

        self.dealersHand = []
        self.playersHand = []

        self.dealersHand.append(deck.drawCard().getValue())
        dealerSecondCard = deck.drawCard().getValue()
        if (self.dealersHand == ("J" or "Q" or "K") and dealerSecondCard == "A"):
            self.dealersHand.append(dealerSecondCard)
        elif (self.dealersHand == ("A") and dealerSecondCard == ("J" or "Q" or "K")):
            self.dealersHand.append(dealerSecondCard)
        else:
            self.dealersHand.append("*")
        
        self.playersHand.append(deck.drawCard().getValue())
        self.playersHand.append(deck.drawCard().getValue())
    def showState(self):
        dealerHandOutput = ""
        for cardText in self.dealersHand:
            dealerHandOutput = dealerHandOutput + cardText + " "
        playersHandOutput = ""
        for cardText in self.playersHand:
            playersHandOutput = playersHandOutput + cardText + " "
        outputString = "Dealer: " + dealerHandOutput + "\n" + "Player: " + playersHandOutput
        return(outputString)