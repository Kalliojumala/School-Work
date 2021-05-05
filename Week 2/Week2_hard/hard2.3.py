#compares ints and prints out which is larger
def compare(num_1: int, num_2:int):
    if num_1 > num_2:
        print(f"Luku {num_1} on suurempi kuin luku {num_2}.")
    elif num_1 < num_2:
        print(f"Luku {num_2} on suurempi kuin luku {num_1}.")
    else:
        print(f"Syötetyt luvut {num_2} ja {num_1} ovat samansuuruiset.")



if __name__ == '__main__':
    #ask for two integers, then compare them printing out the result
    num_1 = int(input("Syötä ensimmäinen luku: "))
    print()
    num_2 = int(input("Syötä toinen luku: "))
    print()
    compare(num_1, num_2)
