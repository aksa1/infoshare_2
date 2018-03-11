#@ TODO - 1. lista slownik do przechowywania + modularyzacja kodu -> functions = szukaj, usun (main, function) + walidacja danych wejsciowych,
#@ TODO - 2. dodanie obslugi plików + obsluga wyjatkow (nie udalo sie zapisac, coś tam)
#@ TODO - 3. obsluga plikow zostaje + obiektowosc,
# class DB:  (nie wolamy funkcji tylko robimy to w klasie,
# DB('nazwa_pliku.txt' - otworzy plik, read, przechować dane,)
# class Person: z atrybutami (napisac takie klasy ktore jeszcze cos robia, a nie tylko przechowuja dane np. nadpisanie __STR__
# opcja SQLALCHEMY
# modul PICKLE - zrzucenie do pliku

import pickle

def del_user(phonebook, user_id):
    if user_id in phonebook.keys():
        del phonebook[user_id]
    else:
        print("Nie ma użytkownika o takim identyfikatorze")

def show_users_list(phonebook):
    for user_id, data in phonebook.items():
        print("{}. {} {} {}".format(
            user_id,
            data['imie'],
            data['nazwisko'],
            data['tel']))

def show_user(phonebook, user_id):
    #if not isinstance(user_id, 'int'):
    #    print("Niepoprawne dane wejściowe")
    #    return 0
    try:
        user_id = int(user_id)
        data = phonebook[user_id]
        print("{} {} {}".format(data['imie'],data['nazwisko'],data['tel']))
    except ValueError:
        print("Niepoprawne dane wejściowe. Poodaj ID usera")

def show_user_by_name(phonebook, user_name):
    for user_id, data in phonebook.items():
        if user_name == data['nazwisko']:
            for key in data.keys():
                print("{}: {}".format(key, data[key]))

def add_user(phonebook, user_id=None):
    if user_id:
        if user_id.isdigit():
            user_id = int(user_id)
            if user_id in phonebook.keys():
                data = phonebook[user_id]
                show_user(user_id)
                new_id = user_id
            else:
                print("Brak takiego usera")
                return
        else:
            print("Nieprawidłowe dane wejściowe")
            return
    else:
        new_id = max(phonebook.keys()) + 1
    new_user_imie = input("podaj imię usera: ")
    new_user_nazwisko = input("podaj nazwisko usera: ")
    try:
        new_user_tel = int(input("podaj telefon usera: "))
    except ValueError:
        print("Podałeś błędny numer telefonu. Ustawiam pusty.")
        new_user_tel = None

    new_user = {'imie': new_user_imie, 'nazwisko': new_user_nazwisko,
                'tel': new_user_tel}
    phonebook.update({new_id: new_user})

def menu():
    print("Menu:")
    print("1 - Dodaj usera")
    print("2 - Wyswietl userów")
    print("3 - Wyswietl usera")
    print("4 - Wyswietl usera (po ID)")
    print("5 - Modyfikuj usera")
    print("6 - Usuń usera")
    print("7 - Zakończ program")

def load_data(file_name):
    try:
        with open(file_name, 'rb') as fh:
            data = pickle.load(fh)
    except FileNotFoundError:
        adress_1 = {'imie': 'Adam', 'nazwisko': 'Kowalski', 'tel': 123}
        adress_2 = {'imie': 'Anna', 'nazwisko': 'Niedziela', 'tel': 456}
        adress_3 = {'imie': 'Alicja', 'nazwisko': 'Nowak', 'tel': 789}
        data = {
            1: adress_1,
            2: adress_2,
            3: adress_3
        }
    return data

def save_data(phonebook, file_name):
    with open(file_name, 'wb') as fh:
        pickle.dump(phonebook, fh)
