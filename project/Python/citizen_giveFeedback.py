import sqlite3 as sql

from datetime import datetime

def submitFeedback(citizen_id, name, form):
    try:
        feedback = form['feedback']

        now = datetime.now()
        timestamp = now.strftime("%d/%m/%Y %H:%M:%S")

        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "INSERT INTO feedback (citizen_id, feedback, timestamp, name) VALUES(?, ?, ?, ?)"
        curr.execute(query, (citizen_id, feedback, timestamp, name))

        conn.commit()
        print("Feedback inserted in db.")

        return "Feedback sent to admin"
    
    except Exception as e:
        print("ERROR : ",e)
        return "Error"
    
    finally:
        curr.close()
        conn.close()

def getCitizenName(citizen_id):
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "SELECT name FROM citizen WHERE citizen_id = ? "
        curr.execute(query, (citizen_id,))
        row = curr.fetchone()
        return row
        
    except Exception as e:
        print("ERROR : ",e)
        return "Error"
    finally:
        curr.close()
        conn.close()