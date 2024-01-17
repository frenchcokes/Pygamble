import Pygamble

if __name__ == "__main__":
    inputString = ""
    state = 0
    while (inputString != "q"):
        inputString = input("Please select game (q = quit, 1 = blackjack, 2 = war, 3 = go fish): ")
        match inputString:
            #Blackjack
            case "1":
                blackjack = Pygamble.Blackjack()
                blackjack.showState()
                while(blackjack.isEnd() == False):
                    gameInput = input("What would you like to do? (Hit = h, Stay = s): ")
                    blackjack.playerTurn(gameInput)
                    blackjack.showState()

            #War
            case "2":
                war = Pygamble.War()
                war.showState()
                while(war.isEnd() == False):
                    gameInput = input("Type to proceed (Proceed = p, Quit = q): ")
                    war.playerTurn(gameInput)
                    war.showState()

            #Go Fish
            case "3":
                goFish = Pygamble.GoFish()
                goFish.showState()
                while(goFish.isEnd() == False):
                    gameInput = input("What would you like to fish?")
                    goFish.playerTurn(gameInput)
                    goFish.showState()
                pass
