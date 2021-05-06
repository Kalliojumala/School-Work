from math import gcd

#example for greatest common divisor
#print(gcd(16,28)) == 4

num1 = int(input("Syötä luku 1: "))
num2 = int(input("Syötä luku 2: "))

print(f"Lukujen {num1} ja {num2} suurin mahdollinen jakaja on: {gcd(num1,num2)}")