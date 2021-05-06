#ask for birthdays, append them to a list
bdays = []

while True:
    bday = input("Syötä syntymäpäivä: ")
    if bday == 'l':
        break
    bdays.append(bday)

print("Syötit seuraavat syntymäpäivät:")
print(bdays)
print("Kiitos ohjelman käytöstä!")