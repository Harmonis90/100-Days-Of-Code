import coffee_data as cd
from colorama import Fore, Back, Style


def print_red(text: str) -> str:
    return Fore.RED + f"{text}" + Fore.RESET


def new_lines(n: int):
    for i in range(n):
        print("\n")


def get_coffee_choice():
    coffee_types = {1: "espresso", 2: "latte", 3: "cappuccino"}
    is_valid_drink = False
    while not is_valid_drink:
        drink_choice = input("Please Choose A Beverage:"
                             "\n\t1: Espresso"
                             "\n\t2: Latte"
                             "\n\t3: Cappuccino"
                             "\n\t Enter the appropriate number: ")

        # CHECK FOR OP COMMANDS
        special_op_commands(drink_choice)
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


def complete_transaction(price: float):
    currency = \
        {
            "Quarter": 0.25,
            "Dime": 0.10,
            "Nickle": 0.05,
            "Penny": 0.01,
        }

    print(f"The cost of a {current_drink} is ${price}"
          f"\n\tPlease insert your change.")
    calculating_change = True
    while calculating_change:
        customer_change_total = 0.0
        print(f"Amount inserted: ${customer_change_total:.2f}")

        quarters = input("Insert Quarters: ")
        if quarters.isdigit():
            customer_change_total += int(quarters) * currency["Quarter"]
            print(f"Amount inserted: ${customer_change_total:.2f}")

        dimes = input("Insert Dimes: ")
        if dimes.isdigit():
            customer_change_total += int(dimes) * currency["Dime"]
            print(f"Amount inserted: ${customer_change_total:.2f}")

        nickles = input("Insert Nickles: ")
        if nickles.isdigit():
            customer_change_total += int(nickles) * currency["Nickle"]
            print(f"Amount inserted: ${customer_change_total:.2f}")

        pennies = input("Insert Pennies: ")
        if pennies.isdigit():
            customer_change_total += int(pennies) * currency["Penny"]
            print(f"Amount inserted: ${customer_change_total:.2f}")

        if customer_change_total >= price:
            if customer_change_total > price:
                change = customer_change_total - price
                print(f"Your change is ${change:.2f}")
                return price
            else:
                print("Thank you for exact change.")
                return price
        print("Invalid Amount. Please take your change back and try again.")


def get_ingredients(drink: str) -> dict:
    ingredients = menu[drink]["ingredients"]
    return ingredients


def has_enough_resources(recipe: dict):
    recipe_list = list(recipe)
    for item in recipe_list:
        if current_resources[item] - recipe[item] <= 0:
            out_of_order(item)
            return False
        else:
            current_resources[item] -= recipe[item]

    return True


def brew():
    print(Back.LIGHTBLUE_EX + Fore.LIGHTGREEN_EX + "BREWING" + Style.RESET_ALL)
    print(Back.LIGHTMAGENTA_EX + Fore.LIGHTGREEN_EX + "BREWING" + Style.RESET_ALL)
    print(Back.LIGHTBLACK_EX + Fore.LIGHTGREEN_EX + "BREWING" + Style.RESET_ALL)


def out_of_order(item):
    print(print_red(f"Sorry! We are currently out of {item}!"))


def special_op_commands(command: str):
    if command == 'OFF':
        print(print_red("Systems Operator == True. Entering Sleep Mode."))
        exit()
    elif command == 'REPORT':
        print(print_red(
            f"\n\tWater: {current_resources['water']} ml,"
            f"\n\tMilk: {current_resources['milk']} ml,"
            f"\n\tCoffee: {current_resources['coffee']} g,"
            f"\n\tTotal Earnings: ${float(current_resources['earnings']):.2f}"))


is_running = True
while is_running:
    current_resources = cd.resources
    menu = cd.MENU
    current_drink = get_coffee_choice()
    drink_ingredients = get_ingredients(current_drink)
    can_brew = has_enough_resources(drink_ingredients)

    if can_brew:
        new_lines(1)
        current_drink_price = menu[current_drink]["cost"]
        current_resources["earnings"] += complete_transaction(current_drink_price)
        brew()
        print(f"Please enjoy your {current_drink}!")
    else:
        is_running = False





