
def USD2EUR(maara):
    """
    Muunna maara US Dollareita Euroihin.
    Käytä: 1 USD = 0.831467 EUR

    argumentit:
        maara: US dollarimäärä (float)

    palauttaa:
        muunnettu_arvo: oikea määrä euroja (float)
    """

    return maara * 0.831467



def EUR2GBP(maara):
    """
    Muunna Euroista Puntiin.
    Käytä: 1 EUR = 0.889358 GBP

    argumentit:
        maara: Euromäärä (float)

    palauttaa:
        muunnettu_arvo: oikea määrä Puntina (float)
    """

    return maara * 0.889358

 

def USD2GBP(maara):
    """
    Muunna US Dollareista Puntiin.

    argumentit:
        maara: US dollarimäärä (float)

    palauttaa:
        muunnettu_arvo: oikea määrä Puntina (float)
    """

    return EUR2GBP(USD2EUR(maara))

 

def paaohjelma():

    maara = float(input("Syötä dollarit USD: $"))

    # Punniksi
    gbp = USD2GBP(maara)

    print("${:.2f} USD = {:.2f} GBP".format(maara, gbp))

if __name__ == '__main__':

    paaohjelma()
    

