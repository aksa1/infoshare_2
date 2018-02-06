digit = input('Podaj liczbe: ')

if digit.isdigit() and int(digit) != 0:
    liczba = int(digit)
    #@ sprawdz czy liczba jest parzysta
    if liczba % 2 == 0:
        print('liczba jest parzysta')

    else:
        print('liczba nie jest parzysta')
else:
    print('nie podales liczby')
