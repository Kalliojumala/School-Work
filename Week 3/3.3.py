
def sum_three(a: int, b: int, c: int):
    """Sums 3 integers, multiplies the sum by three if all 3 numbers are the same.

    Args:
      a: int/float
      b: int/float
      c: int/float
    
    Returns:
      int/float: sum of abc or sum of abc * 3
    """
    if a == b == c:
        return (a + b + c) * 3
    return a + b + c


if __name__ == '__main__':
    a, b, c = input("Enter 3 integers separated by space: ").split(" ")
    print(sum_three(int(a), int(b), int(c)))
    print("Thanks for using my program!")