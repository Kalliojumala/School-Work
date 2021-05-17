def USD2EUR(usd: float):
    """Converts given USD amount to EUR, multiplier 0.831467

    Args:
      usd: float amount of US dollars

    Returns:
      float: EUR value of given dollars
    """
    return usd * 0.831467

def USD2GBP(usd: float):
    """Converts given USD amount to GBP, multiplier 0.739472

    Args:
      usd: float amount of US dollars

    Returns:
      float: Great Britain Pound(GBP) value of given dollars
    """
    return usd * 0.739472

def USD2JPY(usd: float):
    """Converts given USD amount to JPY, multiplier 112.656

    Args:
      usd: float amount of US dollars

    Returns:
      float: Japan Yen value of given dollars
    """
    return usd * 112.656

def main():
    """Main function, converts user input(float) to EUR,GBP and JPY

    Print:
      prints formatted string of USD -> EUR, GBP and JPY.
    
    Return:
      None
    """
    try:
        amount = float(input("Amount of dollars: "))
    except ValueError:
        print("Please input a number...")

    eur = USD2EUR(amount)
    gbp = USD2GBP(amount)
    jpy = USD2JPY(amount)

    print(f"{amount} USD = {eur:.2f} EUR, {gbp:.2f} GBP, {jpy:.2f} JPY.")


if __name__ == '__main__':
    main()