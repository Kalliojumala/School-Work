#13.3
#Combine two tuples

t1 = (5,4,3)
t2= (9,2, 12)

T = t1 + t2

#print("T =",T)

#13.3.1

#checks if user input in tuple
T = (23, 45, 93, 59, 35, 58, 19, 3)

try:
    print(int(input("Anna luku: ")) in T)
except ValueError:
    pass

#13.3.2
#average of T
print(f"T:n keskiarvo: {sum(T)/len(T)}")



