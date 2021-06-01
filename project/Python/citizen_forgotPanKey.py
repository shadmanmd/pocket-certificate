import sqlite3 as sql

from Python.sendMail import forgotPanKeyMail

def citizenForgotPanKey(citizen_id):
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created for Pan")

        query = "SELECT name,email,pan_key FROM citizen WHERE citizen_id = ?"
        curr.execute(query,(citizen_id,))
        print("Query executed")
        row = curr.fetchone()
        name = row[0]
        email = row[1]
        pan_key = row[2]
        print(row)

        forgotPanKeyMail(name, email, pan_key)

        return "PAN key sent to your registered email ID."
    
    except Exception as e:
        print("ERROR : ",e)
        return "Error in fetching details"
    finally:
        curr.close()
        conn.close()