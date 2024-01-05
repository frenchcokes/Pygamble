import Pycards

class Blackjack:
    def __init__(self):
        self.end = False

        deck = Pycards.Deck(0)
        self.deck = deck
        deck.shuffle()

        self.dealersHand = []
        self.playersHand = []

        self.dealersHand.append(deck.drawCard().getValue())
        dealerSecondCard = deck.drawCard().getValue()
        self.dealersSecondCard = dealerSecondCard
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
        outputString = "Dealer: " + dealerHandOutput + " (" + str(self.getHandValue(self.dealersHand))
        if(self.end == False):
            outputString = outputString + " + ?)"
        else:
            outputString = outputString + ")"
        outputString = outputString + "\nPlayer: " + playersHandOutput + " (" + str(self.getHandValue(self.playersHand)) + ")"
        if(self.end == True):
            if(self.getHandValue(self.playersHand) > 21):
                outputString = outputString + "\nDealer wins!"
            elif(self.getHandValue(self.dealersHand) > 21):
                outputString = outputString + "\nPlayer wins!"
            elif(self.getHandValue(self.playersHand) > self.getHandValue(self.dealersHand)):
                outputString = outputString + "\nPlayer wins!"
            elif(self.getHandValue(self.playersHand) < self.getHandValue(self.dealersHand)):
                outputString = outputString + "\nDealer wins!"
            elif(self.getHandValue(self.playersHand) == self.getHandValue(self.dealersHand)):
                outputString = outputString + "\nDraw!"
        return(outputString)
    def playerTurn(self, action):
        if(action == "h"):
            self.playersHand.append(self.deck.drawCard().getValue())
            if(self.getHandValue(self.playersHand) > 21):
                self.end = True
        elif(action == "s"):
            self.dealersHand.remove("*")
            self.dealersHand.append(self.dealersSecondCard)
            if (self.getHandValue(self.dealersHand) >= 17):
                self.end = True
            else:
                while(self.getHandValue(self.dealersHand) < 17):
                    self.dealersHand.append(self.deck.drawCard().getValue())
                self.end = True
        else:
            pass
    def isEnd(self):
        return self.end
    def getHandValue(self, hand):
        handValue = 0
        for symbol in hand:
            if(symbol.isnumeric() == True):
                handValue = handValue + int(symbol)
            else:
                match(symbol):
                    case "J":
                        handValue = handValue + 10
                    case "Q":
                        handValue = handValue + 10
                    case "K":
                        handValue = handValue + 10
                    case "A":
                        if(handValue + 11 <= 21):
                            handValue = handValue + 11
                        else:
                            handValue = handValue + 1
        return handValue