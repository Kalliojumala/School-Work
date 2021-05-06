#list add and sort practice

list_1 = ["Harakka", "Naakka", "Punatulkku", "Joutsen", "Varis"]
list_2 = ["Jänis", "Kissa", "Koira", "Hevonen", "Susi"] 

lists = [item for item in (list_1+list_2)]

#print combined
print(lists)
#print combined alphabetically sorted
print(sorted(lists))
#print combined sorted alphabetically in reverse
print(sorted(lists, reverse=True))