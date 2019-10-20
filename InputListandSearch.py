#List creation and searching

    
names  = []
for x in range(0,10):
    aName = input("enter first name:")
    names.append(aName)

end = input('type End to quit: ')
if end == 'End':
    exit(0)

print(names)
endChoice = False
while not endChoice:
    search = input("enter search name:")

    if search in names:
        print(search, "was found")
    else:
        print (search, "was not found")
    
    if search == 'End':
        exit(0)


    
#make this repeat









