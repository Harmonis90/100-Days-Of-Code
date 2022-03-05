import colorama as col
import cipher_art
import random
import rama_func as rf

alphabet_hard = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
alphabet_easy = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def print_logo():
    color_logo = ""
    for i in cipher_art.logo:
        color_logo += rf.to_light_green(i)
    print(color_logo)


def caesar_hard(text, shift, direction):
    text_index_list = []
    cipher_text = ""
    for i in text:
        text_index_list.append(alphabet_hard.index(i))
    if direction == 'encode':
        for num in text_index_list:
            cipher_text += alphabet_hard[(num + shift) % len(alphabet_hard)]
    else:
        for num in text_index_list:
            cipher_text += alphabet_hard[num - shift % len(alphabet_hard)]

    print(f"{col.Back.LIGHTBLACK_EX + col.Fore.RED + text + col.Fore.RESET + col.Back.RESET} "
          f"is {direction}d as:\n\n"
          f"{col.Back.LIGHTBLACK_EX + col.Fore.BLUE + cipher_text + col.Fore.RESET + col.Back.RESET}")


def caesar_easy(text, shift, direction):
    text_index_list = []
    cipher_text = ""
    for i in text:
        if i in alphabet_easy:
            text_index_list.append(alphabet_easy.index(i))
        else:
            text_index_list.append(i)
    if direction == 'encode':
        for num in text_index_list:
            if type(num) == int:
                cipher_text += alphabet_easy[(num + shift) % len(alphabet_easy)]
            else:
                cipher_text += str(num)
    else:
        for num in text_index_list:
            if type(num) == int:
                cipher_text += alphabet_easy[(num - shift) % len(alphabet_easy)]
            else:
                cipher_text += str(num)

    print(f"{col.Back.LIGHTBLACK_EX + col.Fore.RED + text + col.Fore.RESET + col.Back.RESET} "
          f"is {direction}d as:\n\n"
          f"{col.Back.LIGHTBLACK_EX + col.Fore.BLUE + cipher_text + col.Fore.RESET + col.Back.RESET}")


print_logo()
needs_cipher = True

while needs_cipher:
    has_state = False
    while not has_state:
        get_text_state = input("Type " + col.Fore.LIGHTBLUE_EX + "Encode " + col.Fore.RESET + "or " +
                               col.Fore.LIGHTMAGENTA_EX + "Decode " + col.Fore.RESET +
                               "to modify your message.\n".lower())
        if get_text_state == "encode" or get_text_state == "decode":
            has_state = True
        else:
            print("Try Again")

    get_text = input(f"What is your message?\n").lower()
    shift_amount = int(input("Shift each letter by how many places?\n\tShift Amount: "))
    caesar_easy(text=get_text, shift=shift_amount, direction=get_text_state)
    replay = input("Need to continue?\n\t'Y'|'N': ").lower()
    if replay == 'n':
        needs_cipher = False

print("THANK YOU!")


#caesar_hard(text=get_text, shift=shift_amount, direction=get_text_state)
