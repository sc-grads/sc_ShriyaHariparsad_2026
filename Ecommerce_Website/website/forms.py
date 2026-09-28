from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, EmailField, BooleanField, SubmitField, FloatField, SelectField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange, Regexp, Optional, Email
from flask_wtf.file import FileField, FileRequired 

class SignUpForm(FlaskForm):   
    first_name = StringField('First Name', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]+$', message="First name must contain letters only.")
    ])
    last_name = StringField('Last Name', validators=[
        DataRequired(),
        Regexp(r'^[A-Za-z\s]+$', message="Last name must contain letters only.")
    ])
    email = EmailField('Email', validators=[
        DataRequired(),
        Email(message="Please enter a valid email address.")
    ])
    id_number = StringField('ID Number', validators=[
        DataRequired(), 
        Length(min=13, max=13, message="ID number must be exactly 13 digits."),
        Regexp(r'^\d+$', message="ID number must contain only numbers.")
    ])
    password1 = PasswordField('Enter Your Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirm Your Password', validators=[DataRequired(), Length(min=6)])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Enter Your Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

class PasswordChangeForm(FlaskForm):
    current_password = PasswordField('Current Password', validators=[DataRequired(), Length(min=6)])
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=6)])
    confirm_new_password = PasswordField('Confirm New Password', validators=[DataRequired(), Length(min=6)])
    change_password = SubmitField('Change Password') 

class ShopItemsForm(FlaskForm):
    product_name = StringField('Name of Product', validators=[DataRequired()])
    
    category = SelectField('Category', choices=[
        ('Phones & Tablets', 'Phones & Tablets'),
        ('Laptops & Computers', 'Laptops & Computers'),
        ('Audio & Headphones', 'Audio & Headphones'),
        ('TV & Home Theater', 'TV & Home Theater'),
        ('Smart Home & Security', 'Smart Home & Security'),
        ('Gaming & Consoles', 'Gaming & Consoles'),
        ('Accessories & Power', 'Accessories & Power')
    ], validators=[DataRequired()])
    
    current_price = FloatField('Current Price', validators=[DataRequired()])
    previous_price = FloatField('Previous Price', validators=[Optional()])
    in_stock = IntegerField('In Stock', validators=[InputRequired(), NumberRange(min=0)])
    product_picture = FileField('Product Picture')
    flash_sale = BooleanField('Flash Sale')

    add_product = SubmitField('Add Product')
    update_product = SubmitField('Update')
