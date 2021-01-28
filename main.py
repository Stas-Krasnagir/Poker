from Cards import deck
from players import *
from combinations import CardCombinations
import collections


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
    print("___________")

    winners_list = {player_1.name: player_1.score,
                    player_2.name: player_2.score,
                    player_3.name: player_3.score,
                    player_4.name: player_4.score}

    sorted_values = sorted(winners_list.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for k in winners_list.keys():
            if winners_list[k] == i:
                sorted_dict[k] = winners_list[k]
                break
    res = list(sorted_dict)
    print(res)
    #print(f"Winner is {res[0]} \n Second is {res[1]}\n Third is {res[2]} \n Fourth is {res[3]}")






def check_hand(table_cards, player):
    check_list = CardCombinations(table_cards.cards, player.cards)
    player.score = check_list.cheсk()
    values = [card.value for card in player.cards]
    for value in values:
        player.score += value


start_game()
