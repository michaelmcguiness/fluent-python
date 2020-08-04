"""Special Methods: Page 4"""

import collections
from random import choice

# construct a simple class to represent individual cards
# a namedtuple can be used to build classes of objects that are just bundles
# of attributes with no custom methods, like a database record
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits 
                                        for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]

beer_card = Card('7', 'diamonds')
print(beer_card) # Card(rank='7', suit='diamonds')

deck = FrenchDeck()
print(len(deck)) # 52

# __getitem__ method ("dunder-getitem") allows us to read specific cards from the deck
print(deck[0]) # Card(rank='2', suit='spades')
print(deck[-1]) # Card(rank='A', suit='hearts')

print(choice(deck)) # Card(rank='J', suit='spades')

# because our __getitem__ delegates to the [] operator of self._cards, 
# our deck automatically supports slicing
print(deck[:3]) # look at top three cards from a brand new deck
print(deck[12::13]) # pick just the aces by starting at index 12 and skipping 13 cards at a time

# deck is also iterable
for card in deck:
    print(card)

# deck can also be iterated in reverse
for card in reversed(deck):
    print(card)

# if collection has no __contains__ method, 'in' operator does a sequential scan
print(Card('Q', 'hearts') in deck) # True
print(Card('7', 'beasts') in deck) # False

# Sorting Cards
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)