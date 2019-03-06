# 06/03/2019  11:12 AM

# Some extra info can be found in PythonTutorialAndTips2.py look for *#*

# 1.) __func__ are called magic methods(slang) or special methods or dunder
# The dunders are called by the interpreter and not by us
# We don’t write my_object.__len__(). We write
# len(my_object) and, if my_object is an instance of a user defined class, then Python
# calls the __len__ instance method you implemented.

# 2.) Playing with Dunders
# A class with a deck of playing cards

import collections

Cards = collections.namedtuple('Cards',['rank', 'suit'])  # (*#*) (can be used to create obj
# without function...like a database)

class Deck(): # the class is immutable ofcourse (can't shuffle)
  ranks = [str(i) for i in range(2,11)] + list('JQKA')
  suits = "spades diamonds clubs hearts".split()

  def __init__(self):
    # Creates a deck of 52 cards or 52 Cards object
    # [Cards(rank='2', suite='spades'), Cards(rank='3', suite='spades') ...... ]
    self._cards = [Cards(rank, suit) for suit in self.suits for rank in self.ranks ]

  def __len__(self):
    # Now we can use len(obj) just like any iterable (list[1])
    return len(self._cards)

  def __getitem__(self, item):
    # Can use indexing and run loops on
    return self._cards[item]



d = Deck()
print('The Object {}'.format(d))
print('Length -> {} '.format(len(d)))
print('Index  d[23] -> {}'.format(d[23]))
print([i for i in d if i.suit == 'spades']) # Even Iterable and reversed iterable
print('only Ace \n {}'.format(d[9::13]))
print(Cards('Q', 'hearts') in d)


# Picking random
from random import choice  # choice accepts any iterable / choice('naruto')
print('Picking up random card -> {}'.format(choice(d)))

# Sorting
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
  rank_value = Deck.ranks.index(card.rank)
  return rank_value * len(suit_values) + suit_values[card.suit]

print('************SORTED*****************')
print((sorted(d , key= spades_high)))
print('************SORTED END*****************')
# print(spades_high(Cards('Q', 'hearts')))

# two advantages of using special methods to leverage the Python Data Model:
# 1. The users of your classes don’t have to memorize arbitrary method names for standard
# operations (“How to get the number of items? Is it .size() .length() or what?”)
# 2. It’s easier to benefit from the rich Python standard library and avoid reinventing
# the wheel, like the random.choice function.
# 3. Supports slicing and iteration
# 4. supporsts in and not in and also sorting

class Deck_without_dunder():
  ranks = [str(i) for i in range(2,11)] + list('AJQK')
  suits = "spades diamond clubs hearts".split()

  def __init__(self):
    # Creates a deck of 52 cards or 52 Cards object
    # [Cards(rank='2', suite='spades'), Cards(rank='3', suite='spades') ...... ]
    self._cards = [Cards(rank, suit) for suit in self.suits for rank in self.ranks ]

d1 = Deck_without_dunder()
# print(len(d1))  # TypeError: object of type 'Deck_without_dunder' has no len()
# print(d1[0]) TypeError: 'Deck_without_dunder' object does not support indexing