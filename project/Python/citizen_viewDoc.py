import sqlite3 as sql

def viewDocuments(citizen_id):
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "SELECT name,aadhaar_id,pan_id,voter_id,driving_id FROM citizen WHERE citizen_id = ? "
        curr.execute(query, (citizen_id,))
        row = curr.fetchone()
        return row
        
    except Exception as e:
        print("ERROR : ",e)
        return "Error"
    finally:
        curr.close()
        conn.close()