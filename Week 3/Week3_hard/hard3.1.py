#simple calculator, ask for 2 numbers and operator and print answer

try:
    luku1 = int(input("Syötä ensimmäinen luku: "))
    print()
    luku2 = int(input("Syötä toinen luku: "))
    print()
    operator = int(input("Mitä luvuille tehdään? (1=lisäys, 2=vähennys, 3=kerto, 4=jako): "))
    print()
except ValueError:
    print("Tarkistathan että syötteet ovat lukuja!")

if operator == 1:
    print(f"Luku: {luku1} lisättynä lukuun: {luku2} = {luku1+luku2}")
if operator == 2:
    print(f"Luku: {luku1} vähennettynä luvulla: {luku2} = {luku1-luku2}")
if operator == 3:
    print(f"Luku: {luku1} kertaa luku: {luku2} = {luku1*luku2}")
if operator == 4:
    print(f"Luku: {luku1} jaettuna luvulla: {luku2} = {luku1/luku2}")

print()
print("Kiitos ohjelman käytöstä!")


