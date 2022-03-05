import math
import colorama


def print_red(string):
    return str(colorama.Fore.RED + f"{string}" + colorama.Fore.RESET)


def print_green(string):
    return str(colorama.Fore.GREEN + f"{string}" + colorama.Fore.RESET)


def greet():
    print("Hello!")
    print("This is line 2.")
    print("This is line 3.")


def greet_with_name(name):
    print(f"Hello {str(name).capitalize()}!")
    print(f"Am I spelling {name} correctly? {', '.join(list(name)).capitalize()}?")


def greet_with(name, location):
    print(f"Hello {name.capitalize()}. How is the weather in {location.title()}?")


#REDO OF DAY 6... WHICH WAS ACTUALLY DAY 8 CHALLENGES "OOPSIE POOPSIE"
def paint_calcs(height, width, cover):
    num_of_paint_cans = math.ceil(((height * width) / cover))
    print(f"You'll need {str(num_of_paint_cans)} cans of paint.")


def paint_calc_one_line(height, width, cover):
    print("You\'ll need " + str(math.ceil((height * width) / cover)) + " cans of paint.")


def prime_checker(number):
    max_range = int(math.sqrt(number))
    is_prime = False

    if number == 0 or number == 1 or number == 2:
        is_prime = False
    elif number % 2 == 0:
        is_prime = False
    elif number % 5 == 0:
        is_prime = False
    else:
        for num in range(3, max_range):
            if number % num == 0:
                is_prime = False
            else:
                is_prime = True
    if is_prime:
        print(f"{print_green(str(number))} is {print_green('PRIME')}!")
    else:
        print(f"{print_red(str(number))} is {print_red('NOT')} prime!")


prime_checker(122)