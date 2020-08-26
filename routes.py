from flask import render_template, flash, redirect, url_for, request, abort, current_app, session, Response
from flask_login import current_user, login_required

from . import bp, models
from .models import PortfolioUpload
from .forms import PortfolioUploadForm

import app.models
from app.models import User

# Main portfolio overview
@bp.route("/")
@login_required
def view_portfolios():
	if app.models.is_admin(current_user.username):
		portfolios = models.get_all_portfolios_info ()
		return render_template('view_portfolios.html', portfolios = portfolios)

# View an invidual student's portfolio
@bp.route("/view/<int:student_id>")
@login_required
def view_portfolio(student_id):
	# #¡# Should check if is student as well
	if app.models.is_admin(current_user.username):
		portfolio_uploads = PortfolioUpload.query.filter_by (owner_id = student_id).all ()
		return render_template('view_portfolio.html', portfolio_uploads = portfolio_uploads)
