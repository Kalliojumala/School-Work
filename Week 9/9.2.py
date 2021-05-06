#read file lines into list and close it 

cities_list = []
with open('cities.txt') as file_1:
    for row in file_1:
        row = row.replace('\n', '')
        cities_list.append(row)

    file_1.close()

#confrim file is closed
try:
    print(file_1.read())
except ValueError:
    print("File is closed!")

#print cities
print(cities_list)