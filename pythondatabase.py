#import sql connector in python
import mysql.connector as connector
#create a connection with my sql database
def connect_todatabase():
    try:
        mydatabase = connector.connect(
        host = "localhost",
        user = "root",
        password = "coco14576SNN",
        #select just one database that already exist
        database = "bike"
        )
        print("Goodjobdone")
        return mydatabase
    except connector.Error as err:
        print("oops error")

def my_database_is_connected():
    connection = connect_todatabase()
    if connection:
        return True
    else:
        return False

if my_database_is_connected():
    print("Success")



#create a database
def newdatabase():
    try:
        mydatabase = connect_todatabase().cursor()
        # mycursor = mydatabase.cursor()

        mycursor.execute("CREATE DATABASE clients")
        print("one mile stone completed")
    except connector.Error as err:
        print("oops error",err)
    
    finally:
         if mycursor:
            mycursor.close()
         if mydatabase:
            mydatabase.close()


# newdatabase()

#check for database 
def check_database():
    try: 
        mydb = connect_todatabase()
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        #loop through cursor with a for loop to print everything in the db
        for x in mycursor:
            print(x)
    except connector.Error as err:
        print("oops there was an error",err)

check_database()