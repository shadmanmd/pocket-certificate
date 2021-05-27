from os import error
import sqlite3 as sql;

from werkzeug.utils import secure_filename;

from string import ascii_letters, digits
from random import choices
from cryptography.fernet import Fernet

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

        # Password generation
        pwd = ''.join(choices(ascii_letters + digits, k = 6))
        print(pwd)

        # Password encryption
        key = Fernet.generate_key()
        f = Fernet(key)
        password = f.encrypt(pwd.encode())

        #print(citizen_id,email_id,name,contact_no,dob,gender,address,image_BLOB,password,key)

        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "INSERT INTO citizen (citizen_id,name,email,contact,address,dob,gender,image,password,fernet_key) VALUES(?,?,?,?,?,?,?,?,?,?)"
        curr.execute(query,(citizen_id,name,email_id,contact_no,address,dob,gender,image_BLOB,password,key))
        print("Query execution in progress")

        conn.commit()
        print("Query executed")

        return "Citizen added successfully"
    except Exception as e:
        print("ERROR : ",e)
        return "Error in adding citizen"
    finally:
        curr.close()
        conn.close()
        


