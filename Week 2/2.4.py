#prints string, with zero params prints "Ei sanottavaa"
def print_v2(string: str= "Ei sanottavaa"):
    print(string)



if __name__ == '__main__':
    #type Stop/Lopeta to break
    
    while True:
        param = input("Print: ")
        if param == 'Stop' or param == 'Lopeta':
            break
        elif param == '':
            print_v2()
        else:
            print_v2(param)
    
    