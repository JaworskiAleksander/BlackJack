'''
A simple, terminal-based implementation of Black Jack game
'''

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
        pop one card off a shuffled deck of cards,
        remove it from the stack and return a pointer to it
        '''
        single_card = self.deck.pop()
        return single_card

class Hand():
    '''
    A hand - set of cards that belong to a player
    '''
    def __init__(self):
        '''
        each player start with no cards, no value and no aces
        '''
        self.cards = [] # start with an empty list
        self.value = 0  # start with zero value
        self.aces = 0   # add an attribute to account for an ace in stack

    def add_card(self, card):
        '''
        card passed in from an instance of Deck class with method deal(())
        '''
        self.cards.append(card)
        self.value += values[card.rank]
        # tracking for aces
        if card.rank.count('Ace') != 0:
            self.aces += 1


    def adjust_for_ace(self):
        '''
        when a player has drawn an ace from a deck and total value goes over 21
        changes ave to be 1 instead of 11
        '''
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips():
    '''
    making bets!
    '''
    def __init__(self, total=1000):
        '''
        outcome of games
        '''
        self.total = total
        self.bet = 0

    def win(self):
        '''
        add money once you win a game
        '''
        self.total += self.bet


    def lose_bet(self):
        '''
        substract money when you lose a game
        '''
        self.total -= self.bet


def take_bet(chips):
    '''
    asks user to take a bet and set the actual bet value
    '''
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
            
        except:
            print('Sorry, please provide an integer')
        else:
            if chips.bet > chips.total:
                print('Sorry, you don\'t have enough chips! you have [{}]:'.format(chips.data))
            else:
                break


#-------------------
# Test code
#-------------------
if __name__ == '__main__':
    
    test_deck = Deck()
    test_deck.shuffle()

    # Player
    test_player = Hand()
    pulled_card = test_deck.deal()
    print(pulled_card)
    test_player.add_card(pulled_card)
    print(test_player.value)
