import module
import view
import module


def start():
    while True:
        choice = view.main_menu()

        if choice == str(1):
            module.open_the_book()
        elif choice == str(2):
            module.write_in()
        elif choice == str(3):
            module.searching()
        elif choice == str(4):
            module.new_contact()
        elif choice == str(5):
            module.delete_contact()
        elif choice == str(6):
            module.modifying_contact()
        elif choice == str(7):
            if module.exit_menu() == 0: break
        else:
            view.wrong_input()
            view.main_menu()
