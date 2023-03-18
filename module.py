import view
import json

path = 'phone.json'
# book = {}


def write_in():
    book = read_out()
    with open(path, 'w', encoding="UTF-8") as some_file:
        some_content = json.dumps(book)
        some_file.write(some_content)
    view.changes_is_saved()


def write_in_new_contact(book):
    with open(path, 'w', encoding="UTF-8") as some_file:
        some_content = json.dumps(book)
        some_file.write(some_content)
    view.changes_is_saved()



def read_out():
    with open(path, 'r', encoding="UTF-8") as some_file:
        some_content = some_file.read()
        book = json.loads(some_content)
    return book


def open_the_book():
    book = read_out()
    for key in book:
        view.print_the_contact_info(book, key)
    view.the_book_is_opened()



def searching():
    book = read_out()
    view.enter_any_attribute_to_search()
    data_to_search = input()
    counter = 0
    for key in book:
        if data_to_search in book[key]:
            view.print_the_contact_info(book, key)
            view.info_is_found()
            counter += 1
    if counter == 0: view.no_info_is_found()


def new_contact():
    book = read_out()
    new_name, new_number, new_info = view.enter_name_number_info()
    book[new_name] = [new_name] + [new_number] + [new_info]
    write_in_new_contact(book)



def delete_contact():
    book = read_out()
    contact_to_delete = view.to_delete()
    if contact_to_delete in book.keys():
        del book[contact_to_delete]
        write_in_new_contact(book)



def modifying_contact():
    book = read_out()
    contact_to_modify = view.to_modify()
    if contact_to_modify in book.keys():
        attribute = view.get_attribute_to_modify()
        if attribute == 'name':
            new_attribute_name = view.new_att_is_name()
            book[contact_to_modify][0] = new_attribute_name
        elif attribute == 'num':
            new_attribute_num = view.new_att_is_number()
            book[contact_to_modify][1] = new_attribute_num
        elif attribute == 'info':
            new_info = view.new_att_is_info()
            book[contact_to_modify][2] = new_info
        write_in_new_contact(book)



def exit_menu():
    answer = view.leave_the_menu()
    if answer == 'y':
        return 0
