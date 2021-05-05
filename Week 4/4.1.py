#number guessing game, a little different than the instructions :D !
import random 

number = random.randint(1,100)
#set difficulty/decide how many guesses
guesses_total = int(input("\nKuinka monta arvausta haluat? "))

while guesses_total > 0:
    guess = int(input("\nArvaa luku välillä 1 - 100: "))
    if number == guess:
        print("\nOikein!")
        break 
    if number < guess:
        print("\nArvaus on liian suuri.")
    if number > guess:
        print("\nArvaus on liian pieni.")
    guesses_total -= 1

if guesses_total > 0:
    print("\nOnneksi olkoon voitit pelin!\n")
else:
    print(f"\nOikea numero oli {number}\n")

print("Kiitos ohjelman käytöstä!")
