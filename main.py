from Cards import deck
from players import *


def set_players():
    num_players = int(input("Set numbers of players: "))
    players = []
    for i in range(1, num_players+1):
        name = "Player_"+str(i)
        players.append(name)
    print(players)
    pass

def start_game():
    deck.shuffle()
    table_cards = Deck()
    count = 0
    while count < 5:
        deck.deal(table_cards)
        count += 1
    print(f"Open cards: {table_cards.cards}")

    player_1 = Player("Player_1")
    deck.deal(player_1)
    deck.deal(player_1)
    print(f"Player_1 hand: {player_1.cards}")

    player_2 = Player("Player_2")
    deck.deal(player_2)
    deck.deal(player_2)
    print(f"Player_2 hand: {player_2.cards}")
    check_hand(table_cards.cards, player_1.cards)

def check_hand(table, hand):
    pass
    check_list = []
    check_list.append(table.cards.pop())
    check_list.append(hand.cards.pop())
    check_list.sort()
    print(check_list)







start_game()