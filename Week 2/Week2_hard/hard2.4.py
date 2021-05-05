#make a palindrome
def palindrome(string: str):
    return string[::-1]




if __name__ == '__main__':
    text = input("Syötä teksti: ")
    print(f"Syöttämäsi teksti palindromina: {palindrome(text)}")