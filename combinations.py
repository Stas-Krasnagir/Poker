class CardCombinations:
    def __init__(self, cards, player_cards):
        self.cards = cards + player_cards

    def cheak_suits(self):
        suits = [card.suit for card in self.cards]
        return suits

    def cheak_values(self):
        values = [card.value for card in self.cards]
        return values

    def cheсk(self):
        if self.royal_flush():
            print("Royal flush")
        elif self.straight_flush():
            print("Straight flush")
        elif self.four_kind():
            print("Four kind")
        elif self.full_house():
            print("Full house")
        elif self.flush():
            print(self.flush())
        elif self.straight():
            print(self.straight())
        elif self.three_kind():
            print("Three kind")
        elif self.pairs():
            print(self.pairs())
        elif self.two_pairs():
            print(f"Two pairs of {self.two_pairs()}")
        else:
            print(f"High card: {self.high_card()}")

    def royal_flush(self):  # Straight flush from Ten to Ace
        one_suit = False
        sequence = False
        if self.flush():
            one_suit = True
        elif self.straight():
            values = self.cheak_values()
            values.sort()
            if values[6] == 14:
                sequence = True
            else:
                sequence = False
        if one_suit and sequence:
            return True
        return False

    def flush(self):  # 5 cards of the same suit
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

    def straight(self):  # Sequence of 5 cards in increasing value
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

    def high_card(self):  # Simple value of the card
        values = self.cheak_values()
        high_card = None
        for card in self.cards:
            if high_card is None:
                high_card = card
            elif high_card.value < card.value:
                high_card = card

        return high_card

    def pairs(self):  # Two times two cards with the same value
        pairs = []
        values = self.cheak_values()
        for value in values:
            if values.count(value) >= 2 and value not in pairs:
                pairs.append(value)
            if pairs:
                return f"Pair of {pairs}"
            return False

    def four_kind(self):  # Four cards of the same value
        values = self.cheak_values()
        for value in values:
            if values.count(value) == 4:
                return True

    def three_kind(self):  # Three cards with the same value
        values = self.cheak_values()
        for value in values:
            if values.count(value) == 3:
                return True

    def full_house(self):  # Combination of three of a kind and a pair
        two = False
        three = False

        values = self.cheak_values()
        if values.count(values) == 2:
            two = True
        elif values.count(values) == 3:
            three = True

        if two and three:
            return True

        return False

    def straight_flush(self):  # Straight of the same suit
        one_suits = False
        five_in_line = False
        if self.straight():
            five_in_line = True
        elif self.flush():
            one_suits = True

        if one_suits and five_in_line:
            return True
        return False

    def two_pairs(self):  # Two times two cards with the same value
        pairs = []
        values = self.cheak_values()
        for value in values:
            if values.count(value) >= 2 and value not in pairs:
                pairs.append(value)
            if len(pairs) > 1:
                return f"Pair of {pairs}"
            return False
