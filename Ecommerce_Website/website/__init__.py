import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

load_dotenv()

db = SQLAlchemy()
DB_NAME = 'database.sqlite3'

def create_database(app):
    from .models import Customer, Employee, Cart, Product, Order, Wishlist, CustomerReturn
    from werkzeug.security import generate_password_hash

    db.create_all()
    print('Database Created')

    admin_email = os.getenv('ADMIN_EMAIL')
    employee_exists = Employee.query.filter_by(email=admin_email).first()
    if not employee_exists:
        default_employee = Employee(
            email=admin_email,
            first_name=os.getenv('ADMIN_FIRST_NAME'),
            last_name=os.getenv('ADMIN_LAST_NAME'),
            role='Super Admin',
            password_hash=generate_password_hash(os.getenv('ADMIN_PASSWORD'))
        )
        db.session.add(default_employee)
        db.session.commit()
        print('Default employee account synchronized successfully!')

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['WTF_CSRF_ENABLED'] = False
    
    app.config['REMEMBER_COOKIE_DURATION'] = 86400
    app.config['SESSION_COOKIE_HTTPONLY'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'

    # ---------------------------------------------------------
    # 📝 STARLIGHTTECH LOGGING CONFIGURATION SETUP
    # ---------------------------------------------------------
    if not os.path.exists('logs'):
        os.mkdir('logs')
        
    file_handler = RotatingFileHandler('logs/starlighttech.log', maxBytes=5242880, backupCount=5)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    console_handler.setLevel(logging.INFO)
    
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    app.logger.setLevel(logging.INFO)
    
    app.logger.info('StarlightTech startup initialized successfully')
    # ---------------------------------------------------------

    db.init_app(app)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html')

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .models import Customer, Employee, Cart, Product, Order, Wishlist, CustomerReturn

    @login_manager.user_loader
    def load_user(id):
        user_type = session.get('user_type')
        if user_type == 'employee':
            return Employee.query.get(int(id))
        return Customer.query.get(int(id))

    from .views import views
    from .auth import auth  
    from .admin import admin

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(admin, url_prefix='/')

    with app.app_context():
        create_database(app)

    return app
