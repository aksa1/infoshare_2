b=2.34
a=0
text='abc'

#instrukcje warunkowe
# (każda wartość liczboa rozna od zera jest prawda)\
# każdy niepusty string jest prawda
if b > a:
    print('b > a')
# if b < a:
#     print('b < a')
elif b ==a:
    print('b==a')
else:
    print('b < a')

result = a > b
print(type(result), result)

if text:#zasada jak powinno sie pisac w pythonie
    print(('text is not empty'))

x = 1
y = 2
z = 3

#@todo: if 'a' < 'h' < 'z' (jak posortowac stringi?) PRACA DOMOWA
if x < y < z:
    print('hurra!')

# Laczymy dwa warunki
something = 'abc'
another = 'xyz'
if something == 'abc' and another == 'xyz':
    print('strings are the same')

#czy liczba jest parzysta
is_even = 4 % 2 #modulo 2
if is_even:
    print('the number is even')

#is_rest_equal_to_zero = 4 % 2 #modulo 2
#if not is_rest_equal_to_zero:
    #print('the number is even')

name = 'Jan'
lastname = 'Kowalski'
if name=='Jan' or lastname=='Kowalski':
    print('siema')