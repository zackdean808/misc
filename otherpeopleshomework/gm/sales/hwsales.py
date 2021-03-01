#!/bin/python 
import os, sys
import getpass 

#Problem: Write a program that will accept the names of sales staff and their weekly sales 
# for four weeks. Display their total sales, total commissions, persons who made more than $15000.00 
# and highest and lowest commission.
# Output: This program is used to calculates the commissions of 5 sales staff on our team.

choiceValue = -1 
username = ""
password = ""
userLoggedInStatus = True
# First Names 
spFirstName1 = ""
spFirstName2 = ""
spFirstName3 = ""
spFirstName4 = ""
spFirstName5 = ""
# Last Names 
spLastName1 = ""
spLastName2 = ""
spLastName3 = ""
spLastName4 = ""
spLastName5 = ""
# sales person (sp) 1 sales 
sp1Week1Sales = 0.00
sp1Week2Sales = 0.00
sp1Week3Sales = 0.00
sp1Week4Sales = 0.00
# sales person (sp) 2 sales 
sp2Week1Sales = 0.00
sp2Week2Sales = 0.00
sp2Week3Sales = 0.00
sp2Week4Sales = 0.00
# sales person (sp) 3 sales 
sp3Week1Sales = 0.00
sp3Week2Sales = 0.00
sp3Week3Sales = 0.00
sp3Week4Sales = 0.00
# sales person (sp) 4 sales 
sp4Week1Sales = 0.00
sp4Week2Sales = 0.00
sp4Week3Sales = 0.00
sp4Week4Sales = 0.00
# sales person (sp) 5 sales 
sp5Week1Sales = 0.00
sp5Week2Sales = 0.00
sp5Week3Sales = 0.00
sp5Week4Sales = 0.00
# sales person (sp) commisions  
sp1Commission = 0.00
sp2Commission = 0.00
sp3Commission = 0.00
sp4Commission = 0.00
sp5Commission = 0.00
# sales person (sp) commisions
sp1Avg = 0.00
sp2Avg = 0.00
sp3Avg = 0.00
sp4Avg = 0.00
sp5Avg = 0.00

def registerNewUser():
    print ("New User")
    username = str(input("Please enter a username: ")) 
    password = getpass.getpass("Please enter a password:")
    userLoggedInStatus = True
        
def addSalesPerson():
    if userLoggedInStatus == False: 
        registerNewUser()
    if choiceValue == 2:
        spFirstName1 = str(input("Please enter a first name for sp1: ")) 
        spLastName1 = str(input("Please enter a last name for sp1: "))
        salesCommision()
    elif choiceValue == 3:
        spFirstNam2 = str(input("Please enter a first name for sp2: "))
        spLastName2 = str(input("Please enter a last name for sp12 "))
        salesCommision()
    elif choiceValue == 4:
        spFirstName3 = str(input("Please enter a first name for sp3: "))
        spLastName3 = str(input("Please enter a last name for sp3: "))
        salesCommision()
    elif choiceValue == 5:
        spFirstName4 = str(input("Please enter a first name for sp4: "))
        spLastName4 = str(input("Please enter a last name for sp4: "))
        salesCommision()
    elif choiceValue == 6:
        spFirstName5 = str(input("Please enter a first name for sp5: "))
        spLastName5 = str(input("Please enter a last name for sp5: "))
        salesCommision()
    else:
        print ("Something Went Wrong") 

def salesCommision():
    #print("Sales Commision")
    if choiceValue == 2:
	    sp1Week1Sales = float(input("Please enter a week 1 commission: "))
	    sp1Week2Sales = float(input("Please enter a week 2 commission: "))
	    sp1Week3Sales = float(input("Please enter a week 3 commission: "))
	    sp1Week4Sales = float(input("Please enter a week 4 commission: "))
    elif choiceValue == 3:
        sp2Week1Sales = float(input("Please enter a week 1 commission: "))
        sp2Week2Sales = float(input("Please enter a week 2 commission: "))
        sp2Week3Sales = float(input("Please enter a week 3 commission: "))
        sp2Week4Sales = float(input("Please enter a week 4 commission: "))
    elif choiceValue == 4:
	    sp3Week1Sales = float(input("Please enter a week 1 commission: "))
	    sp3Week2Sales = float(input("Please enter a week 2 commission: "))
	    sp3Week3Sales = float(input("Please enter a week 3 commission: "))
	    sp3Week4Sales = float(input("Please enter a week 4 commission: "))
    elif choiceValue == 5:
	    sp4Week1Sales = float(input("Please enter a week 1 commission: "))
	    sp4Week2Sales = float(input("Please enter a week 2 commission: "))
	    sp4Week3Sales = float(input("Please enter a week 3 commission: "))
	    sp4Week4Sales = float(input("Please enter a week 4 commission: "))
    elif choiceValue == 6:
	    sp5Week1Sales = float(input("Please enter a week 1 commission: "))
	    sp5Week2Sales = float(input("Please enter a week 2 commission: "))
	    sp5Week3Sales = float(input("Please enter a week 3 commission: "))
	    sp5Week4Sales = float(input("Please enter a week 4 commission: "))
    else:
        print ("Something Went Wrong") 

