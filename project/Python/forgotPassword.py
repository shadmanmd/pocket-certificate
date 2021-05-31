import sqlite3 as sql;

from string import ascii_letters, digits
from random import choices
from cryptography.fernet import Fernet

from Python.sendMail import forgotPasswordMail

def forgotPassword(citizen_id):
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "SELECT name,email FROM citizen WHERE citizen_id = ? "
        curr.execute(query, (citizen_id,))
        row = curr.fetchone()

        if row == None:
            return "Invalid Citizen ID"
        else:
            print("Updating password ...")

            # Password generation
            pwd = ''.join(choices(ascii_letters + digits, k = 6))
            print(pwd)

            # Password encryption
            key = Fernet.generate_key()
            f = Fernet(key)
            password = f.encrypt(pwd.encode())

            query = "UPDATE citizen SET password = ? WHERE citizen_id = ?"
            curr.execute(query,(password, citizen_id))

            conn.commit()
            print("Password updated")

            forgotPasswordMail(row[0], row[1], citizen_id, pwd)

        return "New password sent to your registered email ID."
        
    except Exception as e:
        print("ERROR : ",e)
        return "Error"
    finally:
        curr.close()
        conn.close()