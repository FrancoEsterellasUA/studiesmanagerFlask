from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

class Studies(db.Model):
    __tablename__= "studies"

    id= db.Column(db.Integer, primary_key=True)
    Topic = db.Column(db.String(50), nullable=False)
    Date= db.Column(db.Date, nullable=False)
    Information = db.Column(db.String(50), nullable=False)

    def __init__(self, Topic, Date, Information):
        self.Topic= Topic
        self.Date = Date
        self.Information = Information