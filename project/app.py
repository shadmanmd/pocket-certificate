from flask import Flask, render_template, request, redirect, url_for, session
from helper import *

adminCredentials = {'username': 'admin', 'password': 'password'}

app = Flask(__name__)
app.secret_key = 'POCKET-CERTIFICATE-USING-DOUBLE-ENCRYPTION'

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('message', None)
    return redirect(url_for('index'))



# ------------------------------- ADMIN ------------------------------------



@app.route('/admin/login', methods=['GET', 'POST'])
def adminLogin():
    if request.method == 'POST':
        if request.form['username'] == adminCredentials['username'] and request.form['password'] == adminCredentials['password']:
            session['username'] = request.form['username']
            session.pop('message', None)
            return redirect(url_for('adminDashboard'))
        else:
            session['message'] = 'Invalid user ID or password'
            return redirect(url_for('adminLogin'))
    else:
        if 'message' in session:
            m = session['message']
            session.pop('message',None)
            return render_template("login.html", value="Admin", msg = m)
        else:
            return render_template("login.html", value="Admin")



@app.route('/admin/dashboard')
def adminDashboard():
    if 'username' in session:
        if session['username'] == 'admin':
            return render_template("admin-dashboard.html")
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/admin/add-citizen', methods=['GET', 'POST'])
def addCitizen():
    if 'username' in session:
        if session['username'] == 'admin':
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
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/admin/edit-citizen/<citizen_id>', methods = ['GET', 'POST'])
def editCitizen(citizen_id):
    if 'username' in session:
        if session['username'] == 'admin':
            if request.method=='POST':
                msg = adminEditCitizen(citizen_id, request.form)
                return redirect(url_for('manageCitizen'))
            else:
                citizen = adminGetCitizen(citizen_id)
                print(citizen)
                if citizen[6]:
                    redirect(url_for('image_route',citizen_id=citizen_id))
                return render_template("admin-edit-citizen.html", citizen=citizen, citizen_id=citizen_id)
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))




@app.route('/admin/manage-citizen')
def manageCitizen():
    if 'username' in session:
        if session['username'] == 'admin':
            citizenDetail_list = getCitizenDetails()
            return render_template("admin-manage-citizen.html",citizenDetail_list=citizenDetail_list)
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/admin/add-doc', methods=['GET', 'POST'])
def addDoc():
    if 'username' in session:
        if session['username'] == 'admin':
            citizen_id_list = getCitizenId()
            msg=""
            if request.method=='POST':
                msg = adminAddDoc(request.form,request.files)
                print(msg)
            return render_template("admin-add-doc.html",citizen_id_list=citizen_id_list,msg=msg)
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/admin/manage-doc')
def manageDoc():
    if 'username' in session:
        if session['username'] == 'admin':
            doc_list = getDocDetails()
            return render_template("admin-manage-doc.html", doc_list=doc_list)
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/downloads/aadhaar_id/<citizen_id>',methods=['POST','GET'])
def downloadAadhaar(citizen_id):
    if 'username' in session:
        return adminDownloadAadhaar(citizen_id)
        return redirect(url_for('manageDoc'))
    else:
        session['message'] = 'Please login'
        return redirect(url_for('index'))



@app.route('/downloads/pan_id/<citizen_id>',methods=['POST','GET'])
def downloadPan(citizen_id):
    if 'username' in session:
        return adminDownloadPan(citizen_id)
        return redirect(url_for('manageDoc'))
    else:
        session['message'] = 'Please login'
        return redirect(url_for('index'))



@app.route('/downloads/voter_id/<citizen_id>',methods=['POST','GET'])
def downloadVoter(citizen_id):
    if 'username' in session:
        return adminDownloadVoter(citizen_id)
        return redirect(url_for('manageDoc'))
    else:
        session['message'] = 'Please login'
        return redirect(url_for('index'))



@app.route('/downloads/driving_id/<citizen_id>',methods=['POST','GET'])
def downloadDriving(citizen_id):
    if 'username' in session:
        return adminDownloadDriving(citizen_id)
        return redirect(url_for('manageDoc'))
    else:
        session['message'] = 'Please login'
        return redirect(url_for('index'))



