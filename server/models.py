from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Define the association table for the many-to-many relationship
user_question =  db.Table(
    "user_questions",
    db.Column("user_id", db.Integer, db.ForeignKey("user.id", primary_key=True)),
    db.Column("question_id", db.Integer, db.ForeignKey("question.id", primary_key=True))
)


# USer Model
class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    # many-to-many relationship with Question
    questions_attempted = db.relationship("Question", secondary=user_question, back_populates="users_attempted")

    def __repr__(self):
        return f"User \
            id : {self.id} \
            username: {self.username} \
            email: {self.email} \
            "

    