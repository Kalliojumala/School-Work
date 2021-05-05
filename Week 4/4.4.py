#Ask user for inputs(int) return mean
def nouda_arvosana():
    arvosanat = []
    syotteiden_maara = int(input("\nAnna syötettävien arvosanojen määrä: "))
    for i in range(syotteiden_maara):
        arvosanat.append(int(input(f"\nSyötä arvosana({i+1}.): ")))
    return sum(arvosanat) / len(arvosanat)




if __name__ == '__main__':
    keski_arvo = nouda_arvosana()
    print(f"\nSyötettyjen arvosanojen keskiarvo on: {keski_arvo}")
    print("\nKiitos ohjelman käytöstä!")