# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# MGalloway,5.14.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
strFile = 'C:\Python\Python311\_PythonClass\Assignment05\ToDoList.txt'

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(strFile, "r")
for row in objFile:
  lstRow = row.split(",")
  dicRow = {'Task':lstRow[0],'Priority':lstRow[1].strip()}
  lstTable.append(dicRow)
  print(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print(dicRow['Task']+ ',' + dicRow['Priority'])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        print('Type in a task and assign a priority')
        strTask = (input("Enter Task:"))
        strPriority = (input("Enter a Priority:"))
        dicRow = {'Task':strTask, 'Priority':strPriority}
        lstTable.append(dicRow)
        #for dicRow in lstTable:
            #print(dicRow['Task']+ ',' + dicRow['Priority'])
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strItem = input('Which task would you like to remove?')
        for row in lstTable:
            if row['Task'].lower() == strItem.lower():
                lstTable.remove(row)
                print('row removed.')
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open('C:\Python\Python311\_PythonClass\Assignment05\ToDoList.txt', "w")
        for row in lstTable:
            objFile.write(str(row['Task'] + ',' + str(row['Priority'] + '\n')))
        print('Data saved!')
        objFile.close()
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Program closed.')
        break
        exit() # and Exit the program

