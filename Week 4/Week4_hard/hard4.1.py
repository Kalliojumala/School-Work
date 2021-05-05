#number guessing game, a little different than the instructions :D !
import random 

number_range = input("Syötä luku alue jolla arvattavan numeron haluat olevan: ").split('-')
number = random.randint(int(number_range[0]), int(number_range[1]))
#set difficulty/decide how many guesses
guesses_total = int(input("Kuinka monta arvausta haluat? "))

while guesses_total > 0:
    print(f"\nArvauksia on jäljellä {guesses_total}")
    guess = int(input(f"Arvaa luku välillä {number_range[0]} - {number_range[1]}: "))
    if number == guess:
        print("Oikein!")
        print(f"Sinulle jäi {guesses_total} arvausta jäljelle.")
        break 
    if number < guess:
        print("Arvaus on liian suuri.")
    if number > guess:
        print("Arvaus on liian pieni.")
    guesses_total -= 1

if guesses_total > 0:
    print("\nOnneksi olkoon voitit pelin!\n")
else:
    print("\nArvaukset loppuivat :(")
    print(f"\nOikea numero oli {number}\n")

print("Kiitos ohjelman käytöstä!")