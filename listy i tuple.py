# my_tuple = (1, 2, 3, [9, 8])
# my_tuple [3]
# my_tuple[3].append(7)
# my_tuple
# #sprawdzic co sie wyswietla i co sie zmodyfikowalo
#zamiana zmiennej


#my_list = list(range(0,11,2))
# print(my_list)

text = "ala ma kota"
something = list(text)
#print(list(text))
## to samo robił FOR
## for element in text:
# #    print(element)

# wyswietla: numer elementu i sam element (enumerate wypluwa tuple)
for idx, element in enumerate(something):
    print(idx, element)
# jw tylko w formacie tupli
for value in enumerate(something):
    print(value)
