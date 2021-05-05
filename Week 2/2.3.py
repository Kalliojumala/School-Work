#func takes in str and two ints, converts str to int and sums all args
def str_to_int(string: str, int_1: int=5, int_2: int=10):
    return int(string) + int_1 + int_2



if __name__ == '__main__':
    age_random_sum = str_to_int(input('Enter age: '))
    print(age_random_sum)