import sqlite3 as sql

from Python.sendMail import forgotVoterKeyMail

def citizenForgotVoterKey(citizen_id):
    try: 
        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created for Voter")

        query = "SELECT name,email,voter_key FROM citizen WHERE citizen_id = ?"
        curr.execute(query,(citizen_id,))
        print("Query executed")
        row = curr.fetchone()
        name = row[0]
        email = row[1]
        voter_key = row[2]
        print(row)

        forgotVoterKeyMail(name, email, voter_key)

        return "Voter ID key sent to your registered email ID."
    
    except Exception as e:
        print("ERROR : ",e)
        return "Error in fetching details"
    finally:
        curr.close()
        conn.close()