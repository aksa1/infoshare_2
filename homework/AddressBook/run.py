from address_book import *

FILE_NAME = 'phonebook.pickle'

PHONEBOOK = load_data(FILE_NAME)

while True:
    menu()
    try:
        opcja = int(input("Wybierz opcję: "))
    except ValueError:
        continue
    if opcja == 7:
        save_data(PHONEBOOK, FILE_NAME)
        break
    if opcja == 2:
        show_users_list(PHONEBOOK)
    if opcja == 6:
        user_id = input("podaj ID usera do usuniecia: ")
        del_user(PHONEBOOK, int(user_id))
        save_data(PHONEBOOK, FILE_NAME)
    if opcja == 1 or opcja == 5:
        if opcja == 5:
            user_id = input("podaj ID usera do modyfikacji: ")
            add_user(PHONEBOOK, user_id)
        else:
            add_user(PHONEBOOK)
        save_data(PHONEBOOK, FILE_NAME)
    if opcja == 3:
        nazwisko = input("podaj nazwisko usera do wyświetlenia: ")
        show_user_by_name(PHONEBOOK, nazwisko)
    if opcja == 4:
        user_id = input("podaj identyfikator usera: ")
        show_user(PHONEBOOK, user_id)