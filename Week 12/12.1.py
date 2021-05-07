#BMI Mission (again...)


def bmi_calc():
    """Calculates BMI using height and weight

    Returns:
      float: bmi calculated on user input height(cm), weight(kg)
    """
    weight = int(input("\nSyötä paino (kiloissa): "))
    height = int(input("Syötä pituus (senttimetreissä): "))

    return round(weight / ((height/100)**2), ndigits=1)

def bmi_range(bmi_calc):
    """Assign bmi value to correct category

    Args:
      bmi_calc: float, standard range 16-40+. Failsafe for unusually large numbers.
    
    Returns:
      tuple: given bmi value(float), category
    """    
    ranges = {16:'Vaikea alipaino', 17:'Merkittävä alipaino', 18.5:'Lievä alipaino',
              25:'Normaali paino', 30: 'Lievä ylipaino', 35: 'Merkittävä ylipaino', 40: 'Vaikeaylipaino', bmi_calc**2: 'Sairaalloinen ylipaino'}

    for keys,values in ranges.items():
        if bmi_calc < keys:
            return bmi_calc,values

    
if __name__ == '__main__':
    index = bmi_range(bmi_calc())
    print(f"\nPaino indeksi on {index[0]} > {index[1]}.\n")
    print("Thanks for using the app! :D")