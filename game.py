# initial set up
# setting up global variables
import random   # required for shuffling a deck of cards

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}


playing = True

class Card():
    '''
    Basic class card
    '''
    def __init__(self, suit, rank):
        '''
        initialize each card with suit and rank
        each card should be unique by definition
        '''
        self.suit = suit
        self.rank = rank


    def __str__(self):
        '''
        return description of a card
        '''
        return self.rank + " of " + self.suit

class Deck():
    '''
    this is where we store all 52 cards in some form of collection, list, et c.
    '''
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                pass

    def __str__(self):
        pass

    def shuffle(self):
        pass

    def deal(self):
        pass

