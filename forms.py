from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField, SelectField, DateField, SelectMultipleField, BooleanField, FormField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length

class PortfolioUploadForm(FlaskForm):
	portfolio_upload_file = FileField(label='File:')
	title = StringField('File title:', validators=[DataRequired(), Length(max=250)])
	description = StringField('Description:', validators=[Length(max=500)])
	submit = SubmitField('Upload new file')
