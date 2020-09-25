
""" File containing flask application routes """

from flask import request, render_template, make_response
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User # database related imports



@app.route('/user/create', methods=['GET'])
def create_user():
    """Create a user via query string parameters."""
    email = request.args.get('email')
    if email:
        existing_user = User.query.filter(
            User.email == email).first()
        
        if existing_user:
            return make_response(f'"{email}" already created!')
        
        new_user = User(
            email=email,
            created=dt.now(),
            admin=False
        )
        db.session.add(new_user)  # Adds new User record to database
        db.session.commit()  # Commits all changes
        
        return make_response(f"{new_user} successfully created!")