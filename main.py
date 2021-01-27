from Cards import deck
from players import *
from combinations import CardCombinations


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

    player_3 = Player("Player_3")
    for i in range(2):
        deck.deal(player_3)
    print(f"Player_3 hand: {player_3.cards}")

    player_4 = Player("Player_4")
    for i in range(2):
        deck.deal(player_4)
    print(f"Player_4 hand: {player_4.cards}")

    print("___________")

    check_hand(table_cards, player_1)
    check_hand(table_cards, player_2)
    check_hand(table_cards, player_3)
    check_hand(table_cards, player_4)

    print("___________")

    print(f"Player_1 score: {player_1.score}")
    print(f"Player_2 score: {player_2.score}")
    print(f"Player_3 score: {player_3.score}")
    print(f"Player_4 score: {player_4.score}")



def check_hand(table_cards, player):
    check_list = CardCombinations(table_cards.cards, player.cards)
    player.score = check_list.cheсk()
    values = [card.value for card in player.cards]
    for value in values:
        player.score += value


def final_score(player):
    pass





start_game()
