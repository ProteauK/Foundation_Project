import pymongo
import json
import os
import collections

#Connect to the Server.
client = pymongo.MongoClient('localhost:27017')

#Created variable pointing to Database called mydb
mydb = client.EmployeeDB
Collection = mydb.Employees
Ccollection = mydb.Customers
Scollection = mydb.Sales

#creating function to clear terminal screen using os driver
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    return("   ")

#define main menu with options for user to choose from
def main():
    while(True):
        options = input("\n1: Insert\n2: Update\n3: Read\n4: Delete\n5: Import DB from JSON file\nx: Exit Application\n\nWating For User Input: ")
        
        if options == "1":
            insert() 
        elif options == '2':
            update()
        elif options == '3':
            read()
        elif options == '4':
            delete()
        elif options == '5':
            port()
        elif options == 'x':
            print('\nGoodBye ♥\n')
            exit()
        else:
            clear()
            print('\n INVALID SELECTION \n')

#Creating Insert function
def insert():
    try:
        clear()
        empID = input("\nCreate Employee ID: ")
        empName =input("\nFirst & Last Name of Employee: ")
        empAge = input("\nEmployee's Age: ")
        empPhone = input("\nEmployee's Phone Number: ")

        mydb.Employees.insert_one(
            {
                "id": empID,
                "name":empName,
                "age":empAge,
                "Phone":empPhone
        })
        print('\nInserted data successfully\n')
    except Exception as e:
        print(e)

#Creating read function
def read():
    try:
        clear()
        print ('\n All data from Employee Database')
        empCol = mydb.Employees.find()
        for ekey in empCol:
            print("\n")
            del ekey['_id']
            for key in ekey:
                print(f'{key}: {ekey[key]}')

    except Exception as e:
        print(e)

def update():
    try:
        criteria = input('\nEnter ID to update\n')
        name = input('\nEnter name to update\n')
        age = input('\nEnter age to update\n')
        phone = input('\nEnter Phone to update\n')

        mydb.Employees.update_one(
            {"id": criteria},
            {
                "$set": {
                    "name":name,
                    "age":age,
                    "Phone":phone
                }
            }
        )
        print("\nRecords updated successfully\n")    
    
    except Exception as e:
        print(e)

def port():
    try:
        clear()
        with open("C:\\Users\\Kaya\\Desktop\\Python Projects\\Revature Projects\\PortData.JSON") as file:
            file_data = json.load(file)

        if isinstance(file_data, list):
            Collection.insert_many(file_data)
        else:
            Collection.insert_one(file_data)
        print('Import Successful')
    except Exception as e:
        print(e)


def delete():
    try:
        criteria = input('\nEnter employee id to delete: ')
        mydb.Employees.delete_many({"id":criteria})
        print('\nDeletion successful\n')
    except Exception as e:
        print(e)

main()

        