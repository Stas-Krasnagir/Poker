from Cards import deck
from players import *
from combinations import CardCombinations


def set_players():
    num_players = int(input("Set numbers of players: "))
    players = []
    for i in range(1, num_players + 1):
        name = "Player_" + str(i)
        players.append(name)
    print(players)
    pass


def start_game():
    deck.shuffle()
    table_cards = Deck()
    for i in range(5):
        deck.deal(table_cards)
    print(f"Open cards: {table_cards.cards}")

    player_1 = Player("Player_1")
    for i in range(2):
        deck.deal(player_1)
    print(f"Player_1 hand: {player_1.cards}")

    player_2 = Player("Player_2")
    for i in range(2):
        deck.deal(player_2)
    print(f"Player_2 hand: {player_2.cards}")

    hand_1 = check_hand(table_cards, player_1)
    #hand_2 = check_hand(table_cards, player_2)


def check_hand(table_cards, player):
    check_list = CardCombinations(table_cards.cards, player.cards)
    print(check_list.cards)
    check_list.cheсk()





start_game()
