import unittest
from Cards import *
from players import *


class TestTree(unittest.TestCase):
    def test_card(self):
        self.card_1 = Card(14, "C")
        self.card_2 = Card(10, "H")
        message = "test_card is FAIL"
        self.assertNotEqual(self.card_1, self.card_2, message)

    def test_deck(self):
        self.res = 52
        message = "test_deck is FAIL"
        self.assertEqual(len(deck.cards), self.res, message)

    def test_shuffle(self):
        self.deck_1 = StandardDeck
        deck.shuffle()
        message = "test_shuffle is FAIL"
        self.assertNotEqual(self.deck_1, deck, message)

    def test_deal(self):
        self.table_cards = Deck()
        deck.deal(self.table_cards)

        self.table_cards_1 = Deck()
        deck.deal(self.table_cards_1)

        self.res = 50

        message = "test_deal is FAIL"
        self.assertEqual(len(deck.cards), self.res, message)
        self.assertNotEqual(self.table_cards.cards, self.table_cards_1.cards, message)


if __name__ == "__main__":
    unittest.main()
