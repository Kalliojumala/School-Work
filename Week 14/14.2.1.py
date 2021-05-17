#fix following prog

NUMEROT = [1, 2, 3, 100, 4, 5, 6]
"""
def kaanna():    

    NUMEROT = NUMEROT[-1:0:-1]

    print("Ennen kääntöä, NUMEROT =", NUMEROT)

    kaanna()

    print("Käännön jälkeen, NUMEROT =", NUMEROT)
"""

def kaanna():
    global NUMEROT
    #tämä jättää yhden numeron pois niinkuin esimerkissä?
    # NUMEROT = NUMEROT[-1:0:-1]
    
    #Ei jää numeroa pois mutta järjestys muuttuu jos lista on esim [1,7,3,76,4]
    # NUMEROT = sorted(NUMEROT, reverse=True)

    #kääntää listan, ei muuta järjestystä eikä jätä alkioita pois.
    NUMEROT = [numero for numero in reversed(NUMEROT)]
       
print("Ennen kääntöä, NUMEROT =", NUMEROT)
kaanna()
print("Käännön jälkeen, NUMEROT =", NUMEROT)


