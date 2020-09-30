from flask import Flask 

app = Flask(__name__)
app.config['SECRET_KEY'] = '02c6edb914cf6b21d5061f83a6921dec'
 

from challenge-flask-api import main