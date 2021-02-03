from Cards import Card


class CardCombinations:
    def __init__(self, cards: list[Card], player_cards: list[Card]) -> None:
        self.cards = cards + player_cards

    def cheak_suits(self) -> list:
        suits = [card.suit for card in self.cards]
        return suits

    def cheak_values(self) -> list:
        values = [card.value for card in self.cards]
        return values

    def cheсk(self) -> int:
        print_chek = False
        if self.royal_flush():
            if print_chek:
                print("Royal flush")
            return 1000
        elif self.straight_flush():
            if print_chek:
                print("Straight flush")
            return 900
        elif self.four_kind():
            if print_chek:
                print("Four kind")
            return 800
        elif self.full_house():
            if print_chek:
                print("Full house")
            return 700
        elif self.flush():
            if print_chek:
                print(self.flush())
            return 600
        elif self.straight():
            if print_chek:
                print(self.straight())
            return 500
        elif self.three_kind():
            if print_chek:
                print(self.three_kind())
            return 400
        elif self.two_pairs():
            res = self.two_pairs()
            if print_chek:
                print(f"Pairs of {res[0]} and {res[1]}")
            return 300 + res[0] + res[1] + 20
        elif self.pairs():
            res = self.pairs()
            if res:
                if print_chek:
                    print(f"Pair of {res}")
                return 200 + res + 10
        else:
            if print_chek:
                print(f"High card: {self.high_card()}")
            return 100

    def pairs(self) -> bool or list:  # Two cards with the same value
        pairs = []
        values = self.cheak_values()
        for value in values:
            if values.count(value) >= 2 and value not in pairs:
                pairs.append(value)
        if len(pairs) == 1:
            return pairs[0]
        return False

    def two_pairs(self) -> bool or list:  # Two times two cards with the same value
        pairs = []
        values = self.cheak_values()
        for value in values:
            if values.count(value) >= 2 and value not in pairs:
                pairs.append(value)
        if len(pairs) == 2:
            return pairs
        return False

    def royal_flush(self) -> bool:  # Straight flush from Ten to Ace
        one_suit = False
        sequence = False
        if self.flush():
            one_suit = True
        if self.straight():
            values = self.cheak_values()
            values.sort()
            if values[6] == 14:
                sequence = True
            else:
                sequence = False
        if one_suit and sequence:
            return True
        return False

    def straight_flush(self) -> bool:  # Straight of the same suit
        one_suits = False
        five_in_line = False
        if self.straight():
            five_in_line = True
        if self.flush():
            one_suits = True

        if one_suits and five_in_line:
            return True
        return False

    def four_kind(self) -> bool:  # Four cards of the same value
        values = self.cheak_values()
        for value in values:
            if values.count(value) == 4:
                return True

    def full_house(self) -> bool:  # Combination of three of a kind and a pair
        two = False
        three = False

        values = self.cheak_values()
        for value in values:
            if values.count(value) == 2:
                two = True
            elif values.count(value) == 3:
                three = True

        if two and three:
            return True

        return False

    def flush(self) -> bool:  # 5 cards of the same suit
        suits = self.cheak_suits()
        suits.sort()
        if len(set(suits)) == 4:
            return False

        if suits[0] == suits[1] and \
                suits[0] == suits[2] and \
                suits[0] == suits[3] and \
                suits[0] == suits[4]:
            return f"Flush of {suits[0]}"

        elif suits[1] == suits[2] and \
                suits[1] == suits[3] and \
                suits[1] == suits[4] and \
                suits[1] == suits[5]:
            return f"Flush of {suits[1]}"

        elif suits[2] == suits[3] and \
                suits[2] == suits[4] and \
                suits[2] == suits[5] and \
                suits[2] == suits[6]:
            return f"Flush of {suits[2]}"
        else:
            return False

    def straight(self) -> bool:  # Sequence of 5 cards in increasing value
        values = self.cheak_values()
        values.sort()
        if len(set(values)) < 5:
            return False

        # example 1.  [1, 3, 6-10]
        elif values[3] == values[2] + 1 and \
                values[4] == values[3] + 1 and \
                values[5] == values[4] + 1 and \
                values[6] == values[5] + 1:
            return f"Straight from {values[2]} to {values[6]}"

        # example 2. [1-5, 9, 14]
        elif values[1] == values[0] + 1 and \
                values[2] == values[1] + 1 and \
                values[3] == values[2] + 1 and \
                values[4] == values[3] + 1:
            return f"Straight from {values[0]} to {values[4]}"

        # example 3. [1, 3-7, 13]
        elif values[2] == values[1] + 1 and \
                values[3] == values[2] + 1 and \
                values[4] == values[3] + 1 and \
                values[5] == values[4] + 1:
            return f"Straight from {values[1]} to {values[5]}"

        else:
            return False

    def three_kind(self) -> bool:  # Three cards with the same value
        values = self.cheak_values()
        res = []
        for value in values:
            if values.count(value) == 3 and value not in res:
                res.append(value)
        if res:
            return f"Three a kind of {res[0]}"
        return False

    def high_card(self) -> Card:  # Simple value of the card
        high_card = None
        for card in self.cards:
            if high_card is None:
                high_card = card
            if high_card.value < card.value:
                high_card = card
        return high_card
