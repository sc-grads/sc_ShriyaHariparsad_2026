from . import db
from flask_login import UserMixin
from datetime import datetime, timezone, timedelta

def get_sast_time():
    return datetime.now(timezone(timedelta(hours=2)))

class Customer(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    id_number = db.Column(db.String(13), unique=True, nullable=False) 
    password_hash = db.Column(db.String(150), nullable=False)
    date_joined = db.Column(db.DateTime, default=get_sast_time)
    
    # NEW DELIVERY COLUMNS SITTING STABLY HERE
    street_address = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(100), nullable=True)
    postal_code = db.Column(db.String(20), nullable=True)

    cart_items = db.relationship('Cart', backref=db.backref('customer', lazy=True))
    order = db.relationship('Order', backref=db.backref('customer', lazy=True))

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return f'<Customer %r>' % self.id


class Employee(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='Admin') 
    password_hash = db.Column(db.String(150), nullable=False)
    date_joined = db.Column(db.DateTime, default=get_sast_time)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute.')

    @password.setter
    def password(self, password):
        from werkzeug.security import generate_password_hash
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password_hash, password)

    def __str__(self):
        return f'<Employee %r>' % self.id


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(100), nullable=False) 
    current_price = db.Column(db.Float, nullable=False)
    previous_price = db.Column(db.Float, nullable=True)
    in_stock = db.Column(db.Integer, nullable=False)
    product_picture = db.Column(db.String(1000), nullable=False)
    flash_sale = db.Column(db.Boolean, default=False)
    date_added = db.Column(db.DateTime, default=get_sast_time)

    carts = db.relationship('Cart', backref=db.backref('product', lazy=True))
    orders = db.relationship('Order', backref=db.backref('product', lazy=True))

    def __str__(self):
        return '<Product %r>' % self.product_name


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    customer_link = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_link = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __str__(self):
        return '<Cart %r>' % self.id


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(100), nullable=False)
    payment_id = db.Column(db.String(1000), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
    date_ordered = db.Column(db.DateTime, default=get_sast_time)

    customer_link = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_link = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    def __str__(self):
        return '<Order %r>' % self.id


class Wishlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    customer_link = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    product_link = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

    product = db.relationship('Product', backref=db.backref('wishlists', lazy=True))

    def __str__(self):
        return '<Wishlist %r>' % self.id


class CustomerReturn(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reason = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(100), nullable=False, default='Pending Review')
    date_logged = db.Column(db.DateTime, default=db.func.current_timestamp())

    order_link = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    order = db.relationship('Order', backref=db.backref('returns_logged', lazy=True))

    def __str__(self):
        return '<CustomerReturn %r>' % self.id







    

