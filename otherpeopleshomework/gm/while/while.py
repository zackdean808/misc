#!/usr/bin/python
import os, sys

sixc = 0 
fivec = 0 
threec = 0 
count = 0 
num = -1 

while num != 0:
    num = int(input("Please enter a number between 0 and 7: "))
    if num < 0 or num > 7:
        print ("Not in range, Please enter a number between 0 and 7.")    
    if num > 0 or num < 7:
        if num == 6:
            sixc += 1
        elif num == 5:
            fivec += 1
        elif num == 3:
            threec += 1
        elif num == 0:
            num = 0 
        else:
            print ("Not counting, not a 3, 5, or 6")
            num = -1
    

print ("Number of 6's entered: " + str(sixc))
print ("Number of 5's entered: " + str(fivec))
print ("Number of 3's entered: " + str(threec))

