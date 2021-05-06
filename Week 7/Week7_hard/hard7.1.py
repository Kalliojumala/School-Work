

def list_modify(str_list: list, string: str):
    if string in str_list:
        str_list.remove(string)
        print(f"{string} removed from list")
        return str_list

    if len(string) == 0:
        print(f"{str_list[-1]} removed from list")
        str_list.pop(-1)
        return str_list
    
    else:
        str_list.append(string)
        return str_list

#default list 
str_list = ["Hello!"]

while True:

    if len(str_list) == 0:
        print("Bye bye!")
        break

    print(f"\nItems in list {str_list}")
    user_input = input("Input string: ")

    if user_input.lower() == 'quit':
        print("Bye bye!")
        break 
    
    list_modify(str_list, user_input)
    

