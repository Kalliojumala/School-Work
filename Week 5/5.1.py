# -----------------------------------------------------------------------------

# Takes inputs(int) and prints either their only their sum or each input individually and sum.

# Version 1.0 xd

# (C) 2020 Joel Kallio, Tampere, Suomi

# Email joel.kallio@edu.sasky.fi

# -----------------------------------------------------------------------------

#helper text
print("\nTulostetaan raporttina allekain kaikki syötetyt luvut (\"L\") tai tulostetaan VAIN lukujen summa (\"S\")")

#first loop, asks which raport type the user wants
while True:
    raport_type = input("Valitse raportti tyyppi (\"L\" tai \"S\"): ")
    if raport_type == 's' or raport_type == 'l':
        if raport_type == 'l':
            list_numbers = True
            break
        list_numbers = False
        break
    else:
        print(f"{raport_type} raporttityyppiä ei ole.")
        continue

numbers = []

print()
print("Syötä kokonaisluku lisättäväksi listaan tai \"K\" keskeytä")

#second loop for appending numbers(user input) for the raport
while True:

    user_input = input("Syötä kokonaisluku, tai \"K\": ")
    if user_input == 'k' or user_input == 'K':
        break

    try:
        numbers.append(int(user_input))
    except ValueError:
        print(f"{user_input} ei ole kokonaisluku.")

#if user chose l or long raport print each item on numbers 
if list_numbers:
    print("\nSyötetyt luvut:")
    for i in numbers:
        print(i)

print(f"\nSyötettyjen lukujen summa:\n{sum(numbers)}\n")
print("Kiitos ohjelman käytöstä!")


