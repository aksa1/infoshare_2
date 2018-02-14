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

x, y, z, *something = (1, 2, 3, 4, 5, 6)
*nevermind, a, b = (1, 10, 20 ,30 ,40)
print(nevermind)
print(a, b)

def foo(a, b, *args):
    print(a, b, *args)
foo(1, 2)
foo(1, 2, 3, 4, 5, 60)
foo(1, 2, *range(100))
