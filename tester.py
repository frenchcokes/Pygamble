import Pygamble

if __name__ == "__main__":
    inputString = ""
    state = 0
    while (inputString != "Q"):
        inputString = input("Please enter: ")
        match inputString:
            #Blackjack
            case "1":
                blackjack = Pygamble.Blackjack()
                print(blackjack.showState())
                break