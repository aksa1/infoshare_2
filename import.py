from collections import defaultdict, Counter
#
# my_dict = defaultdict(int)
#
# print(my_dict['non_existing'])

# the bad way
text = 'ala ma kota, kot ma ale'
my_dict = dict()
for char in text:
    #sprawdza czy cchar jest w kluczach
    if char in my_dict:
        my_dict[char]+= 1
    else:
        my_dict[char] = 1

print(my_dict)

# the better way
my_dict2 = defaultdict(int)
for char in text:
    #sprawdza czy cchar jest w kluczach
    if char in my_dict:
        my_dict2[char]+= 1
print(my_dict2 == my_dict)

# even the better way
print(Counter(text))

# the best

def test_counter():
    pass

# AKSA@ jak policzyc ile razy wystepuje wyraz