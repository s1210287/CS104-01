#List creation and searching

    
names  = []
for x in range(0,10):
    aName = input("Enter a name to search for:")
    names.append(aName)

end = input('Type End to end the program: ')
if end == 'End':
    exit(0)

print(names)
endChoice = False
while not endChoice:
    search = input("Enter a search name:")

    if search in names:
        print(search, "was found")
    else:
        print (search, "was not found")
    
    if search == 'End':
        exit(0)


    
#make this repeat









