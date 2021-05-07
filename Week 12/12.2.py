import sympy

#lazy me using modules...
print(sympy.isprime(int(input("Onko alkuluku?"))))

#teacher loop for primes numbers
"""
alkuLuku = True # oletetaan, että luku on alkuluku ellei toisin todisteta
luku = 13
silmukka_laskuri = 0

for i in range(2, luku):

    if luku % i == 0:

        alkuLuku = False;

    silmukka_laskuri += 1

 # Tulostetaan lopputulos

if alkuLuku:

    print(luku, "on alkuluku!")

else:

    print(luku, "EI OLE alkuluku.")

print("Silmukoiden kokonaismäärä:", silmukka_laskuri)
"""
