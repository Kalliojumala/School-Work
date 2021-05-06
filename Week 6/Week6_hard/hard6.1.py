#program asks for a string(command 1), then a range from the alphabet(command 2)
#command 3 prints out words from the string if they start with a letter in the chosen alphabet range

import string
#setup default values so user can input any command at any time
abc = string.ascii_lowercase + 'åäö'
user_words = ['Hello', 'from', 'the', 'otherside!']
index_start, index_end = 0, 5

#display commands print
def help_text():
    return """
Valitse seuraavasta:
1 = Syötävirke
2 = Kirjainalue, jolta sanat tulostetaan
3 = Tulosta sanat
0 = Lopeta"""

#function asks for letter range, returns start and end index to loop
def get_range():
    try:
        start, end = input("\nAnna kirjainalue, jolta väliltä virkkeen sanat tulostetaan: ").split('-')
        index_start = abc.find(start)
        index_end = abc.find(end)
        return index_start, index_end
    except ValueError:
        print("Syötä kirjain väli muodossa a-b!")
        return "ab"

def return_matches(user_words: list, abc_range: str):
    """Compares list items to given alphabet range 

    Args:
      user_words: list containing str item for comparison
      abc_range: expected indexed string of ascii_letters, can use custom str

    Returns:
      list: list of words that have a matching start letter to given alphabet range
    """
    any_words = False
    matches = []
    for word in user_words:
            if word[0].lower() in abc_range:
                matches.append(word.replace('.', '').replace(',', '').replace('!', ''))
                any_words = True
    return matches

#main loop 
while True:

    print(help_text())
    command = input("Valintasi: ")

    if command == '1':
        user_words = input("Syötä virke: ").split(' ')

    if command == '2':
        try:
            index_start, index_end = get_range()
        except ValueError:
            continue

    if command == '3':
        abc_range = abc[index_start:index_end+1]
        print(f"\nVirkkeessä oli kirjaimilla {abc[index_start]}-{abc[index_end]} alkavia sanoja seuraavat: ")

        matches = return_matches(user_words, abc_range)
        print(f"\"{', '.join(matches)}\"")

        if len(matches) == 0:
            print("Ei yhtään sanaa halutulla kirjain välillä!")

    if command == '0':
        break

print("\nKiitos ohjelman käytöstä!")