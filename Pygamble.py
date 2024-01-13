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
        self.end = False
        self.winner = ""

        deck = Pycards.Deck(0)
        deck.shuffle()
        self.enemyDeck = deck.splitDeck(26)
        self.playerDeck = deck

        self.enemyBoard = []
        self.playerBoard = []

        self.enemyDiscard = []
        self.playerDiscard = []

    def showState(self):
        playerBoardString = "Player board: "
        if(self.playerBoard == []):
            playerBoardString = playerBoardString + "[empty] "
        else:
            for card in self.playerBoard:
                playerBoardString = playerBoardString + card.getAbrev() + " "
        playerBoardString = playerBoardString + "Remaining deck: " + str(self.playerDeck.size()) + " Discard pile: " + str(len(self.playerDiscard))
        print(playerBoardString)

        enemyBoardString = "Enemy board: "
        if(self.enemyBoard == []):
            enemyBoardString = enemyBoardString + "[empty] "
        else:
            for card in self.enemyBoard:
                enemyBoardString = enemyBoardString + card.getAbrev() + " "
        enemyBoardString = enemyBoardString + "Remaining deck: " + str(self.enemyDeck.size()) + " Discard pile: " + str(len(self.enemyDiscard))
        print(enemyBoardString)

        if(self.winner == "player"):
            print("Player win!")
            self.playerBoard = []
            self.enemyBoard = []
        elif(self.winner == "enemy"):
            print("Enemy win!")
            self.playerBoard = []
            self.enemyBoard = []
        elif(self.winner == "war"):
            print("War! (+2 cards both sides)")
        elif(self.winner == "draw"):
            print("Draw!")

    def playerTurn(self, input):
        match input:
            case "q":
                self.isEnd = True
            case "p":
                if((self.playerDeck.size() == 0) and (self.enemyDeck.size() == 0)):
                    self.winner = "draw"
                    for card in self.playerDiscard:
                        self.playerDeck.addCard(card)
                    self.playerDiscard = []
                    for card in self.enemyDiscard:
                        self.enemyDeck.addCard(card)
                    self.enemyDiscard = []
                elif(self.playerDeck.size() == 0):
                    self.winner = "enemy"
                    for card in self.playerDiscard:
                        self.playerDeck.addCard(card)
                    self.playerDiscard = []
                elif(self.enemyDeck.size() == 0):
                    self.winner = "player"
                    for card in self.enemyDiscard:
                        self.enemyDeck.addCard(card)
                    self.enemyDiscard = []
                else:
                    playerCard = self.playerDeck.drawCard()
                    self.playerBoard.append(playerCard)

                    enemyCard = self.enemyDeck.drawCard()
                    self.enemyBoard.append(enemyCard)

                    if(playerCard.isHigherValue(enemyCard)):
                        self.playerDiscard.extend(self.playerBoard)
                        self.playerDiscard.extend(self.enemyBoard)
                        self.winner = "player"
                    elif(enemyCard.isHigherValue(playerCard)):
                        self.enemyDiscard.extend(self.playerBoard)
                        self.enemyDiscard.extend(self.enemyBoard)
                        self.winner = "enemy"
                    else:
                        if((self.playerDeck.size() < 2) and (self.enemyDeck.size() < 2)):
                            self.winner = "draw"
                        elif(self.playerDeck.size() < 2):
                            self.winner = "enemy"
                        elif(self.enemyDeck.size() < 2):
                            self.winner = "player"
                        else:
                            self.playerBoard.append(self.playerDeck.drawCard())
                            self.playerBoard.append(self.playerDeck.drawCard())
                                
                            self.enemyBoard.append(self.enemyDeck.drawCard())
                            self.enemyBoard.append(self.enemyDeck.drawCard())

                            self.winner = "war"
                self.showState()

    def isEnd(self):
        return self.end