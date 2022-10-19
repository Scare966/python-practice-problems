## making a deck of cards, including a shuffle feature

import random
from random import shuffle

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
values = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def show(self):
        print ("{} of {}".format(self.value, self.suit))

card = Card("Card", 6)
card.show()

class Deck:
    def __init__(self):
        self.cards = []
        self.pile()
    
    def pile(self):
        for i in suits:
            for s in values:
                self.cards.append(Card(i, s))

    def show(self):
        for a in self.cards:
            a.show()

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

deck = Deck()
deck.shuffle()
deck.show()   
