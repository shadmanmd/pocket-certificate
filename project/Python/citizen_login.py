import sqlite3 as sql;

from cryptography.fernet import Fernet

def citizenExists(citizen_id):
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "SELECT name,email,contact,gender,dob,address,image,password,fernet_key FROM citizen WHERE citizen_id = ? "
        curr.execute(query, (citizen_id,))
        row = curr.fetchone()
        return row
        
    except Exception as e:
        print("ERROR : ",e)
        return "Error"
    finally:
        curr.close()
        conn.close()

def checkPassword(key, encryptedPassword, inputPassword):
    f = Fernet(key)
    password = f.decrypt(encryptedPassword).decode()
    if password == inputPassword:
        return True
    else:
        return False