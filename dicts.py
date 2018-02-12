phonebook = {
    'Kowalski': 123,
    'Aksa': 567,
    'Morawski': 985,
}
#pobieranie wartosci z klucza Kowalski
#print(phonebook['Aksa'])

# lastname = input('Podaj nazwisko: ')
# print(phonebook[lastname])

lastname = 'XYZ'
print(phonebook.get(lastname, 'Brak takiego nazwiska'))

new_phonebook = phonebook.copy()
print(new_phonebook)
new_members = {'XYZ': 1, 'ABC': 2}

#scalanie tych 2 slownikow
new_phonebook.update(new_members)
print(new_phonebook)

# update nadpisze dane

new_phonebook['XYZ']=0
print(new_phonebook)

new_phonebook.update({'XYZ': 5})
print(new_phonebook)
#ponizsze niepythonowskie
new_phonebook.update(Kowalski=898, Aksa=111)
print(new_phonebook)

