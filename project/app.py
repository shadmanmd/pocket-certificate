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

@app.route('/admin/edit-citizen/<citizen_id>', methods = ['GET', 'POST'])
def editCitizen(citizen_id):
    if request.method=='POST':
        msg = adminEditCitizen(citizen_id, request.form)
        return redirect(url_for('manageCitizen', msg=msg))
    else:
        citizen = adminGetCitizen(citizen_id)
        print(citizen)
        if citizen[6]:
            redirect(url_for('image_route',citizen_id=citizen_id))
        return render_template("admin-edit-citizen.html", citizen=citizen, citizen_id=citizen_id)

@app.route('/admin/manage-citizen')
def manageCitizen(msg=''):
    print(msg)
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

@app.route('/delete/citizen/<citizen_id>')
def deleteCitizen(citizen_id):
    msg = adminDeleteCitizen(citizen_id)
    return redirect(url_for('manageCitizen'))

@app.route('/edit/aadhaar_id/<citizen_id>', methods=['GET', 'POST'])
def editAadhaar(citizen_id):
    msg=""
    if request.method=='POST':
        msg = adminAddDoc(request.form,request.files)
        print(msg)
        return redirect(url_for('manageDoc'))
    return render_template("admin-edit-doc.html", citizen_id=citizen_id, doc_type='aadhaar')

@app.route('/edit/pan_id/<citizen_id>', methods=['GET', 'POST'])
def editPan(citizen_id):
    msg=""
    if request.method=='POST':
        msg = adminAddDoc(request.form,request.files)
        print(msg)
        return redirect(url_for('manageDoc'))
    return render_template("admin-edit-doc.html", citizen_id=citizen_id, doc_type='pan')

@app.route('/edit/voter_id/<citizen_id>', methods=['GET', 'POST'])
def editVoter(citizen_id):
    msg=""
    if request.method=='POST':
        msg = adminAddDoc(request.form,request.files)
        print(msg)
        return redirect(url_for('manageDoc'))
    return render_template("admin-edit-doc.html", citizen_id=citizen_id, doc_type='voter')

@app.route('/edit/driving_id/<citizen_id>', methods=['GET', 'POST'])
def editDriving(citizen_id):
    msg=""
    if request.method=='POST':
        msg = adminAddDoc(request.form,request.files)
        print(msg)
        return redirect(url_for('manageDoc'))
    return render_template("admin-edit-doc.html", citizen_id=citizen_id, doc_type='driving')

@app.route('/admin/view-feedbacks')
def viewFeedback():
    return render_template("admin-view-feedback.html")

# ------------------------------- CITIZEN ------------------------------------

@app.route('/citizen/login')
def citizenLogin():
    return render_template("login.html", value="Citizen")

@app.route('/citizen/dashboard')
def citizenDashboard():
    citizen_data_list = getCitizenData()
    if(citizen_data_list[7]):
        redirect(url_for('image_route',citizen_id='CTZ1008'))
    return render_template("citizen-dashboard.html",citizen_data=citizen_data_list)

@app.route('/citizen/doc')
def viewDoc():
    return render_template("citizen-view-doc.html")

@app.route('/citizen/feedback')
def giveFeedback():
    return render_template("citizen-give-feedback.html")


@app.route('/image/<citizen_id>')
def image_route(citizen_id):
    img = getCitizenImage(citizen_id)
    if(img[0]):
        return send_file(BytesIO(img[0]),mimetype='image/jpeg')
    

if __name__=='__main__':
	app.run(debug=True)