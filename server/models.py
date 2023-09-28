from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Define the association table for the many-to-many relationship
user_question =  db.Table(
    "user_questions",
    db.Column("user_id", db.Integer, db.ForeignKey("user_id", primary_key=True)),
    db.Column("question_id", db.Integer, db.ForeignKey("question_id", primary_key=True))
)