def salesAverage():
    if choiceValue == 2:
        sp1Avg = (sp1Week1Sales + sp1Week1Sales + sp1Week1Sales + sp1Week1Sales)/4
    elif choiceValue == 3:
        sp2Avg = (sp2Week2Sales + sp2Week1Sales + sp12Week1Sales + sp2Week1Sales)/4
    elif choiceValue == 4:
        sp3Avg = (sp3Week1Sales + sp3Week1Sales + sp3Week1Sales + sp3Week1Sales)/4
    elif choiceValue == 5:
        sp4Avg = (sp4Week1Sales + sp4Week1Sales + sp4Week1Sales + sp4Week1Sales)/4
    elif choiceValue == 6:
        sp5Avg = (sp5Week1Sales + sp5Week1Sales + sp5Week1Sales + sp5Week1Sales)/4
    else:
        print ("Something Went Wrong")

def sp1CalculateCommission():
    sp1Commission = (sp1Week1Sales + sp1Week2Sales + sp1Week3Sales + sp1Week4Sales)
    if sp1Commission > 14999: 
        sp1Commission *= .06
    elif sp1Commission > 9999 and sp1Commission <= 14999: 
        sp1Commission *= .05
    elif sp1Commission > 4999 and sp1Commission <= 9999:
        sp1Commission *= .04
    elif sp1Commission <= 4999:
        sp1Commission *= .03
    else:
        print ("something went wrong")

def sp2CalculateCommission():
    sp2Commission = (sp2Week1Sales + sp2Week2Sales + sp2Week3Sales + sp2Week4Sales)
    if sp2Commission > 14999:
        sp2Commission *= .06
    elif sp2Commission > 9999 and sp2Commission <= 14999:
        sp2Commission *= .05
    elif sp2Commission > 4999 and sp2Commission <= 9999:
        sp2Commission *= .04
    elif sp2Commission <= 4999:
        sp2Commission *= .03
    else:
        print ("something went wrong")

def sp3CalculateCommission():
    sp3Commission = (sp3Week1Sales + sp3Week1Sales + sp3Week3Sales + sp3Weekr4Sales)
    if sp3Commission > 14999:
        sp3Commission *= .06
    elif sp3Commission > 9999 and sp3Commission <= 14999:
        sp3Commission *= .05
    elif sp3Commission > 4999 and sp3Commission  <= 9999:
        sp3Commission *= .04
    elif sp3Commission <= 4999:
        sp3Commission *= .03
    else:
        print ("something went wrong")

def sp4CalculateCommission():
    sp4Commission = (sp4Week1Sales + sp4Week2Sales + sp4Week5Sales + sp4Week4Sales)
    if sp4Commission > 14999:
        sp4Commission *= .06
    elif sp4Commission > 9999 and sp4Commission <= 14999:
        sp4Commission *= .05
    elif sp4Commission > 4999 and sp4Commission <= 9999:
        sp4Commission *= .04
    elif sp4Commission <= 4999:
        sp4Commission *= .03
    else:
        print ("something went wrong")

def sp5CalculateCommission():
    sp5Commission = (sp5Week1Sales + sp5Week2Sales + sp5Week3Sales + sp5Week4Sales)
    if sp5Commission > 14999:
        sp5Commission *= .06
    elif sp5Commission > 9999 and sp5Commission <= 14999:
        sp5Commission *= .05
    elif sp5Commission > 4999 and sp5Commission  <= 9999:
        sp5Commission *= .04
    elif sp5Commission <= 4999:
        sp5Commission *= .03
    else:
        print ("something went wrong")

def printCommisions():
    print ("Sales Person 1: " + spFirstName1 + " " + spLastName1)
    print ("SP1 Commission: " + str(sp1Commission))
    print ("Sales Person 2: " + spFirstName2 + " " + spLastName2)
    print ("SP2 Commission: " + str(sp2Commission))
    print ("Sales Person 3: " + spFirstName3 + " " + spLastName3)
    print ("SP3 Commission: " + str(sp3Commission))
    print ("Sales Person 4: " + spFirstName4 + " " + spLastName4)
    print ("SP4 Commission: " + str(sp4Commission))
    print ("Sales Person 5: " + spFirstName5 + " " + spLastName5)
    print ("SP5 Commission: " + str(sp5Commission))

    #
    # Gareth, sort goes here. I'd just use sorted() but that's me. 
    #
    comList = (float(sp1Commission), float(sp2Commission), float(sp3Commission), float(sp4Commission), float(sp5Commission))
    print ("The max commission is: " + max(comList))

while choiceValue != 0:
    print ("Please select an option from the menu below:")
    print ("1. Register new user")
    print ("2. Register first sales person")
    print ("3. Register second sales person")
    print ("4. Register third sales person")
    print ("5. Register fourth sales person")
    print ("6. Register fifth sales person")
    print ("7. Calculate the commissions") 
    print ("8. Display the highest Commission") 
    print ("0. Exit the application") 
    choiceValue = int(input("Please enter a choice from the following: "))
    if choiceValue == 1:
        registerNewUser()
    elif choiceValue == 2:
        addSalesPerson()
    elif choiceValue == 3:
        addSalesPerson()
    elif choiceValue == 4:
        addSalesPerson()
    elif choiceValue == 5:
        addSalesPerson()
    elif choiceValue == 6:
        addSalesPerson()
    elif choiceValue == 7: 
        sp1CalculateCommission()
        sp2CalculateCommission()
        sp3CalculateCommission()
        sp4CalculateCommission()
        sp5CalculateCommission()
    elif choiceValue == 8: 
        printCommisions()
    else:
        print ("Something Went Wrong") 


