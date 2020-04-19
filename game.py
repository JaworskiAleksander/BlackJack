# initial set up
# setting up global variables
import random   # required for shuffling a deck of cards

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 
        'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 
        'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


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
        '''
        initialize a deck with 52 cards
        this happens every time an instance of Deck class is being created
        '''
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        '''
        return string representation of a deck
        '''
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp

    def shuffle(self):
        '''
        shuffle, 'nuff said
        '''
        random.shuffle(self.deck)   # this happens in place, so there's no need to return anything

    def deal(self):
        '''
        pop one card off a shuffled deck of cards, remove it from the stack and return a pointer to it
        '''
        single_card = self.deck.pop()
        return single_card

class Hand():
    def __init__(self):
        self.cards = [] # start with an empty list
        self.value = 0  # start with zero value
        self.aces = 0   # add an attribute to account for an ace in stack

    def add_card(self):
        pass

    def adjust_for_ace(self):
        pass