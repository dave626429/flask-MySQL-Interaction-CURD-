from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, DecimalField
from wtforms.validators import DataRequired, EqualTo, Length

class AddEmployee(FlaskForm):
    name=StringField('Name',validators=[DataRequired(), Length(min=1,max=25)])
    designation=StringField('Designation',validators=[DataRequired(), Length(min=1,max=20)])
    address=StringField('Address', validators=[DataRequired(), Length(min=1,max=75)])
    phone=DecimalField('PhoneNumber', validators=[DataRequired()])
    submit=SubmitField('Submit')

class Search(FlaskForm):
    search=StringField('Search',validators=[DataRequired()])
    submit= SubmitField('Submit')

