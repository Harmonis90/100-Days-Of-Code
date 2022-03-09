import random
import guesser_art as art
from colorama import Fore, Back, Style





def get_random_number(difficulty):
    if difficulty == 'easy':
        return random.randint(1, 100)
    else:
        return random.randint(1, 1000)


def get_difficulty():
    is_choosing = True
    difficulty = None
    while is_choosing:
        difficulty = input("Type the difficulty:\n\t" +
                           Fore.LIGHTGREEN_EX + "'Easy'" + " (range of 1 to 100)\n\t" + Fore.RESET +
                           Fore.RED + "'Hard'" + " (range of 1 to 1,000)\n\t" + Fore.RESET +
                           Fore.LIGHTWHITE_EX + "Difficulty: " + Fore.RESET).lower()
        if difficulty == 'easy' or difficulty == 'hard':
            return difficulty
        else:
            print("Spell it right dum dum.")


def get_player_guess():
    guess = input("Please guess a number: ")
    if guess.isdigit():
        return int(guess)
    else:
        get_player_guess()

def lose_one_life(num_lives):
    if num_lives - 1 >= 1:
        num_lives -= 1
        print(f"Lives: {num_lives}")
        return num_lives
    else:
        game_over()
        return num_lives - 1


def evaluate_guess(guess_num, real_num):

    if guess_num == real_num:
        winner()
        return True
    else:

        if guess_num > real_num:
            if guess_num - 10 <= real_num:
                print("So close, but a bit too high. You are within 10!")
            else:
                print("Nope. Too High.")
        else:
            if guess_num + 10 >= real_num:
                print("Just a smidge too low. But, you are within 10!")
            else:
                print("Too Low.")
        return False

def game_over():
    print(art.loser)


def winner():
    print(art.winner)


main_loop = True

while main_loop:
    guess_counter = 10
    print(art.logo)
    difficulty = get_difficulty()
    correct_num = get_random_number(difficulty)
    while guess_counter > 0:
        player_guess = get_player_guess()
        is_winner = evaluate_guess(player_guess, correct_num)
        if is_winner:
            break
        else:
            guess_counter = lose_one_life(guess_counter)
    try_again = input("Again?")