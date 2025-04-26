from app import create_app, db
from app.models import User, Course, Category, Lesson, Enrollment, Quiz, Question, Choice, Review
from werkzeug.security import generate_password_hash
from datetime import datetime

def init_db():
    app = create_app()
    with app.app_context():
        # Create tables
        db.create_all()

        # Create sample categories
        categories = [
            Category(name='Programming', description='Learn programming languages and software development'),
            Category(name='Data Science', description='Master data analysis and machine learning'),
            Category(name='Web Development', description='Build modern web applications'),
            Category(name='Business', description='Develop business and entrepreneurship skills'),
        ]
        db.session.add_all(categories)
        db.session.commit()

        # Create sample users
        admin = User(
            username='admin',
            email='admin@example.com',
            password_hash=generate_password_hash('admin123'),
            first_name='Admin',
            last_name='User',
            is_active=True
        )
        instructor = User(
            username='instructor',
            email='instructor@example.com',
            password_hash=generate_password_hash('instructor123'),
            first_name='John',
            last_name='Doe',
            is_active=True
        )
        student = User(
            username='student',
            email='student@example.com',
            password_hash=generate_password_hash('student123'),
            first_name='Jane',
            last_name='Smith',
            is_active=True
        )
        db.session.add_all([admin, instructor, student])
        db.session.commit()

        # Create sample courses
        courses = [
            Course(
                title='Python Programming Fundamentals',
                description='Learn the basics of Python programming language',
                instructor_id=instructor.id,
                price=49.99,
                duration='8 weeks',
                level='beginner',
                category_id=categories[0].id,
                created_at=datetime.utcnow()
            ),
            Course(
                title='Web Development with Flask',
                description='Build web applications using Flask framework',
                instructor_id=instructor.id,
                price=69.99,
                duration='10 weeks',
                level='intermediate',
                category_id=categories[2].id,
                created_at=datetime.utcnow()
            )
        ]
        db.session.add_all(courses)
        db.session.commit()

        # Create sample lessons
        lessons = [
            Lesson(
                title='Introduction to Python',
                content='Learn about Python basics, syntax, and data types',
                course_id=courses[0].id,
                order=1,
                duration=60
            ),
            Lesson(
                title='Control Flow',
                content='Learn about if statements, loops, and control structures',
                course_id=courses[0].id,
                order=2,
                duration=45
            )
        ]
        db.session.add_all(lessons)
        db.session.commit()

        # Create sample enrollment
        enrollment = Enrollment(
            student_id=student.id,
            course_id=courses[0].id,
            enrolled_at=datetime.utcnow(),
            progress=25.0
        )
        db.session.add(enrollment)
        db.session.commit()

        # Create sample review
        review = Review(
            course_id=courses[0].id,
            user_id=student.id,
            rating=5,
            comment='Great course! Very informative and well-structured.',
            created_at=datetime.utcnow()
        )
        db.session.add(review)
        db.session.commit()

        print('Database initialized with sample data!')

if __name__ == '__main__':
    init_db() 