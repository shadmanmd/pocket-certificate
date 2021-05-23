import sqlite3 as sql;
from werkzeug.utils import secure_filename;
from Python.admin_addCitizen import convertToBinaryData

def adminAddDoc(form,files):
    try: 
        doc_type = form["doc-type"]
        citizen_id = form["citizen-id"]
        private_key = form["key"]
        doc = files["doc"]

        doc_key = doc_type+"_key"
        doc_id = doc_type+"_id"

        fileName = secure_filename(doc.filename)
        doc_BLOB = convertToBinaryData(fileName)

        conn = sql.connect("database/pocket-certificate-db.db")
        print("Conection made with the database")

        curr = conn.cursor()
        print("Cursor created")

        #Check if document already exists or not
        query = "SELECT "+doc_key+" FROM citizen WHERE citizen_id = ?"
        curr.execute(query,(citizen_id,))
        row = curr.fetchone()
        if(row[0]):
            return upper(doc_type)+" ID already exists for citizen-id : "+citizen_id+" You can view edit/delete the document from manage documents section."
        else:
            query = "UPDATE citizen SET "+doc_id+" =?, "+doc_key+" =?  WHERE citizen_id = ?"
            curr.execute(query,(doc_BLOB,private_key,citizen_id))
            print("Query execution in progress")

            conn.commit()
            print("Query executed")

            return "Document added successfully"
    except Exception as e:
        print("ERROR : ",e)
        return "Error in adding document"
    finally:
        curr.close()
        conn.close()




