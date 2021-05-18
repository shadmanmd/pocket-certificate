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

@app.route('/admin/add-citizen')

@app.route('/admin/manage-citizen')

@app.route('/admin/add-document')

@app.route('/admin/manage-documents')

@app.route('/admin/view-feedbacks')

# ------------------------------- CITIZEN ------------------------------------

@app.route('/citizen/login')
def citizenLogin():
    return render_template("login.html")

@app.route('/citizen/documents')

@app.route('/citizen/feedback')

if __name__=='__main__':
	app.run(debug=True)