import view
import json
path = 'phone.json'
book = {}

def write_in(your_book):
    with open(path, 'w', encoding="UTF-8") as some_file:
        some_content = json.dumps(your_book)
        some_file.write(some_content)
    view.changes_is_saved()
    view.main_menu(book)

def read_out():
    with open(path, 'r', encoding="UTF-8") as some_file:
        some_content = some_file.read()
        book = json.loads(some_content)
    return book

def open_the_book():
    book = read_out()
    for key in book:
        for i in range(len(book[key])):
            print(f'{book[key][i]:^20}', end='')
        print()
    view.the_book_is_opened()
    view.main_menu(book)

def searching(book):
    view.enter_any_attribute_to_search()
    data_to_search = input()
    for key in book:
        if data_to_search in book[key]:
            view.print_the_contact_info(book, key)
    view.info_is_found()
    view.main_menu(book)