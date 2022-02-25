class Player(object):
    def __init__(self, name=None):
        self.name = name
        self.cards = []
        self.score = 0

    def __repr__(self):
        name = self.name
        return name


class Deck(object):
    def __init__(self):
        self.cards = []
