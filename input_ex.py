#@ TODO pobierz od uzytkownika dowolna liczne lub znak
#@ TODO i sprawdz czy wprowadzone dane to liczna lub litera
#@ TODO wyświetl koomunikat dla np. 'wprowadziles dane typu:liczba'

# data = input('Podaj liczbe lub litere: ')
#
# if data.isdigit():
#     print('podales cyfre')
#     print('bye')
# elif data.isalpha():
#     print('podales liczbe')
#     print('bye')
# else:
#     print('help')


# #prosimy uzytkowniaka by podal w koncu prawidlowe dane
# data = input('Podaj cyfre lub litere: ')
# while not data.isalpha() and not data.isdigit():
#     print('podales bledne dane, podaj jeszcze raz')
#     data = input('Podaj cyfre lub litere: ')
# if data.isdigit():
#     print('Podales cyfre')
# elif data.isalpha():
#     print('podales litere')
# print('bye')

# @ todo uzytkonik podaje dane i oczekujemy ze dane to liczba oraz
# @ todo ze jesli jest to liczna to jest ona !=0
#podaj cyfry tylko rozne od zera
data = input('Podaj liczbe: ')
while not data.isdigit() or int(data)==0:
    print('podales bledne dane, podaj jeszcze raz')
    data = input('Podaj liczbe: ')
print('thx')


