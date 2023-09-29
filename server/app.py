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

        if not username or not email or not password:
            return {"error": "Unprocessable Entity"}, 422
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

            if isinstance(e, (IntegrityError)):
                for error in e.orig.args:
                    if "UNIQUE" in error:
                        errors.append("User name or email already taken. Please try again")

            return {'errors': errors}, 422

api.add_resource(Signup, "/signup", endpoint="signup")



@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

