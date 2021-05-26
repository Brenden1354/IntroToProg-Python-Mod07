# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Researching and working with the Pickle and Exception Handling features
# ChangeLog (Who,When,What):
# BBritt,5.23.2021,Modified code to complete assignment 7
# BBritt,5.24.2021,Modified code to complete assignment 7
# BBritt,5.24.2021,Added comments and edited script
# ---------------------------------------------------------------------------- #

import pickle   #Import existing binary file

userID = ()
useName = ()
lstData = []

try:
    userID = input("Enter an Id: ")  # user input ID
    userName = str(input("Enter a Name: "))  # user input Name
    lstData = [userID, userName]  # list of ID and Name
    if not userID.isnumeric():
        raise Exception('ERROR: Only use numbers for the ID') #error if user enters a letter for ID
    elif userName.isnumeric():
        raise Exception('ERROR: Do not use numbers when entering a name') #error if user enters number for name
except Exception as e:
    print(e)

print(lstData)

objFile = open("AppData.dat", "ab")     #adding user input to existing binary file
pickle.dump(lstData, objFile)
objFile.close()

objFile = open("AppData.dat", "rb")     #reads binary file contents
objFileData = pickle.load(objFile)     #load() only loads one row of data.
objFile.close()
print(objFileData)
