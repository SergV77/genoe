from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, StringField
from wtforms.validators import Required



class RequestForm(FlaskForm):
    text = StringField(label="Симптомы:", validators=[Required()])
    submit = SubmitField('Отправить', id="btn btn-primary")


