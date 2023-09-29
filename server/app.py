#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, session
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

# Local imports
from config import app, db, api
from models import User, Question, Answer, QuizAttempt



class Signup(Resource):

    def post(self):
        data = request.get_json()
        
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")
        password_confirmation = data.get("password_confirmation")

        errors = []
        
        # Check if required fields are missing
        if not username or not email or not password or not password_confirmation:
            errors.append("All fields are required")
        
        # Check if password and password_confirmation match
        if password != password_confirmation:
            errors.append("Password confirmation failed")

        if errors:
            return {"errors": errors}, 422

        # Save a new user to databse 
        new_user = User(username="username", email="email")
        new_user.password_hash = password 

        try:
            db.session.add(new_user)
            db.session.commit()
            
            session["user_id"] = new_user.id

            return new_user.to_dict(), 201
            
        except IntegrityError as e:
            errors = []
            
            # Check if the error is an IntegrityError or DataError            
            if isinstance(e, (IntegrityError)):
                for error in e.orig.args:
                    if "UNIQUE" in error:
                        errors.append("User name or email is already taken. Please try again")

            return {'errors': errors}, 422

api.add_resource(Signup, "/signup", endpoint="signup")



@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

