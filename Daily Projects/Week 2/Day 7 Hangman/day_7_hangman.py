import random
import colorama
import hangman_ascii_art as game_art

print(game_art.logo)


def clear_screen():
    for i in range(10):
        print("\n")


# Day 7 challenges are modular and in total create a full hangman game
def get_difficulty():
    has_chosen_diff = False
    difficulty_dict = {"1": "Easy", "2": "Medium", "3": "Hard"}
    while not has_chosen_diff:
        choose_diff = input("Please choose a difficulty. The harder the difficulty the more challenging the word."
                            "\n\t'1' for 'EASY'\n\t'2' for 'MEDIUM'\n\t'3' for 'HARD'\n\t Difficulty: ")
        if choose_diff in difficulty_dict:
            print(f"The difficulty is {difficulty_dict[choose_diff]}")
            has_chosen_diff = True
        else:
            print("I didn't quite get that. Please try again.")

    return difficulty_dict[choose_diff]


#ref for get_word
difficulty = get_difficulty()


def get_word(d=difficulty):

    word_file = open(r"/Daily Projects/Week 2/Day 7 Hangman/word_list_txt", "r")
    word_list = list(word_file.readlines())
    while True:
        max_index_range = len(word_list) - 1
        word_index = random.randint(0, max_index_range)
        word = word_list[word_index]
        word = word.strip()
        if d.lower() == "easy" and len(word) <= 5:
            break
        elif d.lower() == "medium" and 5 < len(word) <= 8:
            break
        elif d.lower() == "hard" and len(word) >= 9:
            break
        else:
            pass
    return word


word = get_word()
lives = 6
letters_left = len(word)
word_cover = ["_" for i in range(len(word))]
guessed_letters = []
hangman_sprite = game_art.stages

print(hangman_sprite[lives])
while lives and letters_left > 0:
    print(" ".join(word_cover))
    correct_letter = False
    ask_letter = input("Please choose a letter: ").lower()

    print(hangman_sprite[lives])
    if ask_letter in word_cover or ask_letter in guessed_letters:
        print(f"You have already guessed {ask_letter}.")
    for i in range(len(word)):
        if ask_letter == word[i]:
            word_cover[i] = ask_letter
            letters_left -= 1
            correct_letter = True

    if correct_letter:
        print(f"'{ask_letter}' was in the secret word!")
    else:
        lives -= 1
        print(f"Sorry! '{ask_letter}' was {colorama.Fore.RED + 'NOT' + colorama.Fore.RESET} in the secret word!")
        print(f"{lives} lives left!")
        guessed_letters.append(ask_letter)

if letters_left == 0:
    print(colorama.Fore.GREEN + 'YOU WIN !!!' + colorama.Fore.RESET)
else:
    print(hangman_sprite[0])
    print(colorama.Fore.RED + 'YOU LOSE!' + colorama.Fore.RESET)

print(f"The secret word was {word}")









