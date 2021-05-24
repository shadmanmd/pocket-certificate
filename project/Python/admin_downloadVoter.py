import sqlite3 as sql;
from werkzeug.utils import secure_filename;
from flask import send_file
from io import BytesIO

def adminDownloadVoter(citizen_id):
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        query = "SELECT voter_id FROM citizen WHERE citizen_id = ?"
        curr.execute(query,(citizen_id,))
        row = curr.fetchone()
        data = row[0]
        fileName = str(citizen_id) + "_Voter.jpg"
        return send_file(BytesIO(data),mimetype="image/jpeg",attachment_filename=fileName,as_attachment=True)
        
    except Exception as e:
        print("ERROR : ",e)
        return "Error in fetching citizen details"
    finally:
        curr.close()
        conn.close()