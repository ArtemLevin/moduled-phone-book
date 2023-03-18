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

def changes_is_saved():
    print('\n', "Changes is saved. What do you want to do next? ")

def the_book_is_opened():
    print('\n', "The book is opened. What do you want to do next? ")

def info_is_found():
    print('\n', "Info is found. What do you want to do next? ")

def enter_any_attribute_to_search():
    print("Enter name or number or special info of the contact: ")

def print_the_contact_info(book, key):
    print()
    for i in range(len(book[key])):
        print(f'{book[key][i]:^20}', end='')
    print()