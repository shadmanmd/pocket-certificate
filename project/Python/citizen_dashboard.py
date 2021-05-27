import sqlite3 as sql;
from Python.admin_addCitizen import convertToBinaryData
from io import BytesIO
from flask import send_file

def getCitizenData(citizen_id):
    try: 
        print("IN DASHBOARD")
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "SELECT citizen_id,name,email,contact,gender,dob,address,image FROM citizen WHERE citizen_id = ? "
        curr.execute(query, (citizen_id,))
        print("Query executed")
        row = curr.fetchone()
        return row
        
    except Exception as e:
        print("ERROR : ",e)
        return "Error in adding document"
    finally:
        curr.close()
        conn.close()

def getCitizenImage(citizen_id):
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "SELECT image FROM citizen WHERE citizen_id = ? "
        curr.execute(query,(citizen_id,))
        row = curr.fetchone()
        return row
        
    except Exception as e:
        print("ERROR : ",e)
        return "Error in adding document"
    finally:
        curr.close()
        conn.close()
