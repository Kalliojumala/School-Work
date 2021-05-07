#print user data correctly formatted

#lists of data
data = [["Susanna Joki", 57394, "susjok@esimerkki.com"], ["Jukka Mäki", 48539, "jukmak@esimerkki.com"], ["Simo Holm", 58302, "simhol@esimerkki.com"],
        ["Heikki Ukkonen", 48502, "heiukk@esimerkki.com"], ["Topi Lukko", 48291, "topluk@esimerkki.com", "Taina Elo", 58201, "taielo@esimerkki.com"],
        ["Jane Eno", 48293, "janeno@esimerkki.com"], ["Joona Peso", 23945, "joopes@esimerkki.com"], ["Antton Mäki", 85823, "antmak@esimerkki.com"]]

header = ['Nimi', 'ID', 'Sähköposti']

#formatting headers 
header_format = f"\n{header[0].center(15)} || {header[1].center(10)} || {header[2].center(25)}"

#line string separates the header
line_string = len(header_format) * '='
line_string.replace('-', '|')

#print stuff out
print(header_format)
print(line_string)
for info in data:
        print(f"{info[0].center(15)} || {str(info[1]).center(10)} || {info[2].center(25)}")

print()        


