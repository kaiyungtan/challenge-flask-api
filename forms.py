from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired , NumberRange ,InputRequired


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class PredictForm(FlaskForm):
    month = IntegerField("Month", validators=[InputRequired(), NumberRange(min=1, max=12)])
    customer_visiting_website = IntegerField("Customer visiting website", validators=[InputRequired(), NumberRange()])
    seller_available = IntegerField("Seller available", validators=[InputRequired(), NumberRange()])
    submit = SubmitField("Predict")


class ImageUpload(FlaskForm):
    picture = FileField('Update Image', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Upload image')
