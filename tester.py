import Pygamble

if __name__ == "__main__":
    inputString = ""
    state = 0
    while (inputString != "Q"):
        inputString = input("Please select game: ")
        match inputString:
            #Blackjack
            case "1":
                blackjack = Pygamble.Blackjack()
                print(blackjack.showState())
                while(blackjack.isEnd() == False):
                    gameInput = input("What would you like to do? (Hit = h, Stay = s) ")

                break