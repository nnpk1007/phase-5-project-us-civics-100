from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime

from config import db, bcrypt

# Define the association table for the many-to-many relationship
user_question =  db.Table(
    "user_questions",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id", primary_key=True)),
    db.Column("question_id", db.Integer, db.ForeignKey("questions.id", primary_key=True))
)


# User Model
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    # many-to-many relationship with Question
    questions_attempted = db.relationship("Question", secondary=user_question, back_populates="users_attempted")

    @hybrid_property
    def password_hash(self):
        return self._password_hash
        raise Exception("Cannot access password hash")

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def __repr__(self):
        return f"User \
            id : {self.id} \
            username: {self.username} \
            email: {self.email} \
            "


# Question Model
class Question(db.Model, SerializerMixin):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String)

    # many-to-many relationship with User
    users_attempted = db.relationship("User", secondary=user_question, back_populates="questions_attempted")

    # one-to-many relationship with Answer
    answers = db.relationship("Answer", backref="question")

    def __repr__(self):
        return f"Question \
            id: {self.id} \
            question_text: {self.question_text} "  


# Answer Model
class Answer(db.Model, SerializerMixin):
    __tablename__ = "answers"

    id = db.Column(db.Integer, primary_key=True)
    answer_text = db.Column(db.String)
    correct = db.Column(db.Boolean, default=False)

    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))

    def __repr__(self):
        return f"Answer \
            id: {self.id} \
            answer_text: {self.answer_text} \
            correct: {self.correct} \
            question_id: {self.question_id}"


# QuizAttempt Model
class QuizAttempt(db.Model, SerializerMixin):
    __tablename__ = "quiz_attempts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    quiz_date = db.Column(db.DateTime, default=datetime.utcnow)
    score = db.Column(db.Integer)
    questions_attempted = db.Column(db.Integer)

    def __repr__(self):
        return f"QuizAttempt \
            id: {self.id} \
            user_id: {self.user_id} \
            quiz_date: {self.quiz_date} \
            score: {self.score} \
            questions_attempted: {self.questions_attempted}"