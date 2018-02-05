# # a=1
# # b=2
# # c=7
# # result=a+b
# # print(result)
# # result=a-b
# # print(result)
# # result=a*2
# # print(result)
# # result=c/b
# # print(result, type(result))
# # result=c//b
# # print(result,type(result))
# #
# # z=4.23
# # print(type(b))
# # print(type(z))
# # #konwersja typu ziennej
# # z_int=int(z)
# # print(type(z),z)
# # print(type(z_int),z_int)
# #
# # result=b**4
# # print(result)
# # #@TODO sprawdzic co oznacza ^w pythonie
# # # result=b^4
# # # print(result)
# #
# # # print('before', c)
# # # c+=2 #c=c+2
# # # c-=8
# # # c+=4
# # # c/=6
# # # print('after', c)
# #
# # #dzielenie z reszta
# # c=c%2
# # print(c)
# # zero=0
# # two=2
# # print(two/zero)
# #
# # #operator modulo - dzielenie przez 2 - spr czy liczba parzysta,
# #
# # text="Ala ma kota"
# # eng="Tom's house" #poniewaz tekst zawiera w tresci apostrof, to python go zle zinterpretuje zeby apostrof bedacy czescia tekstu wyswietlil sie jako tekst trzeba przed nim postawic \
# # eng2='Tom\'s house'
# # print(eng)
#
# #odwolywanie sie do konkretnych znakow w strongu
# text="ala ma kota"
# eng="Tom's house"
# letter_a=text[0]
# print(letter_a)
# letter_a=text[-2]
# print(letter_a)
#
# #zmierz długosc stringu
# lenght=len(text)
# print(lenght)
# last_char=text[lenght-1]
# print(last_char)
#
# #slices
# something=text[4:8] #[start:stop}
# print(something)
# something2=text[-4:-1] #podajemy w odwrotnej kolejnosci
# print(something2)
#
# steps=text[0:10:2]#podaje co 2. znak z calego stringu
# print(steps)
# dunno=text[0:15]
# #@todo: adres
# print(id(text))
#
# text2=text[::-1]
# print(text2)
#
# print(text2.lower) #po kropce rozne funckje ktore mozna zrobic z textem
#
# #text[0]='O'#stringi nie wykonuja operacje przypisanie - nie da sie nadpisac - stringi sa niemutowalen
# print(text)
#
# #podmienianie stringa na inny
# text='O'+text[1:]
# print(text)
# text=text[:4]+'M'+text[5:]
# print(text)
text3= "Ala ma kota, kot bardzo lubi Ale"
old='kot'
new='pies'
count=1
 #on nie nadpisuje textu a tworzy nowy
# replaced=text3.replace(old, new)
# print(text3,id(text3))#id pozwala potwierdzic ze to 2 rozne strongi
# print(replaced, id(replaced))
replaced=text3.replace(old, new, count)#pdomienia tylko 1 wystąpienie (1. ktore znajdzie)
print(text3,id(text3))
print(replaced, id(replaced))
