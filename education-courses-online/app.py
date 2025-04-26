from flask import Flask, render_template, send_from_directory, request, redirect, url_for, flash
import os

app = Flask(__name__, 
    static_folder='ledu/assets',      # Serve static files from ledu/assets
    template_folder='ledu'            # Serve HTML templates from ledu
)

app.secret_key = 'your-secret-key-here'  # Required for flash messages

# Main routes
@app.route('/')
def home():
    return render_template('index-3.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/courses-list')
def courses_list():
    return render_template('courses-list.html')

@app.route('/courses-details')
def courses_details():
    return render_template('courses-details.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@app.route('/author')
def author():
    return render_template('author.html')

# Authentication routes
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        # Add your authentication logic here
        email = request.form.get('email')
        password = request.form.get('password')
        # Validate credentials
        # If valid, redirect to home
        return redirect(url_for('home'))
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Add your registration logic here
        email = request.form.get('email')
        password = request.form.get('password')
        # Create new user
        # If successful, redirect to signin
        return redirect(url_for('signin'))
    return render_template('signup.html')

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        # Add password reset logic here
        email = request.form.get('email')
        # Send reset email
        flash('Password reset instructions have been sent to your email.')
        return redirect(url_for('signin'))
    return render_template('forgot-password.html')

@app.route('/quiz')
def quiz():
    return render_template('Quiz.html')

# Error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

# Favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        os.path.join(app.static_folder, 'images'),
        'favicon.png',
        mimetype='image/png'
    )

if __name__ == '__main__':
    app.run(debug=True) 