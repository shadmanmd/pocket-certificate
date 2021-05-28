import sqlite3 as sql

def getFeedbacks():
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        conn.row_factory = sql.Row

        curr = conn.cursor()
        print("Cursor created")

        query = "SELECT citizen_id,name,feedback,timestamp FROM feedback"
        curr.execute(query)
        row = curr.fetchall()
        return row
        
    except Exception as e:
        print("ERROR : ",e)
        return "Error in fetching feedbacks"
    finally:
        curr.close()
        conn.close()