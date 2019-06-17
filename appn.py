import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Sample Window")

heading_label = tk.Label(mainWindow, text="Name")
heading_label.pack()

name_field = tk.Entry(mainWindow)
name_field.pack()

heading_label2 = tk.Label(mainWindow, text="College")
heading_label2.pack()

college_field = tk.Entry(mainWindow)
college_field.pack()

heading_label3 = tk.Label(mainWindow, text="Address")
heading_label3.pack()

address_field = tk.Entry(mainWindow)
address_field.pack()

heading_label4 = tk.Label(mainWindow, text="Phone")
heading_label4.pack()

phone_field = tk.Entry(mainWindow)
phone_field.pack()

import sqlite3

connection = sqlite3.connect('sample.db')
print("Database opened successfully.")

TABLE_NAME = "student_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")

def save():
    name = name_field.get()
    college = college_field.get()
    address = address_field.get()
    phone = phone_field.get()
    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                            STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                             STUDENT_PHONE + " ) VALUES ( '" + name +"', '"+college+"', "
                                            "'"+address+"', "+str(phone)+" ); ")
    connection.commit()
    print("Data stored successfully")

def retrieve():
    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")

    for row in cursor:
            print("Student id is: ", row[0])
            print("Student name is: ", row[1])
            print("Student college is: ", row[2])
            print("Student address is: ", row[3])
            print("Student phone is: ", row[4])


button = tk.Button(mainWindow, text="Save", command=lambda : save())
button.pack()
button = tk.Button(mainWindow, text="Retrieve", command=lambda : retrieve())
button.pack()
mainWindow.mainloop()