#Sum/Average Program
#Your first and last name:
#Your student ID:

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
#Instead of searching for a name in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

name = input("Enter your first and last name: ")
ID = int(input("Enter yor ID number: "))

numberList = []
sumInt = 0
avgInt = 0.0

for x in range(0,20):
    numberList.append (int(input("Enter a number:")))

for x in range (0,20):
    sumInt += numberList[x]
    
avgInt = sumInt/20

print("The sum of the numbers you entered is ", sumInt)
print("The average of the numbers you entered is ", avgInt)
