from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired


class TodoForm(FlaskForm):
    task = StringField("Task", validators=[DataRequired()])

class RemoveForm(FlaskForm):
    task = StringField("Task", validators=[DataRequired()])
