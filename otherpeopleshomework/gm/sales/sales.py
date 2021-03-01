#!/bin/python
import os, sys, getpass

firstName = ""
lastName = ""
weekOneSales = 0.00
weekTwoSales = 0.00
weekThreeSales = 0.00
weekFourSales = 0.00
salesTotal = 0.00
userLoggedInStatus = True
choiceValue = -1
S = []

# For testing the application
S.append(["z", "d", 10, 20, 30, 40])
S.append(["g", "m", 1000, 20, 4000, 5000])


"""
for i in S:
    print ("main array") 
    for j in i:
        print ("Inner: " + str(j)) 
        print ("Inner is digit: " + str(j.isdigit()))
"""        

#num = int(input("Please enter a number between 0 and 7: "))

def registerNewUser():
    print ("New User")
    username = str(input("Please enter a username: "))
    password = getpass.getpass("Please enter a password:")
    userLoggedInStatus = True

def addSalesPerson():
    fname = str(input("Please enter a first name: "))
    lname = str(input("Please enter a last name: ")) 
    weekOneSales = float(input("Please enter week one sales: ")) 
    weekTwoSales = float(input("Please enter week two sales: "))
    weekThreeSales = float(input("Please enter week three sales: "))
    weekFourSales = float(input("Please enter week four sales: "))
    S.append([fname, lname, weekOneSales, weekTwoSales, weekThreeSales, weekFourSales])

def calculateCommission():
    tempTotal = 0.00
    countOuter = 0
    for person in S:
        print ("Printing Sales list: " + str(S))
        tempTotal = 0.00
        salesTotal = 0.00
        for value in person:
            try:
                flt_value = float(value)
            except ValueError:
                pass
            else:
                tempTotal += value
        commTotal = tempTotal * calculateCommPercentage(tempTotal)
        S[countOuter].append(commTotal)
        print ("Total w/o Com: " + str(tempTotal))
        print ("Comm Total: " + str(commTotal))
        salesTotal = commTotal + tempTotal
        print ("Sales + Comm Total: " + str(salesTotal))
        S[countOuter].append(salesTotal)
        countOuter += 1


def calculateCommPercentage(totalComm): 
    commPercent = 0
    if totalComm> 14999:
        commPercent = .06
    elif totalComm > 9999 and totalComm <= 14999:
        commPercent = .05
    elif totalComm > 4999 and totalComm  <= 9999:
        commPercent = .04
    elif totalComm <= 4999:
        commPercent = .03
    else:
        print ("something went wrong")
        
    return commPercent 

def printCommisions():
    
    t = [] 
    t = S

    t.sort(key = lambda x: x[6])
    t.reverse()

    for temp in t:
        print (temp)


while choiceValue != 0:
    print ("Please select an option from the menu below:")
    print ("\t1. Register new administrator")
    print ("\t2. Register a sales person")
    print ("\t3. Calculate the commissions")
    print ("\t4. Display the highest Commission")
    print ("\t0. Exit the application")
    choiceValue = int(input("Please enter a choice from the following: "))
    if choiceValue == 1:
        registerNewUser()
    elif choiceValue == 2:
        addSalesPerson()
    elif choiceValue == 3:
        calculateCommission()
    elif choiceValue == 4:
        printCommisions()
    elif choiceValue == 0:
        print ("Exiting") 
    else:
        print ("Something Went Wrong") 

