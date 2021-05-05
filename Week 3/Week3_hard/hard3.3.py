#even or odd number

def even_or_odd(num: int):
    return num % 2 == 0

def even_and_compare():
    #takes 2 numbers as input
    num = int(input("Syötä kokonaisluku: "))
    compare = int(input("\nSyötä vertailuluku: "))
    
    #comparison block, self explanatory imo!
    if even_or_odd(num):
        print("\nSyöttämäsi luku on parillinen.\n")
    else:
        print("\nSyöttämäsi luku on pariton.\n")

    if num > compare:
        print(f"Luku {compare} on pienempi kuin {num}.")
    elif num < compare:
        print(f"Luku {compare} on suurempi kuin {num}.")
    else:
        print(f"Luvut {compare} ja {num} ovat yhtäsuuria!")

    print("\nKiitos ohjelman käytöstä!")

if __name__ == '__main__':
    even_and_compare()