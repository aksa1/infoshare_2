name = "ola"
def hello(username):
    """
    returns uppercase username
    :param username:
    :return:
    """
 #   global name - uzywa zmiennej zdefinowanej poza funkcją i ja uzywa. ale to zla praktyka bo mozna sobie zmasakrowac dzialanie programu
    name = username.upper()
    return (name)

data = input('Podaj imie: ')
uppercase = hello(data)
print(uppercase)
print(name)
#variable scope - zasieg widocznosci zmiennej

