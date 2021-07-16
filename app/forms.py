from flask_wtf import FlaskForm
from wtforms import TextField, TextAreaField, SubmitField, StringField
from wtforms.validators import Required, DataRequired, InputRequired



class RequestForm(FlaskForm):
    text = TextAreaField(validators=[DataRequired()])
    submit = SubmitField('Отправить')

class NameForm(FlaskForm):
    name = StringField('What is you name?', validators=[Required()])
    submit = SubmitField('Submit')

