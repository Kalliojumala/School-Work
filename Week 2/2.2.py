#function takes in a string, converts the first letter to UPPER and returns it
def upper_first_letter(string: str):
    return_string = []
    words = string.split(' ')
    for i in words:
        return_string.append(f"{i[0].upper()+i[1:]}")
    return " ".join(return_string)
    
    




if __name__ == '__main__':
    #ask for three strings to convert, print them after each input
    """
    for i in range(3):
        arg_string = input('String to convert: ')
        message = upper_first_letter(arg_string)
        print(message)
    """
    #OR 3 messages printed at once
    arg_list = []
    for i in range(3):
        arg_list.append(upper_first_letter(input('String to convert: ')))
    
    print("\n".join(arg_list))