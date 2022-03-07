import art_logo
import colorama
from colorama import Fore, Back, Style


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    return a / b


def calculate(num_1, num_2, sign):
    op_key = sign
    math_operators = \
        {
            "+": add(num_1, num_2),
            "-": sub(num_1, num_2),
            "*": mult(num_1, num_2),
            "/": div(num_1, num_2),
        }
    if op_key in math_operators:
        return math_operators[op_key]
    else:
        return


def format_result(int_result):
    return str(f"{int_result:.2f}")


is_computing = True
while is_computing:
    for i in range(100):
        print("\n")
    print(art_logo.logo)
    arg_1 = float(input("First Number: "))
    operator = input("Computation:\n\t'+' for ADDITION\n\t'-' for SUBTRACTION'"
                     "\n\t'*' for MULTIPLICATION\n\t'/' for 'DIVISION'")
    arg_2 = float(input("Second Number:"))
    result = calculate(num_1=arg_1, num_2=arg_2, sign=operator)
    if result is None:
        print(Fore.RED + "CAN NOT COMPUTE!" + Fore.RESET)
    else:
        print(f"ANSWER: {format_result(result)}")
        compute = input(Fore.LIGHTBLUE_EX + "CONTINUE? " + Fore.RESET + "Y | N ").lower()
        if compute != 'y':
            is_computing = False


