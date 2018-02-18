#program obliczajacy liczbe liter i cyfr w stringu
text = input('Podaj tekst: ')
ilosc_liter = 0
ilosc_cyfr = 0
ilosc_odstepow = 0
ilosc_pozostalych_znakow = 0
for i in text:
    if i.isalpha():
        ilosc_liter += 1
    elif i.isnumeric():
        ilosc_cyfr += 1
    elif i.isspace():
        ilosc_odstepow += 1
    else:
        ilosc_pozostalych_znakow += 1
print("Liter w ciagu: {}".format(ilosc_liter))
print("Cyfr w ciagu: {}".format(ilosc_cyfr))
print("odstepow w ciagu: {}".format(ilosc_odstepow))
print("pozostalcyh znakow: {}".format(ilosc_pozostalych_znakow))