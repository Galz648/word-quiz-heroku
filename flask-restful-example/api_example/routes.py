
""" File containing flask application routes """

from flask import request, render_template, make_response, jsonify
from datetime import datetime as dt
from flask import current_app as app
from .models import db, UserModel # database related imports
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
import json
api = Api(app)


user_post_args = reqparse.RequestParser()
user_post_args.add_argument("email", 
                            type=str, 
                            help="email of the user to be created is required", 
                            required=True,
                            location='json'
                            )

response_marshaller = {
    "email": fields.String
}

#resource_fields = {
#	'response': fields.Nested(parameter_marshaller)
#}

   
class UserApi(Resource):
    @marshal_with(response_marshaller)
    def post(self):
        """Create a user via query string parameters."""
        args = user_post_args.parse_args()
        if args['email']:
            email = args['email']
            print(f'arg email: {email}')
            existing_user = UserModel.query.filter(
                UserModel.email == email).first()

            print(f'existing user: {existing_user}')
            print(f'bool: {bool(existing_user)}')
            if existing_user:
                print('\n user already exists\n')
                data = {'email': existing_user.email}
                


            print('\ncreating new user\n')
            new_user = UserModel(
                email=email,
                created=dt.now(),
                admin=False
            )
            db.session.add(new_user)  # Adds new UserModel record to database
            db.session.commit()  # Commits all changes

            data = {'email': new_user.email}
            return data



    
api.add_resource(UserApi, "/user")
