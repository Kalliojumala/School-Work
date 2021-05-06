#list with addresses, print items with text "Ei pysäköintiä" randomly on index 0 or 4
from random import choice 
rndm_index = choice([0,4])

add_list = ['Oikopolku 2', 'Umpikuja 3', 'Tienhaara 5', 'Välitie 6', 'Mikonkatu 4']

for i in range(5):
    if i == rndm_index:
        print(f"{add_list[i]} - Ei pysäköintiä!")
        continue
    print(add_list[i])