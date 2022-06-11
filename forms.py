from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

choices = [["morning", "afternoon", "evening"], ["indoor", "outdoor"]]


class AddActivityForm(FlaskForm):
    activity = StringField(label="Activity", validators=[DataRequired()])
    time_of_the_day = SelectField(label="Time of the day", choices=choices[0], validators=[DataRequired()])
    type = SelectField(label="Type of the activity", choices=choices[1], validators=[DataRequired()])
    location = StringField(label="Location")
    submit = SubmitField("Add New Activity")
