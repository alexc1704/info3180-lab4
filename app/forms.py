from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from wtforms import FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    
    
    
class UploadForm(FlaskForm):
    photo = FileField('Upload Image', validators=[
        DataRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])