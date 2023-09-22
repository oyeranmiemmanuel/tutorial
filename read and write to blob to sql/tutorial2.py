from tkinter import *
from tkinter import filedialog, messagebox
import customtkinter
import mysql.connector
import pymysql
import os
from PIL import Image
import io


#first
def conn():
    global connection, cursor
    connection = mysql.connector.connect(host='localhost',
                        database='python_db',
                        user='root',
                        password='Emmanuel#5336')

    cursor = connection.cursor()

#fourth
def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)


#fifth
def savedata():
    pass


#third
def readBLOB():
    emp_id= entry.get()

    try:
        conn()
        sql_fetch_blob_query = """SELECT * FROM python_employee WHERE id = %s"""

        cursor.execute(sql_fetch_blob_query, (emp_id,))
        record = cursor.fetchone()
        if record:

            photo_name= filedialog.asksaveasfilename(initialdir=os.getcwd(), title="select file", filetypes=(("Image File", "*.jpg"), ("All Files", "*.*")))
            bioData_name= filedialog.asksaveasfilename(initialdir=os.getcwd(), title="select file", filetypes=(("Text File", "*.txt"), ("All Files", "*.*")))

            image = record[2]
            file = record[3]
            if photo_name and bioData_name:
                write_file(image, photo_name)
                write_file(file, bioData_name)


            image=Image.open(io.BytesIO(image))
            img1= customtkinter.CTkImage(light_image=image, dark_image=image, size=(100,150))

            label_1.pack(padx=20, pady=20)
            label_1.configure(image=img1)

    except mysql.connector.Error as error:
        # if there is any error while reading
        print("Failed to read BLOB data from MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")



win= customtkinter.CTk()



#second
Button(win, text="save file to database", command=savedata).pack()
Button(win, text="read data from database", command=readBLOB).pack()
label1= Label(win)
entry= customtkinter.CTkEntry(win)
entry.pack()
label_1 = customtkinter.CTkLabel(win, text="", compound="right", fg_color="green", width=0)
# label_2 = customtkinter.CTkLabel(win, text="", compound="right", fg_color="green", width=0)








win.geometry("200x200")
win.title("Read & save Blob")
win.mainloop()
