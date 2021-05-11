# 1
In the command line,
```python
pip install virtualenv
virtualenv [env-name]
```

Creates a folder in the current directory with the 'env-name'.

# 2
Now run
```
env-name\Scripts\activate.bat
```

The terminal will change with env-name in a bracket. This indicates that all changes made in here (like libraries installed) will be reflected only in the env-name folder.

# 3
- Go to the root directory and create the project folder.
- Go to the project folder and create a .py file.
A simple hello world file is shown below

```python
# hello.py

from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world"
```

# 4
To run the file, go to the command line and set the environment variable FLASK_APP to the name of the Python file
```
set FLASK_APP=hello.py
```
Now the Flask app can be run by
```
flask run
```
You will see the hello world message on localhost:5000 upon executing ```flask run``` again.

# 5 Auto re-render without using ```flask run``` again & again

## a
```
set FLASK_DEBUG=1
```

## b
```python
if __name__=='__main__':
	app.run(debug=True)
```
Now we need to run the file like a simple python file
```
python hello.py
```
