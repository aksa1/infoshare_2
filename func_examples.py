def infinitive_arguments(*args):
    print(args)
    print((type(args)))
infinitive_arguments(1, 2, 3, 4, 5)
#musi byc iterowalne tupla, slownik, lista
print(sum([1, 2])),

#funcja z dowolna liczna arg liczbowych i wyswietli na ekranie ich sume
def funkcja(*args):
    print(sum(args))
    print(type(args))
funkcja(1, 2, 3, 4, 5)
funkcja(*[1, 2, 3])
#rozpakowywanie funkcji za arg pozycyjnych - jest tupla
x, y, z, *something = (1, 2, 3, 4, 5, 6)
*nevermind, a, b = (1, 10, 20 ,30 ,40)
print(nevermind)
#czy to mi wstawilo wolny wiersz miedzy tymmi dowma printami
print("\n")
print(a, b)

def foo(a, b, *args):
    """
    prints given arguments
    :param a:
    :param b:
    :param args:
    :return:
    """
    print(a, b, *args)
foo(1, 2)
foo(1, 2, 3, 4, 5, 60)
foo(1, 2, *range(100))

#argumenty nazwane - sa slownikiem
def bar(**kwargs):
    #print(kwargs)
    for key, value in kwargs.items():
        print(f'{key}-> {value}')

bar(a=1, b=2, zxc=4)
my_dict = {'Kowalski': 123, 'Nowak': 456}
my_dict.update()

#rozpakowywanie
bar(**my_dict)

def baz(x, y, **kwargs):
    pass

#return - zwroc to co bedzie po nim

def funkcja_z_return(*args):
    #pass
    return(sum(args))
values_to_sum = [1, 2, 10, 15]
result = funkcja_z_return(*values_to_sum)
print(result)