from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def get_payment(beverage):
    # beverage = menu.find_drink(beverage)
    is_paying = True
    while is_paying:
        has_payed = money_machine.make_payment(beverage.cost)
        if has_payed:
            return True


def get_drink():
    is_valid_option = False
    while not is_valid_option:
        options = menu.get_items()
        formatted_options = options.replace("/", ", ")
        choice = input(f"We currently have {formatted_options}\n\tPlease type in your beverage. ")
        if choice == 'report':
            get_report()
        elif choice in options:
            return choice


def get_report():
    coffee_maker.report()
    money_machine.report()


is_working = True
while is_working:
    print("Welcome To lOOPy Coffee!")
    is_valid_drink = get_drink()
    drink = menu.find_drink(is_valid_drink)
    if coffee_maker.is_resource_sufficient(drink):
        if get_payment(drink):
            coffee_maker.make_coffee(drink)
    else:
        is_working = False
