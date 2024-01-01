import random

class Deck:
    def __init__(self, cards):
        self.cards = cards
        if(cards == []):
            pass
        
    def shuffle(self):
        random.shuffle(self.cards)

class Card:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name