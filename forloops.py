#ala ma kota to 11 znakow
text = 'Ala ma kota'
# # to rozwiazanie lepsze
# for char in text:
#     print(char)
# # to gorsze
lenght = len(text)
# for idx in range (lenght):
#     print(text[idx])

some_range = range (lenght)
print(some_range)
#triczek
for value in some_range:
    print(value)
#pomaga ocenic czy petla sie juz zakonczyla, wazne jesli mamy program zalezny od zakonczenia innych procesow
else:
    print('Helloo')

