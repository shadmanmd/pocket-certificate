from os import error
import sqlite3 as sql;
from werkzeug.utils import secure_filename;
import os;

def convertToBinaryData(fileName):
    try:
        file = open(fileName,'rb')
        blobData = file.read()
        return blobData
    except Exception as e:
        print("ERROR : ", e)

def adminAddCitizen(form,files):
    try:
        citizen_id = form["citizen-id"]
        email_id = form["email-id"]
        name = form["name"]
        contact_no = form["contact-no"]
        dob = form["dob"]
        gender = form["gender"]
        address = form["address"]
        image = files["image"]
        fileName = secure_filename(image.filename)
        image_BLOB = convertToBinaryData(fileName)
        

        print(citizen_id,email_id,name,contact_no,dob,gender,address,image_BLOB)

        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "INSERT INTO citizen (citizen_id,name,email,contact,address,dob,gender,image) VALUES(?,?,?,?,?,?,?,?)"
        curr.execute(query,(citizen_id,name,email_id,contact_no,address,dob,gender,image_BLOB))
        print("Query execution in progress")

        conn.commit()
        print("Query executed")

        return "Citizen added successfully"
    except sql.Error as e:
        print("ERROR : ",e)
        return "Error in adding citizen"
    finally:
        curr.close()
        conn.close()
        


