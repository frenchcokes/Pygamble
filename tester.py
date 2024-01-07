import Pygamble

if __name__ == "__main__":
    inputString = ""
    state = 0
    while (inputString != "q"):
        inputString = input("Please select game (q = quit, 1 = blackjack): ")
        match inputString:
            #Blackjack
            case "1":
                blackjack = Pygamble.Blackjack()
                blackjack.showState()
                while(blackjack.isEnd() == False):
                    gameInput = input("What would you like to do? (Hit = h, Stay = s): ")
                    blackjack.playerTurn(gameInput)
                    blackjack.showState()
            #Roulette
            case "2":
                pass