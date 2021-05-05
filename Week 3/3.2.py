from random import randint

def value_in_range(value: int):
    """Returns True if the value is between 100-1000 or >=2000

    Args:
      value: value to check
    
    Return:
        bool: Returns True if the value is between 100-1000 or >=2000, else False
    """
    if value in range (100,1001) or value >= 2000:
        return True 
    return False 



if __name__ == '__main__':
    #test the function with random numbers
    ints = [randint(50,2500) for _ in range(5)]
    for i in ints:
        print(i)
        print(value_in_range(i))