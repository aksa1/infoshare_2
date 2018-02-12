my_tuple = (1, 2, 3)
# ponizsze nie dzial!
# my_tuple[1] = 5 + proba przpisania pod element 1 cyfre 5
still_tuple = (4, 5, 6, [7, 8])
still_tuple[-1].append(9)
print(still_tuple)
#powstawje tupla z tupli - nie mozna zapomniec o przecinku po 4 bo to oznacza tuple jednoelementowa
my_tuple = my_tuple + (4,)
print(my_tuple)

