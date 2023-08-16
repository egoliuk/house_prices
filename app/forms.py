from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.fields import EmailField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_wtf.file import FileField, FileRequired, FileAllowed
from app.models import User

class LoginForm(FlaskForm):
    email = EmailField('Email address', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

# TODO implement form to add one House manually
# class HouseForm(FlaskForm):
#     SalePrice = FloatField('Sale Price', default=0.0, validators=[DataRequired()])
#     submit = SubmitField('Submit')

class UploadDatasetForm(FlaskForm):
    dataset = FileField(validators=[FileRequired(), FileAllowed(['csv'], 'CSV only!')])
    submit = SubmitField('Upload')
