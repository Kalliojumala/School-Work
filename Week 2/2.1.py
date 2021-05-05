#function takes in a string, converts the first letter to UPPER and prints it
def upper_first_letter(string: str):
    return_string = []
    words = string.split(' ')
    for i in words:
        return_string.append(f"{i[0].upper()+i[1:]}")
    print(" ".join(return_string))   
    
    




if __name__ == '__main__':
    arg_string = input('String to convert: ')
    upper_first_letter(arg_string)