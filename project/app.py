from flask import Flask, render_template, request, redirect, url_for, session
from helper import *


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# ------------------------------- ADMIN ------------------------------------

@app.route('/admin/login')
def adminLogin():
    return render_template("login.html", value="Admin")

@app.route('/admin/dashboard')
def adminDashboard():
    return render_template("admin-dashboard.html")

@app.route('/admin/add-citizen', methods=['GET', 'POST'])
def addCitizen():
    file = open('citizen-id.txt')
    citizenID = 'CTZ' + file.read()
    print(citizenID)
    file.close()
    msg=""
    if request.method=='POST':
        msg = adminAddCitizen(request.form,request.files)
        
        newCitizenID = int(citizenID[3:]) + 1
        file = open('citizen-id.txt', 'w')
        file.write(str(newCitizenID))
        file.close()

        citizenID = 'CTZ' + str(newCitizenID)
    return render_template("admin-add-citizen.html", citizenID=citizenID, msg=msg)

@app.route('/admin/manage-citizen')
def manageCitizen():
    citizenDetail_list = getCitizenDetails()
    return render_template("admin-manage-citizen.html",citizenDetail_list=citizenDetail_list)

@app.route('/admin/add-doc', methods=['GET', 'POST'])
def addDoc():
    citizen_id_list = getCitizenId()
    msg=""
    if request.method=='POST':
        msg = adminAddDoc(request.form,request.files)
        print(msg)
    return render_template("admin-add-doc.html",citizen_id_list=citizen_id_list,msg=msg)

@app.route('/admin/manage-doc')
def manageDoc():
    doc_list = getDocDetails()
    return render_template("admin-manage-doc.html", doc_list=doc_list)

@app.route('/downloads/aadhaar_id/<citizen_id>',methods=['POST','GET'])
def downloadAadhaar(citizen_id):
    return adminDownloadAadhaar(citizen_id)
    return redirect(url_for('manageDoc'))

@app.route('/downloads/pan_id/<citizen_id>',methods=['POST','GET'])
def downloadPan(citizen_id):
    return adminDownloadPan(citizen_id)
    return redirect(url_for('manageDoc'))

@app.route('/downloads/voter_id/<citizen_id>',methods=['POST','GET'])
def downloadVoter(citizen_id):
    return adminDownloadVoter(citizen_id)
    return redirect(url_for('manageDoc'))

@app.route('/downloads/driving_id/<citizen_id>',methods=['POST','GET'])
def downloadDriving(citizen_id):
    return adminDownloadDriving(citizen_id)
    return redirect(url_for('manageDoc'))

@app.route('/delete/aadhaar_id/<citizen_id>')
def deleteAadhaar(citizen_id):
    msg = adminDeleteAadhaar(citizen_id)
    return redirect(url_for('manageDoc'))

@app.route('/delete/pan_id/<citizen_id>')
def deletePan(citizen_id):
    msg = adminDeletePan(citizen_id)
    return redirect(url_for('manageDoc'))

@app.route('/delete/voter_id/<citizen_id>')
def deleteVoter(citizen_id):
    msg = adminDeleteVoter(citizen_id)
    return redirect(url_for('manageDoc'))

@app.route('/delete/driving_id/<citizen_id>')
def deleteDriving(citizen_id):
    msg = adminDeleteDriving(citizen_id)
    return redirect(url_for('manageDoc'))

@app.route('/admin/view-feedbacks')
def viewFeedback():
    return render_template("admin-view-feedback.html")

# ------------------------------- CITIZEN ------------------------------------

@app.route('/citizen/login')
def citizenLogin():
    return render_template("login.html", value="Citizen")

@app.route('/citizen/dashboard')
def citizenDashboard():
    return render_template("citizen-dashboard.html")

@app.route('/citizen/doc')
def viewDoc():
    return render_template("citizen-view-doc.html")

@app.route('/citizen/feedback')
def giveFeedback():
    return render_template("citizen-give-feedback.html")

if __name__=='__main__':
	app.run(debug=True)