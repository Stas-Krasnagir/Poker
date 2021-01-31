import random
from enum import Enum


class Rank(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    T = 10
    J = 11
    Q = 12
    K = 13
    A = 14


class Suit(Enum):
    Diamonds = "d"
    Clubs = "c"
    Hearts = "h"
    Spades = "s"


class Card(object):
    def __init__(self, value: Rank, suit: Suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        value_name = ""
        suit_name = ""
        if self.value == 2:
            value_name = "Two"
        elif self.value == 3:
            value_name = "Three"
        elif self.value == 4:
            value_name = "Four"
        elif self.value == 5:
            value_name = "Five"
        elif self.value == 6:
            value_name = "Six"
        elif self.value == 7:
            value_name = "Seven"
        elif self.value == 8:
            value_name = "Eight"
        elif self.value == 9:
            value_name = "Nine"
        elif self.value == 10:
            value_name = "Ten"
        elif self.value == 11:
            value_name = "Jack"
        elif self.value == 12:
            value_name = "Queen"
        elif self.value == 13:
            value_name = "King"
        elif self.value == 14:
            value_name = "Ace"
        if self.suit == "d":
            suit_name = "Diamonds"
        elif self.suit == "c":
            suit_name = "Clubs"
        elif self.suit == "h":
            suit_name = "Hearts"
        elif self.suit == "s":
            suit_name = "Spades"
        return value_name + " of " + suit_name


class StandardDeck(object):
    def __init__(self):
        self.cards = []
        suits = ["h", "s", "d", "c"]
        values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

        for name in values:
            for suit in suits:
                self.cards.append(Card(name, suit))

    def shuffle(self):
        random.shuffle(self.cards)
        print("---Deck Shuffled---")

    def deal(self, location):
        if len(self.cards) == 0:
            return None
        else:
            return location.cards.append(self.cards.pop(0))


deck = StandardDeck()
