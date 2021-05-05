#print every third letter and last word of str

string = "Ajattelen, siis olen!"
string_cleaned = string.replace(',','').replace('!', '').replace(' ', '')

#literal example, whitespaces and commas etc inplace
print('\n' + string[::3] + '\n')
print(string[::3][::-1] + '\n')

#whitespace/commas etc removed
print(string_cleaned[::3] + '\n')
print(string_cleaned[::3][::-1] + '\n')

#print last word
print(string.split(' ')[2].replace('!', '') + '\n')