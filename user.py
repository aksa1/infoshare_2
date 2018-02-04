#chcemy zeby userowi wyswietlil sie komunikat zeby podal nam dane
name = input('Podaj swoje imie: ')
age = input('Podaj ile masz lat: ')
# @todo wysiwtl na ekranie zmienna name
print(name)
# 1. the best way (message zawiera podane w formularzu dane, w messagu jest
# pokazane jak sformatować podane dane) dopiero print drukuje wynik
message = f'Twoje imie to: {name} {age}'
print(message)
