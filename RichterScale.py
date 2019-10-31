#version 1
name = input("Enter your first and last name: ")
ID = int(input("Enter your ID number: "))

richter = float(input("Please enter richter value: "))
if richter >= 8.0:
    print ("Most structures fall")
elif richter >= 7.0:
    print("Many buildings destroyed")
elif richter >= 6.0:
    print("Many buildings considerably damaged, some collape")
elif richter >= 4.5:
    print("Damage to poorly constructed buildings")
else:
    print("No destruction of buildings")
