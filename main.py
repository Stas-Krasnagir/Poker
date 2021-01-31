from Cards import *
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


def check_hand(table_cards, player):
    check_list = CardCombinations(table_cards.cards, player.cards)
    player.score = check_list.cheсk()
    values = [card.value for card in player.cards]
    for value in values:
        player.score += value


# start_game()


def str_start_game():
    inp_str = "4cKs4h8s7s Ad4s Ac4d As9s KhKd 5d6d"
    str_table_card = inp_str[:10]
    str_players_card = inp_str[11:]
    split_list = str_players_card.split()

    dict_rank = {
        "2": Rank.Two,
        "3": Rank.Three,
        "4": Rank.Four,
        "5": Rank.Five,
        "6": Rank.Six,
        "7": Rank.Seven,
        "8": Rank.Eight,
        "9": Rank.Nine,
        "T": Rank.T,
        "J": Rank.J,
        "Q": Rank.Q,
        "K": Rank.K,
        "A": Rank.A}

    dict_suit = {
        "d": Suit.Diamonds,
        "c": Suit.Clubs,
        "h": Suit.Hearts,
        "s": Suit.Spades}

    def read_string_to_card(input_string: str):
        res = []
        for ind, i in enumerate(input_string):
            for j in dict_rank:
                if i == j:
                    res.append(Card(dict_rank.get(i).value, input_string[ind + 1]))
        return res

    table = read_string_to_card(str_table_card)
    table_cards = Deck()
    table_cards.cards = table

    player_1 = Player
    player_1.cards = read_string_to_card(split_list[0])
    print(player_1.cards)

    player_2 = Player
    player_2.cards = read_string_to_card(split_list[1])
    print(player_1.cards)
    print(player_2.cards)

    player_3 = Player
    player_3.cards = read_string_to_card(split_list[2])
    print(player_1.cards)
    print(player_2.cards)
    print(player_3.cards)

    player_4 = Player
    player_4.cards = read_string_to_card(split_list[3])
    print(player_1.cards)
    print(player_2.cards)
    print(player_3.cards)
    print(player_4.cards)

    player_5 = Player
    player_5.cards = read_string_to_card(split_list[4])

    print(player_1.cards)
    print(player_2.cards)
    print(player_3.cards)
    print(player_4.cards)
    print(player_5.cards)

    check_hand(table_cards, player_1)
    check_hand(table_cards, player_2)
    check_hand(table_cards, player_3)
    check_hand(table_cards, player_4)
    check_hand(table_cards, player_5)


str_start_game()
