# my_list = list(range(0,11,2))
# my_list.append(13)
# print(my_list)
#
# my_list.reverse()
# print(my_list)
# my_list2 = reversed(my_list)

#@ todo: sprawdzy czy my_list jest indet z my_list2
my_list = list(range(10))
my_list2 = reversed(my_list)
#@ todo: sprawdzy czy my_list jest indet z my_list2
print(my_list)
print(my_list2)
print(my_list, list(my_list2))
#@ todo: zrob kopie my-list i przypusz do zmiennej my_list2
my_list2 = my_list.copy()

#@ todo: odwroc kolejnosc elementow in place z my_list
my_list.reverse()
#@ todo: przypisz do zmiennej wynik reversed(my_list2)
my_list2 = my_list.reverse()

#@ todo: sprawdzy czy my_list jest indet z my_list2
#my_list2 = reverse(my_list2)
print(my_list, my_list2)

if my_list == my_list2:
    print('listy sa takie same')
print(id(my_list))
print(id(my_list2))

print(type(my_list2))
print(isinstance(my_list2, list))

# for idx, element in enumerate(my_list2):
#     print(idx, element)

# wysukiwanie elementow
#print(my_list.index(None))

list_a = [1, 2, 3]
list_b = [4, 5, 6]
# dokleja zagniezczona liste b do listy a
list_a.append(list_b)
print(list_a)
print(list_a[3][1])
list_c = [1, [2, 3]]
#dokleja elementy z liste b do listy a
list_a.extend(list_b)
print(list_a)
list_b.extend(list_c)
print(list_c)