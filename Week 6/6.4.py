#split string, print and count words. 
#Did not bother to use slicing here, sorry!

string = "Non scholae sed vitae discimus"

#print all words separately
for word in string.split(' '):
    print(word)

#print word count
print(len(string.split()))