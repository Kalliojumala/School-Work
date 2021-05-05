#ask for user age, print a message based on var

#strings to print
under_12 = "Olet vielä lapsi"
under_18 = "Olet nuori"
over_18 = "Olet aikuinen"

age = int(input("Kuinka vanha olet?\n"))

if age < 12:
    print(under_12)
elif age < 18:
    print(under_18)
else:
    print(over_18)