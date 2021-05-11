#Dict prac

#make a dict
groceries_dict = {'Bread':2.26,'Oatmilk':3.62,'Chocolate':1.59}

#print items(keys) in the dict
print('Items in stock:')

for item in groceries_dict.keys():
    print(item)

#ask for user which item to change
item_to_change = input("Name of product to be assigned a new price: ")

#check if item in list
if item_to_change not in groceries_dict.keys():
    print(f'{item_to_change} not in stock!')

#if true ask for new price for 'item_to_change
else:
    try:
        #check that the price is a number
        groceries_dict[item_to_change] = float(input('New price: '))
        print(f"New price of {item_to_change} is {groceries_dict[item_to_change]}.")
    except ValueError:
        print('New price invalid.')

print("Thanks for using the program!")
