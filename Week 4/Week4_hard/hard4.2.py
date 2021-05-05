#palindrome 2.0
#takes user input(str), then prints it(1) or prints it in reverse(2), (0) for quit

#default word, if user chooses option 2 or 3 before entering a word
word = 'tissit'
choices = [1,2,3,0]
while True:
    x = """
Voit valita seuraavista vaihtoehdoista:
1) Syötä sana
2) Tulosta sana vasemmalta oikealle ja ylhäältä alas
3) Tulosta sana oikealta vasemmalle ja alhaalta ylös
0) Lopeta"""
    
    print(x)
    command = int(input("Valinta: "))
    if command == 1:
        word = input("Anna sana: ")

    if command == 2:
        print(word)
        for i in word[1:]:
            print(i)

    if command == 3:
        reverse = word[::-1]
        print(reverse)
        for i in reverse[1:]:
            print(i)

    if command == 0:
        print("Kiitos ohjelman käytöstä!")
        break

    elif command not in choices:
        print("Valintaa ei tunnistettu!")    
    