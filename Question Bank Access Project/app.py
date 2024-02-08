from flask import Flask, render_template, request, session
import mysql.connector
from difflib import SequenceMatcher

app = Flask(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')

# Define other routes...

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
