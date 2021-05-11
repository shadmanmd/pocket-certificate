from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world from anukul"

if __name__=='__main__':
	app.run(debug=True)