#prints string 'n' times
def print_n_times(string:str, n:int=1):
    for i in range(n):
        print(string)



if __name__ == '__main__':
    string = input("Syötä sana: ")
    times = int(input(f"Kuinka monta kertaa {string} tulostetaan: "))
    print_n_times(string, times)
