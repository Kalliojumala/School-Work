#even or odd number

def even_or_odd(num: int):
    return num % 2 == 0



if __name__ == '__main__':
    num = int(input("Syötä kokonaisluku: "))
    print()
    if even_or_odd(num):
        print("Syöttämäsi luku on parillinen.\n")
    else:
        print("Syöttämäsi luku on pariton.\n")
    print("Kiitos ohjelman käytöstä!")
