digit = input('Podaj liczbe: ')
#zeby otrzymac ze stringa integera -> skonwertowac na integera
digit = int(digit)

#@ todo: sprawdz czy liczba jest parzysta
if digit % 2 == 0:
    print('liczba jest parzysta')
#@ todo: w przeciwnym przypadku wyświetl 'liczba jest nieparzysta' PRACA DOMOWA
else:
    print('liczba nie jest parzysta')
