import os

os.chdir('13.2_textejä')

with open('1.txt') as file_1, open('2.txt') as file_2, open('3.txt') as file_3:
    #readline ja poistetaan \n merkki
    print("Tiedoston: {nimi} ensimmäinen rivi on {sisalto}".format(nimi=file_1.name, sisalto=file_1.readline().replace('\n', '')))
    #splitataan koko tiedosto rivien kohdalta ja printataan ensimmäinen, readline tapa kyllä parempi 
    print("Tiedoston: {nimi} ensimmäinen rivi on {sisalto}".format(nimi=file_2.name, sisalto=file_2.read().split('\n')[0]))
    print("Tiedoston: {nimi} ensimmäinen rivi on {sisalto}".format(nimi=file_3.name, sisalto=file_3.read().split('\n')[0]))
    
    #suljetaan tiedostot
    for fle in [file_1,file_2,file_3]:
        fle.close()

#tarkastetaan onko tiedostot kiinni
#file_1.read()

print("\nKiitos ohjelman käytöstä!")