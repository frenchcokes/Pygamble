import Pycards

class Blackjack:
    def __init__(self):
        self.end = False

        deck = Pycards.Deck(0)
        self.deck = deck
        deck.shuffle()

        self.dealersHand = []
        self.playersHand = []

        self.drawAndAddValueToDealerHand()
        dealerSecondCard = deck.drawCard().getValue()
        self.dealerSecondCard = dealerSecondCard
        self.dealersHand.append("*")
        
        self.drawAndAddValuetoPlayerHand()
        self.drawAndAddValuetoPlayerHand()

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
            playerHandValue = self.getHandValue(self.playersHand)
            dealerHandValue = self.getHandValue(self.dealersHand)
            if(playerHandValue > 21):
                outputString = outputString + "\nDealer wins!"
            elif(dealerHandValue > 21):
                outputString = outputString + "\nPlayer wins!"
            elif(playerHandValue > dealerHandValue):
                outputString = outputString + "\nPlayer wins!"
            elif(playerHandValue < dealerHandValue):
                outputString = outputString + "\nDealer wins!"
            elif(playerHandValue == dealerHandValue):
                outputString = outputString + "\nDraw!"
        print(outputString)

    def playerTurn(self, action):
        if(action == "h"):
            self.drawAndAddValuetoPlayerHand()
            if(self.getHandValue(self.playersHand) > 21):
                self.revealDealerHiddenCard()
                self.end = True
        elif(action == "s"):
            self.revealDealerHiddenCard()
            if (self.getHandValue(self.dealersHand) >= 17):
                self.end = True
            else:
                while(self.getHandValue(self.dealersHand) < 17):
                    self.drawAndAddValueToDealerHand()
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
                    case "J" | "Q" | "K":
                        handValue = handValue + 10
                    case "A":
                        if(handValue + 11 <= 21):
                            handValue = handValue + 11
                        else:
                            handValue = handValue + 1
        return handValue
    
    def drawAndAddValueToDealerHand(self):
        self.dealersHand.append(self.deck.drawCard().getValue())
    
    def drawAndAddValuetoPlayerHand(self):
        self.playersHand.append(self.deck.drawCard().getValue())

    def revealDealerHiddenCard(self):
        self.dealersHand.remove("*")
        self.dealersHand.append(self.dealerSecondCard)

class War:
    def __init__(self):
        deck = Pycards.Deck(1)
        deck.shuffle()
        self.enemyDeck = deck.splitDeck(27)
        self.playerDeck = deck
    def showState(self):
        self.enemyDeck.cardDisplay()
        self.playerDeck.cardDisplay()