import sqlite3 as sql;
from werkzeug.utils import secure_filename;

def adminEditCitizen(citizen_id, form):
    try:
        name = form["name"]
        contact_no = form["contact-no"]
        dob = form["dob"]
        gender = form["gender"]
        address = form["address"]

        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "UPDATE citizen SET name = ?, contact = ?, dob = ?, gender = ?, address = ? WHERE citizen_id = ?"
        curr.execute(query, (name, contact_no, dob, gender, address, citizen_id))
        print("Query execution in progress")

        conn.commit()
        print("Query executed")

        return "Citizen edited successfully"
    except Exception as e:
        print("ERROR : ",e)
        return "Error in adding citizen"
    finally:
        curr.close()
        conn.close()


def adminGetCitizen(citizen_id):
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        conn.row_factory = sql.Row

        curr = conn.cursor()
        print("Cursor created")

        query = "SELECT name,email,contact,address,dob,gender,image FROM citizen WHERE citizen_id = ?"
        curr.execute(query,(citizen_id,))
        row = curr.fetchone()
        return row
        
    except Exception as e:
        print("ERROR : ",e)
        return "Error in fetching citizen details"
    finally:
        curr.close()
        conn.close()