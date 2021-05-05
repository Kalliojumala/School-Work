#ask for two words, print them separately and then together
def word_play():
    print("Tämä teksti tulostuu funktiosta.\n")
    word_1 = input("Anna sana: ")
    print(f"Syötit sanan: {word_1} \n")
    word_2 = input("Anna toinen sana: ")
    print(f"Syötit sanan: {word_2}")
    print(f"Syöttämistäsi sanoista {word_1} ja {word_2} muodustuu yhdyssana:\n{word_1 + word_2}.") 









if __name__ == '__main__':
    word_play()