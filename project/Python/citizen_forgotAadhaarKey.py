import sqlite3 as sql

from Python.sendMail import forgotAadhaarKeyMail

def citizenForgotAadhaarKey(citizen_id):
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created for Aadhaar")

        query = "SELECT name,email,aadhaar_key FROM citizen WHERE citizen_id = ?"
        curr.execute(query,(citizen_id,))
        print("Query executed")
        row = curr.fetchone()
        name = row[0]
        email = row[1]
        aadhaar_key = row[2]
        print(row)

        forgotAadhaarKeyMail(name, email, aadhaar_key)

        return "Aadhaar key sent to your registered email ID."
    
    except Exception as e:
        print("ERROR : ",e)
        return "Error in fetching details"
    finally:
        curr.close()
        conn.close()