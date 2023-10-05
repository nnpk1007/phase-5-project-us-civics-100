#!/usr/bin/env python3
import random

from flask import request, session, jsonify
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from random import sample

from config import app, db, api
from models import User, Question, Answer, QuizAttempt


class Signup(Resource):
    def post(self):
        data = request.get_json()

        username = data["username"]
        email = data["email"]
        password = data["password"]
        password_confirmation = data["passwordConfirmation"]

        errors = []

        # Check if required fields are missing
        if not username or not email or not password or not password_confirmation:
            errors.append("All fields are required")

        # Check if password and password_confirmation match
        if password != password_confirmation:
            errors.append("Password confirmation failed")

        try:
            new_user = User(username=username, email=email)
            new_user.password_hash = password
            new_user.validate_email(key="email", address=email)
            new_user.validate_password(key="password", password=password)

        except ValueError as e:
            errors.append(str(e))

        if errors:
            return {"errors": errors}, 422

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
                        errors.append(
                            "User name or email is already taken. Please try again"
                        )

            return {"errors": errors}, 422


api.add_resource(Signup, "/signup", endpoint="signup")


@app.route("/authorized", methods=["GET"])
def authorized():
    user = User.query.filter(User.id == session.get("user_id")).first()
    if user:
        response = {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }

        return response
    else:
        return {"errors": ["Unauthorized"]}, 401


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    user = User.query.filter(User.username == username).first()
    print(user)

    if user:
        if user.authenticate(password):
            session["user_id"] = user.id

            response = {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }

            return response, 200
        else:
            return {"errors": ["Invalid password"]}, 401
    else:
        return {"errors": "Invalid username or password"}, 401


class Logout(Resource):
    def delete(self):
        if session.get("user_id"):
            session["user_id"] = None
            return {}, 204

        return {"error": "Unauthorized"}, 401


api.add_resource(Logout, "/logout", endpoint="logout")


class Civics100Learning(Resource):
    def get(self):
        questions = Question.query.all()

        # create an empty list to store question-answer pairs
        question_answer_list = []

        for question in questions:
            # Retrieve the answers associated with each question
            answers = question.answers

            # Create a list to store the answer_texts (only correct answer)
            answer_texts = [
                answer.answer_text for answer in answers if answer.correct == 1
            ]

            # create a dictionary for the question_answer pair
            question_answer_pair = {
                "question_text": question.question_text,
                "answers": answer_texts,
            }

            question_answer_list.append(question_answer_pair)

        return question_answer_list, 200


api.add_resource(
    Civics100Learning, "/civics100-learning", endpoint="civics100-learning"
)


#  Generate a list of random questions from the database.
def generate_random_question(number_of_questions):
    all_questions = Question.query.all()

    random_questions = sample(all_questions, number_of_questions)

    return random_questions


class CivicsTest(Resource):
    def get(self):
        questions = generate_random_question(10)
        # print("questions generated:", questions)

        # create an empty list to store question-answer pairs
        question_answer_list = []

        for question in questions:
            # Retrieve the answers associated with each question
            answers = question.answers

            # create the answer options list
            answers_option = [
                {"answer_text": answer.answer_text, "correct": answer.correct}
                for answer in answers
            ]

            # shuffle the answers_option in random order
            random.shuffle(answers_option)

            # create the question object
            question_object = {
                "question_text": question.question_text,
                "answer_options": answers_option,
            }

            question_answer_list.append(question_object)
        return question_answer_list, 200


api.add_resource(CivicsTest, "/civics-test", endpoint="civics-test")


@app.route("/submit-quiz-attempt", methods=["POST"])
def submit_quiz_attempt():
    data = request.get_json()

    user_id = data.get("user_id")
    score = data.get("score")
    questions_attempted = data.get("questions_attempted")

    quiz_attempt = QuizAttempt(
        user_id=user_id, score=score, questions_attempted=questions_attempted
    )

    db.session.add(quiz_attempt)
    db.session.commit()

    return quiz_attempt.to_dict(), 201


@app.route("/quiz-attempts/<int:user_id>", methods=["GET"])
def get_quiz_attempts(user_id):
    quiz_attempts = QuizAttempt.query.filter_by(user_id=user_id).all()

    quiz_attempts_data = [attempt.to_dict() for attempt in quiz_attempts]

    return jsonify(quiz_attempts_data), 200


if __name__ == "__main__":
    app.run(port=5555, debug=True)
