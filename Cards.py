import random


class Card(object):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return str(self.value) + self.suit


class StandardDeck(object):
    def __init__(self):
        self.cards = []
        suits = ["H", "S", "D", "C"]
        values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10,
                  "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}

        for name in values:
            for suit in suits:
                self.cards.append(Card(values[name], suit))

    def shuffle(self):
        random.shuffle(self.cards)
        print("Deck Shuffled")

    def deal(self):
        return self.cards.pop(0)


card_deck = StandardDeck()
print(card_deck.cards)
card_deck.shuffle()
