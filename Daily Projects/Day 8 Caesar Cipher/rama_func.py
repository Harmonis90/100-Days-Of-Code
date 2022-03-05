import colorama as col


def to_red(string):
    string = str(col.Fore.RED + f"{string}" + col.Fore.RESET)
    return string


def to_green(string):
    string = str(col.Fore.GREEN + f"{string}" + col.Fore.RESET)
    return string


def to_green_bright(string):
    string = str(col.Style.BRIGHT + col.Fore.GREEN + f"{string}" + col.Fore.RESET + col.Style.RESET_ALL)
    return string


def to_white_bright(string):
    string = str(col.Style.BRIGHT + col.Fore.WHITE + f"{string}" + col.Fore.RESET + col.Style.RESET_ALL)
    return string


def to_white(string):
    string = str(col.Fore.WHITE + f"{string}" + col.Fore.RESET)
    return string


def to_light_white(string):
    string = str(col.Fore.LIGHTWHITE_EX + f"{string}" + col.Fore.RESET)
    return string


def to_light_green(string):
    string = str(col.Fore.LIGHTGREEN_EX + f"{string}" + col.Fore.RESET)
    return string


def to_light_blue(string):
    string = str(col.Fore.LIGHTBLUE_EX + f"{string}" + col.Fore.RESET)
    return string


def to_light_yellow(string):
    string = str(col.Fore.LIGHTYELLOW_EX + f"{string}" + col.Fore.RESET)
    return string


def to_light_black(string):
    string = str(col.Fore.LIGHTBLACK_EX + f"{string}" + col.Fore.RESET)
    return string
