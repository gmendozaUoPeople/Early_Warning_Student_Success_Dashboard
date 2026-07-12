from flask import Flask, render_template

from config import Config
from models import db, Student

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

    # Add sample students the first time the app runs
    if Student.query.count() == 0:
        students = [
            Student(
                first_name="Sahvanna",
                last_name="Mendoza",
                grade_level=10,
                attendance=95,
                average_grade=88,
                risk_level="Low"
            ),
            Student(
                first_name="Taylor",
                last_name="Young",
                grade_level=9,
                attendance=82,
                average_grade=67,
                risk_level="High"
            ),
            Student(
                first_name="Jordan",
                last_name="Schneider",
                grade_level=11,
                attendance=91,
                average_grade=79,
                risk_level="Moderate"
            )
        ]

        db.session.add_all(students)
        db.session.commit()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/students")
def students():

    student_list = Student.query.all()

    return render_template(
        "students.html",
        students=student_list
    )


if __name__ == "__main__":
    app.run(debug=True)