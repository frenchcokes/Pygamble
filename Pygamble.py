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

        self.enemyBoard = Pycards.Deck(-1)
        self.playerBoard = Pycards.Deck(-1)

        self.enemyDiscard = Pycards.Deck(-1)
        self.playerDiscard = Pycards.Deck(-1)

    def showState(self):
        playerBoardString = "Player board: "
        if(self.playerBoard.isEmpty() == True):
            playerBoardString = playerBoardString + "[empty] "
        else:
            for card in self.playerBoard.getCards():
                playerBoardString = playerBoardString + card.getAbrev() + " "
        playerBoardString = playerBoardString + "Remaining deck: " + str(self.playerDeck.size()) + " Discard pile: " + str(self.playerDiscard.size())
        print(playerBoardString)

        enemyBoardString = "Enemy board: "
        if(self.enemyBoard.isEmpty() == True):
            enemyBoardString = enemyBoardString + "[empty] "
        else:
            for card in self.enemyBoard.getCards():
                enemyBoardString = enemyBoardString + card.getAbrev() + " "
        enemyBoardString = enemyBoardString + "Remaining deck: " + str(self.enemyDeck.size()) + " Discard pile: " + str(self.enemyDiscard.size())
        print(enemyBoardString)

        match(self.winner):
            case "player":
                print("Player win!")
                self.playerBoard.empty()
                self.enemyBoard.empty()
            case "enemy":
                print("Enemy win!")
                self.playerBoard.empty()
                self.enemyBoard.empty()
            case "war":
                print("War! (+2 cards both sides)")
            case "drawooc":
                print("Draw! (Both players ran out of cards)")
            case "enemyooc":
                print("Enemy win! (Player ran out of cards)")
            case "playerooc":
                print("Player win! (Enemy ran out of cards)")
            case "playerWin":
                print("Player has won the war! Game Over.")
                self.isEnd = True
            case "enemyWin":
                print("Enemy has won the war! Game Over")
                self.isEnd = True
        
    def playerTurn(self, input):
        match input:
            case "q":
                self.isEnd = True
            case "p":
                if((self.playerDeck.isEmpty() == True) and (self.enemyDeck.isEmpty() == True)):
                    self.winner = "drawooc"
                    for card in self.playerDiscard.getCards():
                        self.playerDeck.addCard(card)
                    self.playerDiscard.empty()
                    for card in self.enemyDiscard.getCards():
                        self.enemyDeck.addCard(card)
                    self.enemyDiscard.empty()
                elif(self.playerDeck.isEmpty() == True):
                    self.winner = "enemy"
                    for card in self.playerDiscard.getCards():
                        self.playerDeck.addCard(card)
                    self.playerDiscard.empty()
                elif(self.enemyDeck.isEmpty() == True):
                    self.winner = "player"
                    for card in self.enemyDiscard.getCards():
                        self.enemyDeck.addCard(card)
                    self.enemyDiscard.empty()
                else:
                    playerCard = self.playerDeck.drawCard()
                    self.playerBoard.addCard(playerCard)

                    enemyCard = self.enemyDeck.drawCard()
                    self.enemyBoard.addCard(enemyCard)

                    if(playerCard.isHigherValue(enemyCard)):
                        self.playerDiscard.combineDeck(self.playerBoard)
                        self.playerDiscard.combineDeck(self.enemyBoard)
                        self.winner = "player"
                    elif(enemyCard.isHigherValue(playerCard)):
                        self.enemyDiscard.combineDeck(self.playerBoard)
                        self.enemyDiscard.combineDeck(self.enemyBoard)
                        self.winner = "enemy"
                    else:
                        if((self.playerDeck.size() < 2) and (self.enemyDeck.size() < 2)):
                            for card in self.playerDiscard.getCards():
                                self.playerDeck.addCard(card)
                                self.playerDiscard.empty()
                            self.winner = "drawooc"
                        elif(self.playerDeck.size() < 2):
                            for card in self.playerDiscard.getCards():
                                self.playerDeck.addCard(card)
                                self.playerDiscard.empty()
                            self.winner = "enemyooc"
                        elif(self.enemyDeck.size() < 2):
                            for card in self.enemyDiscard.getCards():
                                self.enemyDeck.addCard(card)
                                self.enemyDiscard.empty()
                            self.winner = "playerooc"
                        else:
                            self.playerBoard.addCard(self.playerDeck.drawCard())
                            self.playerBoard.addCard(self.playerDeck.drawCard())
                                
                            self.enemyBoard.addCard(self.enemyDeck.drawCard())
                            self.enemyBoard.addCard(self.enemyDeck.drawCard())

                            self.winner = "war"
                    if(self.playerBoard.isEmpty() and self.playerDiscard.isEmpty()):
                        self.winner = "enemyWin"
                    elif(self.enemyBoard.isEmpty() and self.playerDiscard.isEmpty()):
                        self.winner = "playerWin"
                
    def isEnd(self):
        return self.end
    
class GoFish:
        def __init__(self):
            self.playerHand = Pycards.Deck(-1)
            self.enemyHand = Pycards.Deck(-1)

            self.playerBooks = 0
            self.enemyBooks = 0

            self.deck = Pycards.Deck(0)
            self.dealStartingCards()
        def showState(self):
            print("Enemy has: " + str(self.enemyHand.size()) + " cards in hand.")
            print("Enemy has: " + str(self.enemyBooks) + " books")
            print("The deck has: " + str(self.deck.size()) + " cards")
            print("Player has: " + str(self.playerBooks) + " books")
            print("Player has: " + self.playerHand.getDisplayString() + " (" + str(self.playerHand.size()) + " total)")

        def isEnd(self):
            pass

        def playerTurn(self):
            pass

        def dealStartingCards(self):
            for _ in range(7):
                self.playerHand.addCard(self.deck.drawCard())
                self.enemyHand.addCard(self.deck.drawCard())