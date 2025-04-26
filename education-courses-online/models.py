from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    enrolled_courses = db.relationship('Enrollment', back_populates='student')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
        
    def __repr__(self):
        return f'<User {self.username}>'

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    instructor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    price = db.Column(db.Float)
    duration = db.Column(db.String(50))  # e.g., "6 weeks"
    level = db.Column(db.String(20))  # beginner, intermediate, advanced
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    image_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    instructor = db.relationship('User', backref='courses_taught')
    category = db.relationship('Category', back_populates='courses')
    enrollments = db.relationship('Enrollment', back_populates='course')
    lessons = db.relationship('Lesson', back_populates='course', order_by='Lesson.order')
    
    def __repr__(self):
        return f'<Course {self.title}>'

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text)
    
    # Relationships
    courses = db.relationship('Course', back_populates='category')
    
    def __repr__(self):
        return f'<Category {self.name}>'

class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    order = db.Column(db.Integer)  # Order within the course
    duration = db.Column(db.Integer)  # Duration in minutes
    
    # Relationships
    course = db.relationship('Course', back_populates='lessons')
    
    def __repr__(self):
        return f'<Lesson {self.title}>'

class Enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)
    progress = db.Column(db.Float, default=0.0)  # Percentage completed
    
    # Relationships
    student = db.relationship('User', back_populates='enrolled_courses')
    course = db.relationship('Course', back_populates='enrollments')
    
    def __repr__(self):
        return f'<Enrollment {self.student_id} in {self.course_id}>'

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lesson.id'))
    
    # Relationships
    questions = db.relationship('Question', back_populates='quiz')
    lesson = db.relationship('Lesson', backref='quizzes')
    
    def __repr__(self):
        return f'<Quiz {self.title}>'

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))
    question_text = db.Column(db.Text, nullable=False)
    question_type = db.Column(db.String(20))  # multiple_choice, true_false, etc.
    
    # Relationships
    quiz = db.relationship('Quiz', back_populates='questions')
    choices = db.relationship('Choice', back_populates='question')
    
    def __repr__(self):
        return f'<Question {self.question_text[:20]}...>'

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    choice_text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False)
    
    # Relationships
    question = db.relationship('Question', back_populates='choices')
    
    def __repr__(self):
        return f'<Choice {self.choice_text[:20]}...>'

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    rating = db.Column(db.Integer)  # 1-5 stars
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    course = db.relationship('Course', backref='reviews')
    user = db.relationship('User', backref='reviews')
    
    def __repr__(self):
        return f'<Review {self.rating} stars by {self.user_id}>' 