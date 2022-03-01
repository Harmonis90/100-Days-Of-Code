import random

def rand_float(min, max):
    i = random.randint(min, max)
    f = random.random()
    result = float(i + f)
    print(f"{result:.2f}")

#CHALLENGE 1 HEADS OR TAILS
def heads_or_tails():
    print(random.choice(["Heads", "Tails"]))
 

 #CHALLENGE 2 WHO IS PAYING?   
def who_is_paying():
    # 🚨 Don't change the code below 👇
    test_seed = int(input("Create a seed number: "))
    random.seed(test_seed)

    # Split string method
    names_string = input("Give me everybody's names, separated by a comma. ")
    names = names_string.split(", ")
    # 🚨 Don't change the code above 👆

    #Write your code below this line 👇
    print(names[random.randint(0, len(names) - 1)] + " is going to buy the meal today!")


def x_marks_the_spot():
    # 🚨 Don't change the code below 👇
    row1 = ["⬜️","⬜️","⬜️"]
    row2 = ["⬜️","⬜️","⬜️"]
    row3 = ["⬜️","⬜️","⬜️"]
    map = [row1, row2, row3]
    print(f"{row1}\n{row2}\n{row3}")
    position = input("Where do you want to put the treasure? ")
    # 🚨 Don't change the code above 👆

    #Write your code below this row 👇
    map[int(position[1]) - 1][int(position[0]) - 1] = "X"

    #Write your code above this row 👆

    # 🚨 Don't change the code below 👇
    print(f"{row1}\n{row2}\n{row3}")


x_marks_the_spot()