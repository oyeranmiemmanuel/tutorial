import mysql.connector
# import MySQLdb
# MySQLdb.connect


def conn():
    global connection, cursor
    connection = mysql.connector.connect(host='localhost',
                        database='python_db',
                        user='root',
                        password='Emmanuel#5336')

    cursor = connection.cursor()

def create_db(db_name:str):
    global cursor, connection
    try:
        connection = mysql.connector.connect(host='localhost',
                    # database='python_db',
                    user='root',
                    password='Emmanuel#5336')



        cursor = connection.cursor()

        query= """CREATE DATABASE IF NOT EXISTS %s""" %(db_name)
        cursor.execute(query)
        print("database create!!")


    except mysql.connector.Error as error:
        print("Failed to create database {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is Closed")



def drop_db(database_name:str):
    try:
        conn()
        query= """DROP DATABASE %s""" %(database_name)
        cursor.execute(query)

        print("Database Deleted")

    except mysql.connector.Error as error:

        print(f"Failed to Drop Database: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MYSQL Connection is Closed")






def create_table(table_name:str):
    try:
        conn()
        # query= "CREATE TABLE %s (`id` INT NOT NULL , `name` TEXT NOT NULL ,`photo` LONGBLOB NOT NULL , `biodata` BLOB NOT NULL ,PRIMARY KEY `id`)"
        query= """CREATE TABLE IF NOT EXISTS %s (%s INT NOT NULL, %s TEXT NOT NULL, 
            %s LONGBLOB NOT NULL , %s BLOB NOT NULL)""" % (table_name, 'id', 'name', 'photo', 'biodata') 

        cursor.execute(query)

        print("Table Created")

    except mysql.connector.Error as error:
        print("Failed to create table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is Closed")



def convertToBinaryData(filename:str):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def insertBLOB(emp_id:int, name:str, photo:str, biodataFile:str):
    # global cursor, connection
    print("Inserting BLOB into python_employee table")
    try:
        conn()
        sql_insert_blob_query = """ INSERT INTO python_employee
                          (id, name, photo, biodata) VALUES (%s,%s,%s,%s)"""

        empPicture = convertToBinaryData(photo)
        file = convertToBinaryData(biodataFile)

        # Convert data into tuple format
        insert_blob_tuple = (emp_id, name, empPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_employee table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



# create_db("python_db")
# drop_db("python_db")
create_table("Python_Employee")

insertBLOB(1, "Emmanuel", "guy_with_polo.jpg",
           "emmanuel.txt")
insertBLOB(2, "Samuel", "samuel.jpg",
           "samuel.txt")

