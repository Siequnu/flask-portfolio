from flask import current_app
from app import db
from datetime import datetime

from app.models import User

class PortfolioUpload (db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(250))
	description = db.Column(db.String(500))
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	original_filename = db.Column(db.String(140))
	filename = db.Column(db.String(140))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.now())
	
	def __repr__(self):
		return '<Portfolio Upload {}>'.format(self.id)

	def add (self):
		db.session.add(self)
		db.session.commit()

	def save (self):
		db.session.commit()

	def delete (self):
		db.session.delete(self)
		db.session.commit()

def get_all_portfolios_info ():
	return PortfolioUpload.query.all()