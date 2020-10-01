from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired 

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')


class PredictForm(FlaskForm):
	month = IntegerField('Month', validators=[DataRequired()])
	customer_visiting_website = IntegerField('Customer visiting website',validators=[DataRequired()])
	seller_avaible =  IntegerField('Seller avaible',validators=[DataRequired()])

	submit = SubmitField('Predict')
 