import sqlite3 as sql;
from werkzeug.utils import secure_filename;

def getCitizenDetails():
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        conn.row_factory = sql.Row

        curr = conn.cursor()
        print("Cursor created")

        query = "SELECT citizen_id,name,email FROM citizen"
        curr.execute(query)
        row = curr.fetchall()
        return row
        
    except Exception as e:
        print("ERROR : ",e)
        return "Error in fetching citizen details"
    finally:
        curr.close()
        conn.close()