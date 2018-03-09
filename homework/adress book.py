#@ TODO - 1. lista slownik do przechowywania + modularyzacja kodu -> functions = szukaj, usun (main, function) + walidacja danych wejsciowych,
#@ TODO - 2. dodanie obslugi plików + obsluga wyjatkow (nie udalo sie zapisac, coś tam)
#@ TODO - 3. obsluga plikow zostaje + obiektowosc,
# class DB:  (nie wolamy funkcji tylko robimy to w klasie,
# DB('nazwa_pliku.txt' - otworzy plik, read, przechować dane,)
# class Person: z atrybutami (napisac takie klasy ktore jeszcze cos robia, a nie tylko przechowuja dane np. nadpisanie __STR__
# opcja SQLALCHEMY
# modul PICKLE - zrzucenie do pliku

adress_1 = {'imie': 'Adam', 'nazwisko': 'Kowalski', 'tel': 123}
adress_2 = {'imie': 'Anna', 'nazwisko': 'Niedziela', 'tel': 456}
adress_3 = {'imie': 'Alicja', 'nazwisko': 'Nowak', 'tel': 789}
phonebook = {
    1: adress_1,
    2: adress_2,
    3: adress_3
}

# def validate_data():
#     while not data.isalpha() and not data.isdigit():
#         print('Podales zle dane, podaj jeszcze raz')
#         data = input('Podaj poprawne dane: ')

def del_user(user_id):
    if user_id in phonebook.keys():
        del phonebook[user_id]
    else:
        print("Nie ma użytkownika o takim identyfikatorze")

def show_users_list():
    for user_id, data in phonebook.items():
        print("{}. {} {}".format(
            user_id,
            data['imie'],
            data['nazwisko'],
            data['tel']))

def show_user(user_id):
    data = phonebook[user_id]
    print("{} {} {}".format(data['imie'],data['nazwisko'],data['tel']))

def show_user_by_name(user_name):
    for user_id, data in phonebook.items():
        if user_name == data['nazwisko']:
            for key in data.keys():
                print("{}: {}".format(key, data[key]))

def add_user(user_id=None):

    if user_id:
        data = phonebook[user_id]
        show_user(user_id)
        new_id = user_id
    else:
        new_id = max(phonebook.keys()) + 1
    new_user_imie = input("podaj imię usera: ")
    new_user_nazwisko = input("podaj nazwisko usera: ")
    new_user_tel = input("podaj telefon usera: ")
    new_user = {'imie': new_user_imie, 'nazwisko': new_user_nazwisko,
                'tel': new_user_tel}

    phonebook.update({new_id: new_user})


def menu():
    print("Menu:")
    print("1 - Dodaj usera")
    print("2 - Wyswietl userów")
    print("3 - Wyswietl usera")
    print("4 - Modyfikuj usera")
    print("5 - Usuń usera")
    print("6 - Zakończ program")


while True:
    menu()
    opcja = int(input("Wybierz opcję: "))
    if opcja == 6:
        break
    if opcja == 2:
        show_users_list()
    if opcja == 5:
        user_id = input("podaj ID usera do usuniecia: ")
        del_user(int(user_id))
    if opcja == 1 or opcja == 4:
        if opcja == 4:
            user_id = int(input("podaj ID usera do modyfikacji: "))
            add_user(user_id)
        else:
            add_user()
    if opcja == 3:
        nazwisko = input("podaj nazwisko usera do wyświetlenia: ")
        show_user_by_name(nazwisko)