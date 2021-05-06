#shopping list, add, remove, print and clear


def help_text():
    return """
Valitse seuraavista:
1 = Lisää tuote.
2 = Poista syötetty tuote.
3 = Tulosta lista.
4 = Tyhjennä lista.
0 = Lopetus."""

shoppinglist = []

while True:
    
    print(help_text())
    command = input("\nAnna valintasi: ")
    
    if command not in "01234":
        print("\nSyötä oikea komento! (0-4)")
        continue 
        
    if command == '0':
        print("\nKiitos ohjelman käytöstä!")
        break

    if command == '1':
        shoppinglist.append(input("Syötä lisättävä tuote: "))

    if command == '2':
        print(f"Kauppalistassa on {shoppinglist}")
        prod_to_del = input("Syötä poistettava tuote: ")
        if prod_to_del in shoppinglist:
            shoppinglist.remove(prod_to_del)
    
    if command == '3':
        print(f"Kauppalistassa on {shoppinglist}")
    
    if command == '4':
        shoppinglist = []
        print("Kauppalista on nyt tyhjä!")




