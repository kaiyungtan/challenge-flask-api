from flask import Flask, render_template, flash 
from forms import LoginForm
import secrets

app = Flask(__name__)

app.config['SECET_KEY'] = '02c6edb914cf6b21d5061f83a6921dec'

@app.route('/status', methods=['GET'])
def status():
    return "Alive"


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    USER_NAME_HERE = form.username.data
    PASSWORD_LENGTH_HERE = len(form.password.data)

    return flash(f"Login success for user {USER_NAME_HERE} with password from length: {PASSWORD_LENGTH_HERE}!")


if __name__ == '__main__':
   app.run(port=5000,debug=True)