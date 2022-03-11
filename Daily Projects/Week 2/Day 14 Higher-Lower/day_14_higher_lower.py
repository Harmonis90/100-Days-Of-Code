import random
from higher_lower_data import data
import higher_lower_art as art
from colorama import Fore, Back, Style


def clear():
    for i in range(1):
        print("\n")


def print_magenta(text: str) -> str:
    return Fore.LIGHTMAGENTA_EX + f"{text}" + Fore.RESET


def print_black(text: str) -> str:
    return Fore.BLACK + f"{text}" + Fore.RESET


def gray_background(color_text: str):
    return Back.LIGHTBLACK_EX + print_black(text=color_text) + Style.RESET_ALL


def print_green(text: str) -> str:
    return Fore.LIGHTGREEN_EX + f"{text}" + Fore.RESET


def print_blue(text: str) -> str:
    return Fore.CYAN + f"{text}" + Fore.RESET


def print_red(text: str) -> str:
    return Fore.RED + f"{text}" + Fore.RESET


def get_random_data():
    return random.choice(data)


def format_random_data(data_set_one: dict) -> dict:
    formatted_data_dict = {}
    name = data_set_one["name"]
    f_count = data_set_one["follower_count"]
    description = data_set_one["description"]
    country = data_set_one["country"]
    vowels = ['a', 'e', 'i', 'o', 'u']
    pre_the_countries = ['United States', 'United Kingdom']
    if country in pre_the_countries:
        country = f"The {country.title()}"
    if description[0].lower() in vowels:
        format_data = f"{name}, an {description.lower()} from {country.title()}."
    else:
        format_data = f"{name}, a {description.lower()} from {country.title()}."
    formatted_data_dict["question"] = format_data
    formatted_data_dict["count"] = int(f_count)
    return formatted_data_dict


def get_bigger_count(count_one: int, count_two: int) -> int:
    if count_one > count_two:
        return count_one
    elif count_one < count_two:
        return count_two
    else:
        return -1


def get_player_input():

    main_question = print_magenta("Who has more followers?")
    print(main_question)
    print(f"{print_green('A:')} {print_green(data_set_one['question'])}")
    print(f"{print_red(art.vs)}")
    print(f"{print_blue('B:')} {print_blue(data_set_two['question'])}")
    answer = input(f"{print_green('A')} or {print_blue('B')}: ")
    return answer.lower()


def check_if_winner(player_answer: str, correct_answer: str) -> bool:
    if player_answer == correct_answer:
        return True
    else:
        return False


def format_winning_text(is_winner: bool, name: str) -> str:
    if is_winner:
        return print_green(f"CORRECT! {name} has more followers.")
    else:
        return print_red(f"Sorry! {name} actually has more followers.")


player_score = 0
data_set_one_raw = get_random_data()
data_set_one = format_random_data(data_set_one_raw)
is_playing = True
print(art.logo)
while is_playing:

    data_set_two_raw = get_random_data()
    data_set_two = format_random_data(data_set_two_raw)
    winner = {}
    winner_data_set_raw = {}
    winner_data_set = {}
    winner_name = ""

    check_winner = get_bigger_count(data_set_one["count"], data_set_two["count"])

    if data_set_one["count"] == check_winner:
        winner = 'a'
        winner_data_set_raw = data_set_one_raw
        winner_data_set = data_set_one
        winner_name = data_set_one_raw["name"]
    elif data_set_two["count"] == check_winner:
        winner = 'b'
        winner_data_set_raw = data_set_two_raw
        winner_data_set = data_set_two
        winner_name = data_set_two_raw["name"]
    else:
        print("Unable to calculate winner")

    is_valid_choice = False
    while not is_valid_choice:
        clear()
        player_choice = get_player_input()
        if player_choice == 'a' or player_choice == 'b':
            is_valid_choice = True
            if check_if_winner(player_choice, winner):
                player_score += 1
                win_text = format_winning_text(True, winner_name)
                print(f"{win_text} " + print_green(f"SCORE:{player_score}"))
                data_set_one = winner_data_set
                data_set_one_raw = winner_data_set_raw

            else:
                lost_text = format_winning_text(False, winner_name)
                print(f"{lost_text} Final Score: {player_score}")
                is_playing = False
        else:
            pass




