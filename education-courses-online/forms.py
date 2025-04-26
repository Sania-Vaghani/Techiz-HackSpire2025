from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SelectField, FloatField, FileField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from models import User

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=64)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=64)])
    
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
            
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

class CourseForm(FlaskForm):
    title = StringField('Course Title', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Course Description', validators=[DataRequired()])
    price = FloatField('Price', validators=[DataRequired()])
    duration = StringField('Duration', validators=[DataRequired()])
    level = SelectField('Level', choices=[
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced')
    ])
    category_id = SelectField('Category', coerce=int)
    image = FileField('Course Image')

class LessonForm(FlaskForm):
    title = StringField('Lesson Title', validators=[DataRequired(), Length(max=200)])
    content = TextAreaField('Lesson Content', validators=[DataRequired()])
    order = IntegerField('Lesson Order', validators=[DataRequired()])
    duration = IntegerField('Duration (minutes)', validators=[DataRequired()])

class CategoryForm(FlaskForm):
    name = StringField('Category Name', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Category Description')

class QuizForm(FlaskForm):
    title = StringField('Quiz Title', validators=[DataRequired(), Length(max=200)])

class QuestionForm(FlaskForm):
    question_text = TextAreaField('Question', validators=[DataRequired()])
    question_type = SelectField('Question Type', choices=[
        ('multiple_choice', 'Multiple Choice'),
        ('true_false', 'True/False')
    ])

class ChoiceForm(FlaskForm):
    choice_text = TextAreaField('Choice', validators=[DataRequired()])
    is_correct = BooleanField('Correct Answer')

class ReviewForm(FlaskForm):
    rating = SelectField('Rating', choices=[(str(i), str(i)) for i in range(1, 6)], validators=[DataRequired()])
    comment = TextAreaField('Comment', validators=[DataRequired()])

class ProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    first_name = StringField('First Name', validators=[DataRequired(), Length(max=64)])
    last_name = StringField('Last Name', validators=[DataRequired(), Length(max=64)])
    current_password = PasswordField('Current Password')
    new_password = PasswordField('New Password', validators=[Length(min=6)])
    confirm_password = PasswordField('Confirm New Password', validators=[EqualTo('new_password')])

    def __init__(self, original_username, original_email, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username
        self.original_email = original_email

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        if email.data != self.original_email:
            user = User.query.filter_by(email=email.data).first()
            if user is not None:
                raise ValidationError('Please use a different email address.') 