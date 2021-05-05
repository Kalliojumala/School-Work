#Ask user for 5 inputs(int) return mean of those values 

def nouda_arvosana():
    arvosanat = []
    print("\nSyötä viisi arvosanaa, yksi kerralla.")
    for i in range(5):
        arvosanat.append(int(input("\nSyötä arvosana: ")))
    return sum(arvosanat) / len(arvosanat)




if __name__ == '__main__':
    keski_arvo = nouda_arvosana()
    print(f"\nSyötettyjen arvosanojen keskiarvo on: {keski_arvo}")
    print("\nKiitos ohjelman käytöstä!")