from app import create_app, db
from app.models import User, Course, Category, Lesson, Enrollment, Quiz, Question, Choice, Review

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Course': Course,
        'Category': Category,
        'Lesson': Lesson,
        'Enrollment': Enrollment,
        'Quiz': Quiz,
        'Question': Question,
        'Choice': Choice,
        'Review': Review
    }

if __name__ == '__main__':
    app.run(debug=True) 