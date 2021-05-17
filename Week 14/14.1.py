import sys

#arguments
args = sys.argv[1:]

#int args, the list only accepts numbers and rejects strings etc.
int_args = []
for i in range(len(args)):
    try:
        int_args.append(int(args[i]))
    except ValueError:
        pass

#str conversion for cleaner format ('join')
str_args = [str(arg) for arg in sorted(int_args)]
#print
print(f"Numbers in order are: {' '.join(str_args)}")

#write line to a file
with open('jarjestety_luvut.txt', 'a') as file_1:
    file_1.write(f"{' '.join(str_args)}\n")

print("Thank you for using my program! :D")

