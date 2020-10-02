from flask import Flask  
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config["SECRET_KEY"] = "d0ea495b7900975cd88b63a8d8875106"
app.config['SQLALCHEMY_DATA_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from main import routes