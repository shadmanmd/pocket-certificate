import sqlite3 as sql;

def adminDeletePan(citizen_id):
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "UPDATE citizen SET pan_id = null, pan_key = null WHERE citizen_id = ?"
        curr.execute(query,(citizen_id,))

        conn.commit()
        print("Query executed")

        return "Deletion successful"
    
    except Exception as e:
        print("ERROR : ",e)
        return "Error in deletion"
    
    finally:
        curr.close()
        conn.close()