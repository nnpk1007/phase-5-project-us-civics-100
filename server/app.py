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


class CheckSession(Resource):
    
    def get(self):
        user_id = session.get("user_id")

        if user_id:
            user = User.query.filter(User.id == user_id).first()
            
            return user.to_dict(), 200
        else:

            return {}, 204

api.add_resource(CheckSession, '/check_session', endpoint='check_session')


class Login(Resource):
     
     def post(self):
        data = request.get_json()

        username = data.get("username")
        password = data.get("password")

        user = User.query.filter(User.username==username).first()

        if user and user.authenticate(password):
            session["user_id"] = user.id

            response = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }

            return response, 200

        return {"error": "Invalid username or password"}, 401

api.add_resource(Login, '/login', endpoint='login')


class Logout(Resource):

    def delete(self):
        if session.get["user_id"]:
            session["user_id"] = None

            return {}, 204

        return {"error": "Unauthorized"}, 401

api.add_resource(Logout, '/logout', endpoint='logout')


class Civics100Learning(Resource):

    def get(self):
        questions = Question.query.all()

        # create an empty list to store question-answer pairs
        question_answer_list = []

        for question in questions:
            # Retrieve the answers associated with each question
            answers = question.answers

            # Create a list to store the answer_texts (only correct answer)
            answer_texts = [answer.answer_text for answer in answers if answer.correct==1]

            # create a dictionary for the question_answer pair
            question_answer_pair = {
                "question_text": question.question_text,
                "answers": answer_texts
            }

            question_answer_list.append(question_answer_pair)

        return question_answer_list, 200

api.add_resource(Civics100Learning, "/civics100learning", endpoint="civics100learning")


@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

