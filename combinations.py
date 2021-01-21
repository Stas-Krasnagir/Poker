class CardCombinations:
    def __init__(self, cards, player_cards):
        self.cards = cards + player_cards

    def cheсk(self):
        print(f"flush {self.flush()}")
        print(f"straight {self.straight()}")
        print(f"high_card {self.high_card()}")
        print(f"pairs {self.pairs()}")
        print(f"three_kind {self.three_kind()}")
        print(f"four_kind {self.four_kind()}")
        print(f"full_house {self.full_house()}")

    def flush(self):  # 5 cards of the same suit
        suits = [card.suit for card in self.cards]
        if len(set(suits)) == 1:
            return True
        return False

    def straight(self):  # Sequence of 5 cards in increasing value
        values = [card.value for card in self.cards]
        values.sort()

        if not len(set(values)) == 5:
            return False

        if values[4] == 14 and values[0] == 2 and values[1] == 3 and values[2] == 4 and values[3] == 5:
            return 5

        else:
            if not values[0] + 1 == values[1]:
                return False
            if not values[1] + 1 == values[2]:
                return False
            if not values[2] + 1 == values[3]:
                return False
            if not values[3] + 1 == values[4]:
                return False

        return values[4]

    def high_card(self):  # Simple value of the card
        values = [card.value for card in self.cards]
        high_card = None
        for card in self.cards:
            if high_card is None:
                high_card = card
            elif high_card.value < card.value:
                high_card = card

        return high_card

    def pairs(self):  # Two times two cards with the same value
        pairs = []
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 2 and value not in pairs:
                pairs.append(value)

        return pairs

    def four_kind(self):  # Four cards of the same value
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 4:
                return True

    def three_kind(self):  # Three cards with the same value
        values = [card.value for card in self.cards]
        for value in values:
            if values.count(value) == 3:
                return True

    def full_house(self):  # Combination of three of a kind and a pair
        two = False
        three = False

        values = [card.value for card in self.cards]
        if values.count(values) == 2:
            two = True
        elif values.count(values) == 3:
            three = True

        if two and three:
            return True

        return False

    def straight_flush(self):  # Straight of the same suit
        pass
