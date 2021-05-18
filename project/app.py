from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

# ------------------------------- ADMIN ------------------------------------

@app.route('/admin/login')
def adminLogin():
    return render_template("login.html")

@app.route('/admin/dashboard')
def adminDashboard():
    return render_template("admin-dashboard.html")

@app.route('/admin/add-citizen')
def addCitizen():
    return render_template("admin-add-citizen.html")

@app.route('/admin/manage-citizen')
def manageCitizen():
    return render_template("admin-manage-citizen.html")

@app.route('/admin/add-doc')
def addDoc():
    return render_template("admin-add-doc.html")

@app.route('/admin/manage-doc')
def manageDoc():
    return render_template("admin-manage-doc.html")

@app.route('/admin/view-feedbacks')
def viewFeedback():
    return render_template("admin-view-feedback.html")

# ------------------------------- CITIZEN ------------------------------------

@app.route('/citizen/login')
def citizenLogin():
    return render_template("login.html")

@app.route('/citizen/doc')
def viewDoc():
    return render_template("citizen-view-doc.html")

@app.route('/citizen/feedback')
def giveFeedback():
    return render_template("citizen-give-feedback.html")

if __name__=='__main__':
	app.run(debug=True)