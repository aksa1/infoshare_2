# Narysuj piramidę Mario - jako input - wysokość piramidy
# np. piramida wysokości 3 ma wyglądać:

  #
 ###
#####

h = int(input('Podaj wysokosc piramidy: '))
for i in range(0, h):
    print((h-i)*' '+((2*i+1)*'*')+(h-i)*' ')