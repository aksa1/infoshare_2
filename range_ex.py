value = int(input('Podaj liczbe: ')
#@ todo: wyswielt kolejne parzyste bez instrukcji warunkowych
# range (Start, stop, krok) - start = 0
# wyswietlic dla liczb z zakresu tylko z funkcja for
start = 0
stop = value
step = 2
for idx in range(start, stop, step):
    print(idx)
