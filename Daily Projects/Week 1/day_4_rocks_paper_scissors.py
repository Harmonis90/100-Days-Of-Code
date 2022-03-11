import random

player_score = 0
ai_score = 0

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ________
---'   _______)__
          ________)
          _________)
         _________)
---.____________)
'''

scissor = '''
    _______
---'   ____)______
          _________)
       _____________)
      (____)
---.__(___)
'''

print("Welcome to Rock, Paper, Scissors!")


def game():

    print("Which sign will you thrown down?\n\tRock:    'R'\n\tPaper:   'P'\n\tScissor: 'S'")
    is_selected = False
    player_choice = None
    choices = ['r', 'p', 's']
    while not is_selected:
        selection = input("Selection: ").lower()
        if selection[0] in choices:
            is_selected = True
            if selection == choices[0]:
                player_choice = "r"
            elif selection == choices[1]:
                player_choice = "p"
            else:
                player_choice = "s"
        else:
            print("I didn't quite get that...")
    ascii_select = {"r": rock, "p": paper, "s": scissor}
    choices_format = {"r": "rock", "p": "paper", "s": "scissor"}
    ai_choice = choices[random.randint(0, 2)]
    print(ascii_select[player_choice])
    print(ascii_select[ai_choice])
    player_win_conditions = {("r", "s"), ("p", "r"), ("s", "p")}
    if (player_choice, ai_choice) in player_win_conditions:
        print(f"You win! {choices_format[player_choice].capitalize()} beats {choices_format[ai_choice].capitalize()}")
        global player_score
        player_score += 1

    elif player_choice == ai_choice:
        print("Tie")
    else:
        print(f"You Lose! {choices_format[ai_choice].capitalize()} beats {choices_format[player_choice].capitalize()}")
        global ai_score
        ai_score += 1


is_playing = True
while is_playing:
    game()
    print(f"Player: {player_score}\tComputer: {ai_score}")
    play_again = input("Play Again? 'Y':'N' ").lower()
    if play_again[0] == "n":
        is_playing = False
    else:
        continue

if player_score > ai_score:
    print("You came out on top! Good job! ***THEME MUSIC***")
elif player_score == ai_score:
    print("A tie! I guess that's not a loss.")
else:
    print("Well, that was... something. Better luck next time.")
