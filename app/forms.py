from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, StringField
from wtforms.validators import Required



class RequestForm(FlaskForm):
    text = TextAreaField(validators=[Required()])
    submit = SubmitField('Отправить')

class NameForm(FlaskForm):
    name = StringField('What is you name?', validators=[Required()])
    submit = SubmitField('Submit')

