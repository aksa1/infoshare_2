#@ todo uzytkownik podaje start
#@ todo uzytkownik podaje stop
#@ todo *uzytkownik podaje krok
#@ todo wykorzystując FOR zliczyć liczby parzyste i nieparzyste
#@ todo w zbiorze od start do stop wlacznie
#@ todo **uzytkownik podaje w takim formacie: (start, stop, krok)
#@ todo poszukać SPLIT + delimiter

value_start = int(input('Podaj liczbe start: '))
value_stop = int(input('Podaj liczbe stop: '))
start = int(value_start)
stop = int(value_stop)
for idx in range(start, stop):
    count(idx)
