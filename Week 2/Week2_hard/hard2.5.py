#find out if the string is a palindrome, return bool
"""
def is_palindrome(string: str):
    if string != string[::-1]:
        return False
    return True
"""
#same but with print commands
def is_palindrome(string: str):
    if string != string[::-1]:
        print(f"Syötit seuraavan palindromin: {string} joka on käännettynä {string[::-1]}.")
        print("Sana ei ole palindromi.")
    else:
        print(f"Syötit seuraavan palindromin: {string} joka on käännettynä {string[::-1]}.")
        print("Sana on palindromi!")




if __name__ == '__main__':
    word = input("Syötä palindromi: ")
    is_palindrome(word)
