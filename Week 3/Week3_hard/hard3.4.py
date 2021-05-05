#Calculate BMI
def calculate_bmi(weight: int, height: float):
    #weight in kilograms, height in centimeters!!!
    return weight / ((height/100)**2)

def print_bmi(bmi: float):
    #print which bmi category parameter 'bmi' falls into
    if bmi < 18.5:
        print(f"{bmi:.2f} : Painoindeksi erittäin alhainen!")
    elif bmi < 25:
        print(f"{bmi:.2f} : Normaali painoindeksi.")
    elif bmi < 30:
        print(f"{bmi:.2f} : Ylipaino eli lievä lihavuus.")
    elif bmi < 35:
        print(f"{bmi:.2f} : Merkittävä lihavuus.")
    elif bmi < 40:
        print(f"{bmi:.2f} : Vaikea lihavuus.")
    else:
        print(f"{bmi:.2f} : Sairaalloinen lihavuus.")


if __name__ == '__main__':
    x = calculate_bmi(80, 175)
    print_bmi(x)