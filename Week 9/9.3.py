#read color names in upper case, use read only mode

colors_list = []

with open('rainbow.txt', 'r') as colors:
    for row in colors:
        row = row.replace('\n', '')
        colors_list.append(row)
        print(row.upper())
    colors.close()

