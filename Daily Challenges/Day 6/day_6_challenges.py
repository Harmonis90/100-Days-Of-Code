import math


def paint_calc(height, width, cover):
    print("You\'ll need " + str(round((height * width) / cover)) + " cans of paint.")


def prime_checker(number):
    is_prime = True
    if number % 2 == 0 or number % 5 == 0:
        is_prime = False
    max_range = int(math.sqrt(number))
    for i in range(3, max_range, 2):
        if number % i == 0:
            is_prime = False

    print(is_prime)


prime_checker(157)
