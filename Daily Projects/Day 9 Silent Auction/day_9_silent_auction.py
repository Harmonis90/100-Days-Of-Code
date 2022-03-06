import art_logo as art


bids = {}


def clear():
    for i in range(100):
        print("\n")

def add_bid(name, bid):
    bids[name] = bid


def logo():
    print(art.logo)


def get_bidders():
    is_bidding_complete = False
    while not is_bidding_complete:
        logo()
        print("Welcome to 'Do You Really Want This???'\n")

        get_name = input("Please input your name.\n\tName: ")
        get_bid = round(float(input("How much will you be bidding?\n\t$")))
        add_bid(get_name, get_bid)
        is_finished = input("Thank you!\n Will anyone else be       bidding?  \n\t 'Y'|'N' ").lower()
        if is_finished == 'n':
            is_bidding_complete = True
        else:
            clear()


def find_winner():
    winning_bid = 0
    winner = ""

    for key in bids:

        if bids[key] > winning_bid:
            winning_bid = bids[key]
            winner = key

    print(f"{winner} WON with the bid with ${winning_bid}")


get_bidders()
find_winner()
