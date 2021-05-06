#write to dog names to a file, then read it after

koirat = ['Mäyräkoira','Lammaskoira','Noutaja','Beagle']
dogs_final = []

#write 4 dog breeds to file
with open('koirat.txt', 'w') as dogs:
    for dog in koirat:
        dogs.write(f"{dog}\n")
    dogs.close()

with open('koirat.txt') as dogs:
    for row in dogs:
        row = row.replace('\n', '')
        print(row)
    dogs.close()

with open('koirat.txt', 'a') as dogs:
    dogs.write('Gorgi')
    dogs.close()

with open('koirat.txt') as dogs:
    print()
    for row in dogs:
        row = row.replace('\n', '')
        dogs_final.append(row)
    dogs.close()

print(dogs_final)