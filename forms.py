from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError, Regexp
from flask_wtf.file import FileField, FileAllowed
from wtforms.widgets import TextArea
from wtforms.fields import MultipleFileField
# from main import User

class RegistrationForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(),  Regexp(r'^[\w.@+-]+$', message="Username must not include spaces") ,Length(max=10, message="Should be less than 10 characters")])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=10, message="Number must be 10 digits")])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=16, message="Password must be less than 16 characters")])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    # def validate_phone(self, phone):
    #     user = User.query.filter_by(phone=phone.data).first()
    #     if user:
    #         raise ValidationError('That phone number is taken. Please choose a different one.')

class DeliveryForm(FlaskForm):
    username = StringField('Name', validators=[DataRequired(),  Regexp(r'^[\w.@+-]+$', message="Username must not include spaces") ,Length(max=10, message="Should be less than 10 characters")])
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=10, message="Number must be 10 digits")])
    location = StringField('Location', validators=[DataRequired()])
    items = StringField('Items', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    # password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=16, message="Password must be less than 16 characters")])
    # confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Delivery Up')

    # def validate_phone(self, phone):
    #     user = User.query.filter_by(phone=phone.data).first()
    #     if user:
    #         raise ValidationError('That phone number is taken. Please choose a different one.')

# Form validation for item name 
class ItemForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50, message="This should be less than 50 characters")])
    price = IntegerField('Price', validators=[DataRequired()])
    description = StringField('Description', widget=TextArea(), validators=[DataRequired()])
    picture = FileField('Add a picture', validators=[ FileAllowed(['jpg', 'png','jpeg'])])
    link = StringField('Firebase Link')
    category = SelectField('Category', choices=[('Farm', 'Farm'), ('Herb','Herb'), ('Medication','Medication'), ('Corbs','Corbs'), ('Haemoglobin','Haemoglobin') ])
    other_pictures = MultipleFileField('Choose your other pictures',  validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Item')

class FarmForm(FlaskForm):
    name = StringField('Farm Name', validators=[Length(max=50, message="This should be less than 50 characters")])
    owner = StringField('Owner Name')
    email = StringField('Email', validators=[Length(max=50, message="This should be less than 50 characters")])
    size = StringField('Size')
    crop = StringField('Crop')
    location = StringField('Location')
    phone = StringField('Contact Number')
    price = IntegerField('Price')
    description = StringField('Tell us about your farm', widget=TextArea())
    picture = FileField('Add a picture', validators=[ FileAllowed(['jpg', 'png','jpeg'])])
    link = StringField('Firebase Link')
    # category = SelectField('Category', choices=[('Farm', 'Farm'), ('Herb','Herb'), ('Medication','Medication'), ('Corbs','Corbs'), ('Haemoglobin','Haemoglobin') ])
    other_pictures = MultipleFileField('Choose your other pictures',  validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Item')

class ExtensionForm(FlaskForm):
    name = StringField('Farm Name', validators=[Length(max=50, message="This should be less than 50 characters")])
    owner = StringField('Owner Name')
    email = StringField('Email', validators=[Length(max=50, message="This should be less than 50 characters")])
    size = StringField('Size')
    crop = StringField('Crop')
    location = StringField('Location')
    phone = StringField('Contact Number')
    price = IntegerField('Price')
    description = StringField('Tell us about your farm', widget=TextArea())
    picture = FileField('Add a picture', validators=[ FileAllowed(['jpg', 'png','jpeg'])])
    link = StringField('Firebase Link')
    # category = SelectField('Category', choices=[('Farm', 'Farm'), ('Herb','Herb'), ('Medication','Medication'), ('Corbs','Corbs'), ('Haemoglobin','Haemoglobin') ])
    other_pictures = MultipleFileField('Choose your other pictures',  validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Item')
 
class LoginForm(FlaskForm):
    phone = StringField('Phone', validators=[DataRequired(), Length(min=10, max=10, message="Number must be 10 digits")])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class Search(FlaskForm):
    search = StringField('Search', validators=[DataRequired()])
    submit = SubmitField('Search')

class InvestorForm(FlaskForm):
    name = StringField('Full Name', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    picture = FileField('Add a picture', validators=[ FileAllowed(['jpg', 'png','jpeg'])])
    size = IntegerField('Enter Land Size', validators=[DataRequired()])
    submit = SubmitField('Enter')