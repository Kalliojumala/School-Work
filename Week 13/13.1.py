#Define a function that takes even numbers in, closes on odd number input
def odd_or_not():
    user_input = input("\nInput an odd number: ")
    try:
        if int(user_input) % 2 == 0:
            print("Number is even!")
            odd_or_not()
        else:
            print(f'{user_input} is odd.')
    except ValueError:
        print("Please input a number!")
        odd_or_not()
    
    

if __name__ == '__main__':
    odd_or_not()
    print('\nThanks for using my program!')