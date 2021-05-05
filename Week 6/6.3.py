#len and indexing practice

string = "Hyvä koodi on kuin runo."

#print string length using len()
print(len(string))

#print the string on lines, cut in the middle
print(f"\n{string[:12]}\n{string[12:]}\n")

#print index of first letter of word "kuin"
print(string.find("ku"))
