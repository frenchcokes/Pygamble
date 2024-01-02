import Pycards

class Blackjack:
    def __init__(self):
        deck = Pycards.Deck(0)
        self.deck = deck
        deck.shuffle()

        self.dealersHand = []
        self.playersHand = []

        self.dealersHand.append(deck.drawCard())
        self.playersHand.append(deck.drawCard())
        
    def showState(self):
        dealerHandOutput = ""
        for card in self.dealersHand:
            dealerHandOutput = dealerHandOutput + card.getAbrev() + " "
        playersHandOutput = ""
        for card in self.playersHand:
            playersHandOutput = playersHandOutput + card.getAbrev() + " "
        outputString = "Dealer: " + dealerHandOutput + "\n" + "Player: " + playersHandOutput
        return(outputString)