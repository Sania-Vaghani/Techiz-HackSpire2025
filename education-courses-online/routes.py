from flask import render_template, flash, redirect, url_for, request, jsonify
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from forms import (LoginForm, RegistrationForm, CourseForm, LessonForm, CategoryForm,
                  QuizForm, QuestionForm, ChoiceForm, ReviewForm, ProfileForm)
from models import User, Course, Category, Lesson, Enrollment, Quiz, Question, Choice, Review

@app.route('/')
@app.route('/index')
def index():
    courses = Course.query.order_by(Course.created_at.desc()).limit(6).all()
    categories = Category.query.all()
    return render_template('index.html', courses=courses, categories=categories)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data,
                   first_name=form.first_name.data, last_name=form.last_name.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Register', form=form)

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm(current_user.username, current_user.email)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        if form.new_password.data:
            current_user.set_password(form.new_password.data)
        db.session.commit()
        flash('Your profile has been updated.')
        return redirect(url_for('profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
    return render_template('auth/profile.html', title='Profile', form=form)

@app.route('/course/new', methods=['GET', 'POST'])
@login_required
def create_course():
    form = CourseForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        course = Course(title=form.title.data, description=form.description.data,
                       price=form.price.data, duration=form.duration.data,
                       level=form.level.data, category_id=form.category_id.data,
                       instructor_id=current_user.id)
        db.session.add(course)
        db.session.commit()
        flash('Your course has been created!')
        return redirect(url_for('course', course_id=course.id))
    return render_template('course/create.html', title='Create Course', form=form)

@app.route('/course/<int:course_id>')
def course(course_id):
    course = Course.query.get_or_404(course_id)
    return render_template('course/view.html', course=course)

@app.route('/course/<int:course_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    if course.instructor_id != current_user.id:
        abort(403)
    form = CourseForm()
    form.category_id.choices = [(c.id, c.name) for c in Category.query.all()]
    if form.validate_on_submit():
        course.title = form.title.data
        course.description = form.description.data
        course.price = form.price.data
        course.duration = form.duration.data
        course.level = form.level.data
        course.category_id = form.category_id.data
        db.session.commit()
        flash('Your course has been updated!')
        return redirect(url_for('course', course_id=course.id))
    elif request.method == 'GET':
        form.title.data = course.title
        form.description.data = course.description
        form.price.data = course.price
        form.duration.data = course.duration
        form.level.data = course.level
        form.category_id.data = course.category_id
    return render_template('course/edit.html', title='Edit Course', form=form, course=course)

@app.route('/course/<int:course_id>/lesson/new', methods=['GET', 'POST'])
@login_required
def create_lesson(course_id):
    course = Course.query.get_or_404(course_id)
    if course.instructor_id != current_user.id:
        abort(403)
    form = LessonForm()
    if form.validate_on_submit():
        lesson = Lesson(title=form.title.data, content=form.content.data,
                       order=form.order.data, duration=form.duration.data,
                       course_id=course.id)
        db.session.add(lesson)
        db.session.commit()
        flash('Your lesson has been created!')
        return redirect(url_for('course', course_id=course.id))
    return render_template('lesson/create.html', title='Create Lesson', form=form, course=course)

@app.route('/course/<int:course_id>/enroll', methods=['POST'])
@login_required
def enroll(course_id):
    course = Course.query.get_or_404(course_id)
    if current_user.is_enrolled(course):
        flash('You are already enrolled in this course.')
        return redirect(url_for('course', course_id=course.id))
    enrollment = Enrollment(student_id=current_user.id, course_id=course.id)
    db.session.add(enrollment)
    db.session.commit()
    flash('You have successfully enrolled in the course!')
    return redirect(url_for('course', course_id=course.id))

@app.route('/course/<int:course_id>/review', methods=['GET', 'POST'])
@login_required
def review_course(course_id):
    course = Course.query.get_or_404(course_id)
    if not current_user.is_enrolled(course):
        flash('You must be enrolled in the course to review it.')
        return redirect(url_for('course', course_id=course.id))
    form = ReviewForm()
    if form.validate_on_submit():
        review = Review(rating=form.rating.data, comment=form.comment.data,
                       user_id=current_user.id, course_id=course.id)
        db.session.add(review)
        db.session.commit()
        flash('Your review has been submitted!')
        return redirect(url_for('course', course_id=course.id))
    return render_template('course/review.html', title='Review Course', form=form, course=course)

@app.route('/categories')
def categories():
    categories = Category.query.all()
    return render_template('category/list.html', categories=categories)

@app.route('/category/<int:category_id>')
def category(category_id):
    category = Category.query.get_or_404(category_id)
    courses = Course.query.filter_by(category_id=category.id).all()
    return render_template('category/view.html', category=category, courses=courses)

@app.route('/search')
def search():
    query = request.args.get('q', '')
    courses = Course.query.filter(
        Course.title.ilike(f'%{query}%') | Course.description.ilike(f'%{query}%')
    ).all()
    return render_template('search.html', courses=courses, query=query)

@app.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_instructor():
        courses = Course.query.filter_by(instructor_id=current_user.id).all()
        return render_template('dashboard/instructor.html', courses=courses)
    else:
        enrollments = current_user.enrollments
        return render_template('dashboard/student.html', enrollments=enrollments) 