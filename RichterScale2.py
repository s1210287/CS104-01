#version 2

name = input("Enter your first and last name: ")
ID = int(input("Enter your ID number: "))

#end = float(input('Enter the Richter scale value or -99 to end: '))
#if end == -99:
    #exit(0)

yes = False
while not yes:
    richter = float(input("Enter the Richter scale value or -99 to end: "))
    if richter >= 8.0:
        print ("Most structures fall")
    elif richter >= 7.0:
        print("Many buildings destroyed")
    elif richter >= 6.0:
        print("Many buildings considerably damaged, some collape")
    elif richter >= 4.5:
        print("Damage to poorly constructed buildings")
    elif richter >= 0.0:
        print("No destruction of buildings")
    else:
        print("Value must be greater than 0")

    if richter == -99:
        exit(0)
            
            

