# Education Courses Online Platform

A modern online education platform built with Flask, featuring course management, user authentication, and interactive learning features.

## Features

- User Authentication (Sign In/Sign Up)
- Course Catalog and Management
- Interactive Quiz System
- Responsive Design
- Dark/Light Theme Support
- Contact Form
- FAQ Section
- Testimonials
- Author Profiles

## Project Structure

```
education-courses-online/
│
├── app/                    # Application package
│   ├── __init__.py        # App initialization
│   ├── auth/              # Authentication blueprint
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── courses/           # Courses blueprint
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── main/             # Main blueprint
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models.py         # Database models
│   ├── static/           # Static files
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   └── templates/        # Jinja2 templates
│       ├── auth/
│       ├── courses/
│       └── base.html
│
├── migrations/           # Database migrations
├── instance/            # Instance-specific files
├── tests/               # Test suite
├── config.py            # Configuration
├── requirements.txt     # Python dependencies
└── run.py              # Application entry point
```

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd education-courses-online
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a .env file in the root directory with the following content:
```
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=your-super-secret-key-change-this
DATABASE_URL=sqlite:///education_courses.db

# Mail settings (optional)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-specific-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
```

5. Initialize the database:
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. Run the application:
```bash
flask run
```

The application will be available at `http://127.0.0.1:5000/`

## Development

- The application uses Flask's development server with debug mode enabled
- Database migrations are handled by Flask-Migrate
- Forms are created using Flask-WTF
- Authentication is managed by Flask-Login
- Static files are served from the `app/static` directory
- Templates are located in the `app/templates` directory

## Testing

Run the test suite:
```bash
python -m pytest
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 