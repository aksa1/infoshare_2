counter = 0
value = input('Podaj liczbe: ')
value = int(value)

# @ todo: wyswietl wartosc coounter
# @ todo: wyswietl tylko jezeli counter jest nieparzysty (do WARTOSCI podanej w counterze)
# while counter < value:
# # ten kod wykonuje sie w petli
#    if counter % 2:
#         print (counter)
#         counter += 1
#    else:
#        counter += 1
#        continue
#     # ten juz poza petla
# print('Bye')

## ograniczamy wartość countera do 1000
while counter < value:
# ten kod wykonuje sie w petli
   if counter % 2:
        print (counter)
        counter += 1
   elif value > 1000:
       break
   else:
       counter += 1
       continue
    # ten juz poza petla
print('Bye')