#ask for name and age, verify its a number and print message
name = input('Mikä on nimesi? ')

try:
    age = int(input('Kuinka vanha olet? '))
    print(f"Ajattele {name.upper()}! Vuonna 2040 olet jo {age + 20} vuotta vanha.")
except ValueError:
    print("Ole ystävällinen ja anna ikäsi numeroina.")