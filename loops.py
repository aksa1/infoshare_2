## user podaje liczbe i petla while bedzie tyle razy wyswietlac hello
# while True:
#     print('Hello')
##wyświetla w nieskonczonosc napis hello

licznik = 0
value = input('Podaj liczbe: ')
value = int(value)
while licznik < value:
# ten kod wykonuje sie w petli
    print ('Hello')
    licznik += 1
# ten juz poza petla
print('Bye')