@app.route('/delete/aadhaar_id/<citizen_id>')
def deleteAadhaar(citizen_id):
    if 'username' in session:
        if session['username'] == 'admin':
            msg = adminDeleteAadhaar(citizen_id)
            return redirect(url_for('manageDoc'))
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/delete/pan_id/<citizen_id>')
def deletePan(citizen_id):
    if 'username' in session:
        if session['username'] == 'admin':
            msg = adminDeletePan(citizen_id)
            return redirect(url_for('manageDoc'))
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/delete/voter_id/<citizen_id>')
def deleteVoter(citizen_id):
    if 'username' in session:
        if session['username'] == 'admin':
            msg = adminDeleteVoter(citizen_id)
            return redirect(url_for('manageDoc'))
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/delete/driving_id/<citizen_id>')
def deleteDriving(citizen_id):
    if 'username' in session:
        if session['username'] == 'admin':
            msg = adminDeleteDriving(citizen_id)
            return redirect(url_for('manageDoc'))
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/delete/citizen/<citizen_id>')
def deleteCitizen(citizen_id):
    if 'username' in session:
        if session['username'] == 'admin':
            msg = adminDeleteCitizen(citizen_id)
            return redirect(url_for('manageCitizen'))
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/edit/aadhaar_id/<citizen_id>', methods=['GET', 'POST'])
def editAadhaar(citizen_id):
    if 'username' in session:
        if session['username'] == 'admin':
            if request.method=='POST':
                msg = adminAddDoc(request.form,request.files)
                print(msg)
                return redirect(url_for('manageDoc'))
            return render_template("admin-edit-doc.html", citizen_id=citizen_id, doc_type='aadhaar')
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/edit/pan_id/<citizen_id>', methods=['GET', 'POST'])
def editPan(citizen_id):
    if 'username' in session:
        if session['username'] == 'admin':
            if request.method=='POST':
                msg = adminAddDoc(request.form,request.files)
                print(msg)
                return redirect(url_for('manageDoc'))
            return render_template("admin-edit-doc.html", citizen_id=citizen_id, doc_type='pan')
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/edit/voter_id/<citizen_id>', methods=['GET', 'POST'])
def editVoter(citizen_id):
    if 'username' in session:
        if session['username'] == 'admin':
            if request.method=='POST':
                msg = adminAddDoc(request.form,request.files)
                print(msg)
                return redirect(url_for('manageDoc'))
            return render_template("admin-edit-doc.html", citizen_id=citizen_id, doc_type='voter')
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/edit/driving_id/<citizen_id>', methods=['GET', 'POST'])
def editDriving(citizen_id):
    if 'username' in session:
        if session['username'] == 'admin':
            if request.method=='POST':
                msg = adminAddDoc(request.form,request.files)
                print(msg)
                return redirect(url_for('manageDoc'))
            return render_template("admin-edit-doc.html", citizen_id=citizen_id, doc_type='driving')
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



@app.route('/admin/view-feedbacks')
def viewFeedback():
    if 'username' in session:
        if session['username'] == 'admin':
            return render_template("admin-view-feedback.html")
        else:
            return "<h1>Please login as admin to view this.</h1>"
    else:
        session['message'] = 'Please login'
        return redirect(url_for('adminLogin'))



# ------------------------------- CITIZEN ------------------------------------



@app.route('/citizen/login', methods = ['GET', 'POST'])
def citizenLogin():
    if request.method == 'POST':
        inputCitizen = request.form['username']
        inputPassword = request.form['password']
        data = citizenExists(inputCitizen)
        print(data)
        if data == None:
            session['message'] = 'Invalid user ID or password'
            return redirect(url_for('citizenLogin'))
        else:
            if checkPassword(data[8], data[7], inputPassword) == True:
                session['username'] = request.form['username']
                return redirect(url_for('citizenDashboard'))
            else:
                session['message'] = 'Invalid user ID or password'
                return redirect(url_for('citizenLogin'))
    else:
        if 'message' in session:
            msg = session['message']
            session.pop('message',None)
            return render_template("login.html", value="Citizen", msg = msg)
        else:
            return render_template("login.html", value="Citizen")



@app.route('/citizen/dashboard')
def citizenDashboard():
    if 'username' in session:
        citizen_id = session['username']
        citizen_data_list = getCitizenData(citizen_id)
        if citizen_data_list == None:
            return "<h1>Please login as citizen to view this.</h1>"
        if(citizen_data_list[7]):
            redirect(url_for('image_route',citizen_id=citizen_id))
        return render_template("citizen-dashboard.html",citizen_data=citizen_data_list)
    else:
        session['message'] = 'Please login'
        return redirect(url_for('citizenLogin'))


@app.route('/citizen/doc')
def viewDoc():
    if 'username' in session:
        citizen_id = session['username']
        docs = viewDocuments(citizen_id)
        if docs == None:
            return "<h1>Please login as citizen to view this.</h1>"
        return render_template("citizen-view-doc.html", docs=docs, citizen_id=citizen_id)
    else:
        session['message'] = 'Please login'
        return redirect(url_for('citizenLogin'))

@app.route('/citizen/feedback')
def giveFeedback():
    if 'username' in session:
        citizen_id = session['username']
        return render_template("citizen-give-feedback.html")
    else:
        session['message'] = 'Please login'
        return redirect(url_for('citizenLogin'))


@app.route('/image/<citizen_id>')
def image_route(citizen_id):
    img = getCitizenImage(citizen_id)
    if(img[0]):
        return send_file(BytesIO(img[0]),mimetype='image/jpeg')
    

if __name__=='__main__':
	app.run(debug=True)