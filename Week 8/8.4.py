from functools import reduce

#join and casting prac

#long str
string = "01234567890123456789"

#cast as list
string_list = list(string)

#one liner to get list sum instead of for loop
list_sum = reduce(lambda x, y: int(x) + int(y), string_list)

#join it with '+' and print it with list_sum
print(f"\n{'+'.join(string_list)}={list_sum}\n")
print("Kiitos ohjelman käytöstä!")


