from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(50), nullable=False)

    last_name = db.Column(db.String(50), nullable=False)

    grade_level = db.Column(db.Integer)

    attendance = db.Column(db.Float)

    average_grade = db.Column(db.Float)

    risk_level = db.Column(db.String(20))

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"