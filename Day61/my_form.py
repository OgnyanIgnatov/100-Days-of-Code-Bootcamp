from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email

class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Not a valid format")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="You should have at least 8 charachters")])
    submit = SubmitField(label='Log In')