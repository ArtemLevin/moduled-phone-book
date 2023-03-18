import json
from colorama import Fore, Style


def main_menu():
    print('\n', f"{'CHOOSE THE ACTION': ^30}", '\n', f"{'MENU BAR': ^30}", '\n', '#' * 33, '\n',
          Fore.GREEN + Style.BRIGHT + 'Press 1 to open the phone book', '\n',
          'Press 2 to save the file', '\n',
          'Press 3 to search the contact information', '\n',
          'Press 4 to add a contact', '\n',
          'Press 5 to delete a contact', '\n',
          'Press 6 to modify a contact data', '\n',
          'Press 7 to exit',
          Style.RESET_ALL + " ")

    choice = input("Enter your choice ")
    return choice


def changes_is_saved():
    print('\n', "Changes is saved. What do you want to do next? ")


def the_book_is_opened():
    print('\n', "The book is opened. What do you want to do next? ")


def info_is_found():
    print('\n', "Info is found. What do you want to do next? ")

def no_info_is_found():
    print('\n', "Info is not found. What do you want to do next? ")


def enter_any_attribute_to_search():
    print("Enter name or number or special info of the contact: ")


def print_the_contact_info(book, key):
    print()
    for i in range(len(book[key])):
        print(f'{book[key][i]:^20}', end='')
    print()


def enter_name_number_info():
    new_name = input("Enter the name of the new contact ")
    new_number = input("Enter the number of the new contact ")
    new_info = input("Enter the info about the new contact ")
    return new_name, new_number, new_info


def to_delete():
    contact_to_delete = input("Enter the name of the contact to delete ")
    return contact_to_delete


def to_modify():
    contact_to_modify = input("What contact info do you want to modify? ")
    return contact_to_modify


def get_attribute_to_modify():
    attribute = input("What attribute do you want to modify: name, num, info? ")
    return attribute


def new_att_is_name():
    new_attribute_name = input("Enter new name of the contact ")
    return new_attribute_name


def new_att_is_number():
    new_attribute_number = input("Enter new number of the contact ")
    return new_attribute_number


def new_att_is_info():
    new_attribute_info = input("Enter new info of the contact ")
    return new_attribute_info


def leave_the_menu():
    answer = input("Do you want to leave? (y/n) ")
    return answer


def wrong_input():
    return print('Wrong input')
