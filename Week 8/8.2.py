###KORJAUS TEHTÄVÄ , EN JAKSANUT KÄÄNTÄÄ ENGLANNIKSI
"""
Korjaa virhe seuraavasta koodista
for numero in range[2, 21, 2]

    print(numero)
"""
#koodi tulostaa parilliset numerot 2-20
for numero in range(2, 21, 2):
    print(numero)



"""sub_total = 0
temp = 0
for item in range( , ,):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)

Tulostus:
sub_total: 0 + 25 = 25
sub_total: 25 + 30 = 55
sub_total: 55 + 35 = 90
sub_total: 90 + 40 = 130
sub_total: 130 + 45 = 175
Total = 175
"""
#Täydennä seuraava koodi niin, että syntyy seuraava tulostus
sub_total = 0
temp = 0
for item in range(25,46,5):
    temp = sub_total
    sub_total += item
    print("sub_total:", temp, "+", item, "=",sub_total)
print("Total =", sub_total)