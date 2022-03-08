import random
import art_logo

# Rules:
#   1: Ace is 1 or 11 depending.
#       if 11 == bust then a = 1
#   2: Face and the 10 card are worth 10
#   3: All other cards are worth their own value
#
#   4: Place bet before game starts
#       if player gets ace and face card on deal and dealer does not have same
#           player gets 1.5x their bet
#       if dealer gets a natural then hand is over
#       if dealer and player both get naturals then draw
#   5: The player goes first deciding weather to 'Hit' or 'Stand'
#           if player doesn't bust and stands, their hand is over and the dealer starts
#   6: if the dealer's hand is >= 17 dealer must stand
#           if the dealer's hand is <= 16 they must hit
#       if the dealer has an ace and the ace brings him to 17 or more,
#       the dealer must stand
#   7: if a players first two cards are the same they can split into two separate hands.
#           The newly created second hand must then have the same bet as the original hand.
#   8: if a players first two cards equal 9, 10 or 11 the player can double down to increase
#           their bet by 100%. They are then delt only ONE card and then must stand.


card_values = \
    {
        "A": [1, 11],
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 10,
        "Q": 10,
        "K": 10,
    }

player_hand = []
dealer_hand = []


def draw_card():
    return random.choice(list(card_values))


def deal_one_card(player_turn):
    if player_turn[0].lower() == "p":
        player_hand.append(draw_card())
        return player_hand
    else:
        dealer_hand.append(draw_card())
        return dealer_hand


def first_deal():
    deal_one_card("player")
    deal_one_card("player")

    deal_one_card("dealer")
    deal_one_card("dealer")

    black_jack_player = blackjack(player_hand)
    black_jack_dealer = blackjack(dealer_hand)

    if black_jack_player:
        print("BLACKJACK!")
        print_all_cards()
        return True
    if black_jack_dealer:
        print("BlackJack Dealer")
        print_all_cards()
        return True
    else:
        return False


def print_cards():
    dealer_hand_formatted = []
    for i in range(0, len(dealer_hand)):
        if i == 0:
            dealer_hand_formatted.append("-")
        else:
            dealer_hand_formatted.append(dealer_hand[i])
    print(f"""DEALER: {dealer_hand_formatted}
    
PLAYER: {player_hand} = {get_hand_value(player_hand)}""")


def print_all_cards():
    print(f"""DEALER: {dealer_hand} = {get_hand_value(dealer_hand)}
PLAYER: {player_hand} = {get_hand_value(player_hand)}""")


def get_hand_value(hand):
    hand_value = 0
    ace_count = 0
    has_ace = False
    for card in hand:
        if card == 'A':
            has_ace = True
            ace_count += 1
        else:
            hand_value += card_values[card]
    if has_ace:
        if hand_value + card_values['A'][1] > 21:
            hand_value += card_values['A'][0]  # 1
        else:
            hand_value += card_values['A'][1]  # 11
    return hand_value


def blackjack(first_two_cards):
    hand = list(first_two_cards)
    ten_cards = ['10', 'J', 'Q', 'K']
    if 'A' in hand:
        for i in hand:
            if i in ten_cards:
                return True
    return False


def is_bust(hand_value):
    if hand_value > 21:
        return True
    return False


def hit_or_stay():
    has_input = False
    while not has_input:
        player_input = input("'h' for HIT| 's' for STAY: ").lower()
        if player_input == 'h':
            return 'hit'
        elif player_input == 's':
            return 'stay'
        else:
            pass


def dealer():
    dealer_hand_value = 0
    is_dealer_turn = True
    dealer_hand_value = get_hand_value(dealer_hand)

    while is_dealer_turn:

        if dealer_hand_value < 17:
            deal_one_card("dealer")
            dealer_hand_value = get_hand_value(dealer_hand)
            if is_bust(dealer_hand_value):
                print("DEALER BUSTS! YOU WIN!")
                return -1
        else:
            is_dealer_turn = False
    print_all_cards()
    return dealer_hand_value


def player():
    player_hand_value = 0
    is_player_turn = True
    while is_player_turn:
        print_cards()
        player_hand_value = get_hand_value(player_hand)
        player_choice = hit_or_stay()
        if player_choice[0] == 'h':
            deal_one_card("player")
            if is_bust(get_hand_value(player_hand)):
                print("BUST!!!")
                return -1
        elif player_choice[0] == 's':
            is_player_turn = False
        else:
            pass
    return player_hand_value


def find_winner(player_value, dealer_value):
    if player_value > dealer_value:
        print("YOU WIN!")
    elif player_value == dealer_value:
        print("DRAW!")
    else:
        print("YOU LOSE!")


main_loop = True
while main_loop:

    game_loop = True
    while game_loop:
        print(art_logo.logo)
        has_blackjack = first_deal()
        if not has_blackjack:
            player_val = player()
            if player_val == -1:
                game_loop = False
            dealer_val = dealer()
            if dealer_val == -1:
                game_loop = False
            find_winner(player_val, dealer_val)
        player_hand.clear()
        dealer_hand.clear()
        input("Press Enter:")
