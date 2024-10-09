from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class QA(db.Model):
    __tablename__ = 'questions_answers'

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text, nullable=False)

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

