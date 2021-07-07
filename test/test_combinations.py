import unittest
from Cards import *
from combinations import *


class TestTree(unittest.TestCase):

    def test_pairs(self):
        table_cards = [Card(12, "S"), Card(6, "S"), Card(4, "D"), Card(5, "H"), Card(5, "D")]
        player_hand = [Card(7, "C"), Card(13, "C")]

        seven_cards = CardCombinations(table_cards, player_hand)
        message = "test_pairs is FAIL"
        self.assertTrue(seven_cards.pairs(), message)

    def test_three_kind(self):
        table_cards = [Card(2, "S"), Card(6, "S"), Card(4, "D"), Card(6, "H"), Card(7, "D")]
        player_hand = [Card(8, "C"), Card(6, "C")]

        seven_cards = CardCombinations(table_cards, player_hand)
        message = "test_three_kind is FAIL"
        self.assertTrue(seven_cards.three_kind(), message)

    def test_straight(self):
        table_cards = [Card(2, "S"), Card(3, "S"), Card(4, "D"), Card(5, "H"), Card(11, "D")]
        player_hand = [Card(14, "C"), Card(6, "C")]

        seven_cards = CardCombinations(table_cards, player_hand)
        message = "test_straight is FAIL"
        self.assertTrue(seven_cards.straight(), message)

    def test_flush(self):
        table_cards = [Card(2, "C"), Card(3, "S"), Card(4, "C"), Card(5, "H"), Card(11, "C")]
        player_hand = [Card(14, "C"), Card(6, "C")]

        seven_cards = CardCombinations(table_cards, player_hand)
        message = "test_straight is FAIL"
        self.assertTrue(seven_cards.flush(), message)

    def test_full_house(self):
        table_cards = [Card(13, "D"), Card(13, "S"), Card(4, "C"), Card(5, "H"), Card(7, "C")]
        player_hand = [Card(13, "C"), Card(7, "D")]

        seven_cards = CardCombinations(table_cards, player_hand)
        message = "test_full_house is FAIL"
        self.assertTrue(seven_cards.full_house(), message)

    def test_four_kind(self):
        table_cards = [Card(6, "D"), Card(6, "S"), Card(6, "C"), Card(5, "H"), Card(7, "C")]
        player_hand = [Card(6, "H"), Card(13, "D")]

        seven_cards = CardCombinations(table_cards, player_hand)
        message = "test_four_kind is FAIL"
        self.assertTrue(seven_cards.four_kind(), message)

    def test_straight_flush(self):
        table_cards = [Card(2, "D"), Card(3, "D"), Card(4, "D"), Card(5, "D"), Card(9, "H")]
        player_hand = [Card(6, "D"), Card(13, "S")]

        seven_cards = CardCombinations(table_cards, player_hand)
        message = "test_straight_flush is FAIL"
        self.assertTrue(seven_cards.straight_flush(), message)

    def test_royal_flush(self):
        table_cards = [Card(10, "D"), Card(11, "D"), Card(12, "D"), Card(13, "D"), Card(3, "H")]
        player_hand = [Card(14, "D"), Card(5, "S")]

        seven_cards = CardCombinations(table_cards, player_hand)
        message = "test_royal_flush is FAIL"
        self.assertTrue(seven_cards.royal_flush(), message)

    def test_high_card(self):
        table_cards = [Card(10, "C"), Card(4, "H"), Card(7, "S"), Card(14, "C"), Card(3, "H")]
        player_hand = [Card(2, "D"), Card(5, "S")]

        seven_cards = CardCombinations(table_cards, player_hand)
        message = "test_high_card is FAIL"
        res = Card(14, "C")
        self.assertTrue(seven_cards.high_card(), message)
        self.assertNotEqual(seven_cards.high_card(), res, message)

    def test_check(self):
        table_cards = [Card(10, "C"), Card(4, "H"), Card(7, "S"), Card(14, "C"), Card(3, "H")]
        player_hand = [Card(2, "D"), Card(5, "S")]

        seven_cards = CardCombinations(table_cards, player_hand)
        message = "test_check is FAIL"
        res = Card(14, "C")
        self.assertNotEqual(seven_cards.cheсk(), res, message)


if __name__ == "__main__":
    unittest.main()
