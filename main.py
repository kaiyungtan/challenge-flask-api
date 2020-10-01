from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'd0ea495b7900975cd88b63a8d8875106'

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')

@app.route("/status")
def status():
	return render_template('status.html')

@app.route("/login" ,methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash(f'Login success for {form.username.data} with password length of: {len(form.password.data)}!' ,'success')
		return redirect(url_for('home'))
	return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
	app.run(debug=True)
