from flask.ext.wtf import Form
from wtforms import TextField
from wtforms.validators import Required
from app import app
app.config['SECRET_KEY'] ='HARD TO GUESS STRING'
class NameForm(Form):
    name = TextField('What is your name?? ' , validators = [Required()])
