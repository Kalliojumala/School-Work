#poem scrambler, short words(<=3 letters) are lowercased and
#long words(>=7 letters) are uppercased
#print words in random order after recasing them
from random import shuffle

def word_scramble(poem):
    #create 3 lists from user input 
    user_list = sorted(poem.split(' '), key= lambda x: len(x))
    short_words = []
    long_words = []
    for word in user_list.copy():
        #append short and long words to separate lists
        if len(word) <= 3:
            short_words.append(word.lower())
            user_list.remove(word)

        if len(word) >= 7:
            long_words.append(word.upper())
            user_list.remove(word)
    
    #return the three lists combined
    return [item for item in (user_list + short_words + long_words)]

while True:
    #take user input
    poem = input("Syötä vähintään viisi sanaa sisältävä runo tai sanonta:")

    #check it is atleast 5 words long, re-ask input if its invalid
    if len(poem.split(' ')) < 5:
        print("\nSyötä vähintään viisi sanaa!\n")
        continue
    
    #apply the function on the input and shuffle the returned list
    ready_list = word_scramble(poem)
    shuffle(ready_list)

    #print the list as a string and exit
    print(" ".join(ready_list))
    break

print("Kiitos ohjelman käytöstä!\n")

