import coffee_data as cd
from clear_screen import clear




def get_coffee_choice():
    coffee_types = {1: "espresso", 2: "latte", 3: "cappuccino"}
    is_valid_drink = False
    while not is_valid_drink:
        drink_choice = input("Please Choose A Beverage:"
                             "\n\t1: Espresso"
                             "\n\t2: Latte"
                             "\n\t3: Cappuccino"
                             "\n\t Enter the appropriate number: ")
        if drink_choice.isdigit():
            if int(drink_choice) in coffee_types:
                is_correct = False
                while not is_correct:
                    check_choice = input(f"Are you sure you want {coffee_types[int(drink_choice)].title()}?"
                                         f"\n\tY : N for {coffee_types[int(drink_choice)].title()} ").lower()
                    if check_choice == "y":
                        return coffee_types[int(drink_choice)]
                    elif check_choice == 'n':
                        break


get_coffee_choice()
clear()





