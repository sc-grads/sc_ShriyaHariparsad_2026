import os
import re
from flask import Blueprint, render_template, flash, redirect, url_for, request, jsonify, current_app 
from .forms import LoginForm, SignUpForm, PasswordChangeForm
from .models import Customer, Employee, Product, Cart, Wishlist
from .import db
from flask_login import login_user, login_required, logout_user, current_user
from flask import session

auth = Blueprint('auth', __name__)

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        id_number = form.id_number.data
        password1 = form.password1.data
        password2 = form.password2.data

        if password1 == password2:
            new_customer = Customer()
            new_customer.email = email
            new_customer.first_name = first_name
            new_customer.last_name = last_name
            new_customer.id_number = id_number
            new_customer.password = password2

            if 'guest_address' in session:
                new_customer.street_address = session.get('guest_address', '')
                new_customer.city = session.get('guest_city', '')
                new_customer.postal_code = session.get('guest_postal_code', '')

            try:
                db.session.add(new_customer)
                db.session.commit()
                current_app.logger.info(f"New User Registration: Customer account successfully created for {email}")

                session.pop('guest_address', None)
                session.pop('guest_city', None)
                session.pop('guest_postal_code', None)

                if 'guest_wishlist' in session and session['guest_wishlist']:
                    try:
                        for wish_item_id in session['guest_wishlist']:
                            wish_id = int(wish_item_id)
                            wish_exists = Wishlist.query.filter_by(product_link=wish_id, customer_link=new_customer.id).first()
                            if not wish_exists:
                                new_wish_item = Wishlist()
                                new_wish_item.product_link = wish_id
                                new_wish_item.customer_link = new_customer.id
                                db.session.add(new_wish_item)
                        db.session.commit()
                        session.pop('guest_wishlist', None)
                    except Exception as wishlist_merge_error:
                        db.session.rollback()
                        current_app.logger.error(f"Wishlist Merge Exception during Sign Up for {email} - Error: {str(wishlist_merge_error)}")

                if 'guest_cart' in session and session['guest_cart']:
                    try:
                        for item_id_str, qty in session['guest_cart'].items():
                            item_id = int(item_id_str)
                            product_info = db.session.get(Product, item_id)
                            
                            if not product_info:
                                continue

                            new_cart_item = Cart()
                            if qty > product_info.in_stock:
                                new_cart_item.quantity = product_info.in_stock
                            else:
                                new_cart_item.quantity = qty
                            new_cart_item.product_link = item_id
                            new_cart_item.customer_link = new_customer.id
                            db.session.add(new_cart_item)

                            wish_to_clear = Wishlist.query.filter_by(product_link=item_id, customer_link=new_customer.id).first()
                            if wish_to_clear:
                                db.session.delete(wish_to_clear)

                        db.session.commit()
                        session.pop('guest_cart', None)
                        login_user(new_customer, remember=True)
                        session['user_type'] = 'customer'
                        return redirect(url_for('views.show_cart'))
                    except Exception as merge_error:
                        db.session.rollback()
                        current_app.logger.error(f"Cart Merge Exception during Sign Up for {email} - Error: {str(merge_error)}")

                flash('Account Created Successfully, You can now Login', category='success')
                return redirect(url_for('auth.login'))
            except Exception as e:
                db.session.rollback()
                current_app.logger.warning(f"Registration Blocked: Duplicate email or ID attempt for {email}")
                flash('Account Not Created!!, Email or ID number already exists', category='error')

            form.email.data = ''
            form.first_name.data = ''
            form.last_name.data = ''
            form.id_number.data = ''
            form.password1.data = ''
            form.password2.data = ''

    return render_template('signup.html', form=form)




@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data

        customer = Customer.query.filter_by(email=email).first()
        if customer:
            if customer.verify_password(password=password):
                session['user_type'] = 'customer'
                login_user(customer, remember=True)
                current_app.logger.info(f"Session Authenticated: Customer {email} logged in")

                if 'guest_address' in session and session['guest_address']:
                    try:
                        customer.street_address = session.pop('guest_address')
                        customer.city = session.pop('guest_city', customer.city)
                        customer.postal_code = session.pop('guest_postal_code', customer.postal_code)
                        db.session.commit()
                    except Exception as addr_error:
                        db.session.rollback()
                        current_app.logger.error(f"Address Merge Exception during Login for {email} - Error: {str(addr_error)}")
                else:
                    session.pop('guest_address', None)
                    session.pop('guest_city', None)
                    session.pop('guest_postal_code', None)

                if 'guest_wishlist' in session and session['guest_wishlist']:
                    try:
                        for wish_item_id in session['guest_wishlist']:
                            wish_id = int(wish_item_id)
                            wish_exists = Wishlist.query.filter_by(product_link=wish_id, customer_link=customer.id).first()
                            if not wish_exists:
                                new_wish_item = Wishlist()
                                new_wish_item.product_link = wish_id
                                new_wish_item.customer_link = customer.id
                                db.session.add(new_wish_item)
                        db.session.commit()
                        session.pop('guest_wishlist', None)
                    except Exception as wishlist_merge_error:
                        db.session.rollback()
                        current_app.logger.error(f"Wishlist Merge Exception during Login for {email} - Error: {str(wishlist_merge_error)}")

                if 'guest_cart' in session and session['guest_cart']:
                    try:
                        for item_id_str, qty in session['guest_cart'].items():
                            item_id = int(item_id_str)
                            item_exists = Cart.query.filter_by(product_link=item_id, customer_link=customer.id).first()
                            
                            if item_exists:
                                item_exists.quantity = item_exists.quantity + qty
                            else:
                                new_cart_item = Cart()
                                new_cart_item.quantity = qty
                                new_cart_item.product_link = item_id
                                new_cart_item.customer_link = customer.id
                                db.session.add(new_cart_item)

                            wish_to_clear = Wishlist.query.filter_by(product_link=item_id, customer_link=customer.id).first()
                            if wish_to_clear:
                                db.session.delete(wish_to_clear)

                        db.session.commit()
                        session.pop('guest_cart', None)
                    except Exception as e:
                        db.session.rollback()
                        current_app.logger.error(f"Cart Merge Exception: Failed moving guest cart to registry for {email} - Error: {str(e)}")

                    return redirect(url_for('views.show_cart'))

                return redirect(url_for('views.home'))
            else:
                current_app.logger.warning(f"Failed Login Attempt: Incorrect password entered for customer account {email}")
                flash('Incorrect Email or Password', category='error')
                return render_template('login.html', form=form)

        employee_user = Employee.query.filter_by(email=email).first()
        if employee_user:
            if employee_user.verify_password(password=password):
                session['user_type'] = 'employee'
                login_user(employee_user, remember=True)
                current_app.logger.info(f"Session Authenticated: Staff member {email} logged in [Role: {employee_user.role}]")
                return redirect(url_for('views.home'))
            else:
                current_app.logger.warning(f"Failed Login Attempt: Incorrect password entered for staff account {email}")
                flash('Incorrect Email or Password', category='error')
                return render_template('login.html', form=form)

        current_app.logger.warning(f"Failed Login Attempt: Email {email} does not exist in the database system")
        flash('Account does not exist please Sign Up', category='error')

    return render_template('login.html', form=form)





@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def log_out():
    user_email = current_user.email
    user_type = session.get('user_type', 'unknown')
    session.pop('user_type', None)
    logout_user()
    # Log session termination
    current_app.logger.info(f"Session Terminated: User {user_email} logged out [Type: {user_type}]")
    return redirect(url_for('views.home'))


@auth.route('/profile/<int:customer_id>', methods=['GET', 'POST'])
@login_required
def profile(customer_id):
    if session.get('user_type') == 'employee':
        flash("Employees do not manage public shopping profile records here.", category='error')
        return redirect(url_for('views.home'))

    customer = db.session.get(Customer, customer_id)
    
    if request.method == 'POST':
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()
        email = request.form.get('email', '').strip()
        id_number = request.form.get('id_number', '').strip()
        
        name_pattern = r"^[A-Za-z\s]+$"
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not first_name or not re.match(name_pattern, first_name):
            flash("First name must contain letters only.", category='error')
            return render_template('profile.html', customer=customer)

        if not last_name or not re.match(name_pattern, last_name):
            flash("Last name must contain letters only.", category='error')
            return render_template('profile.html', customer=customer)

        if not email or not re.match(email_pattern, email):
            flash("Please enter a valid email address.", category='error')
            return render_template('profile.html', customer=customer)

        customer.first_name = first_name
        customer.last_name = last_name
        customer.id_number = id_number
        customer.email = email
        customer.street_address = request.form.get('street_address')
        customer.city = request.form.get('city')
        customer.postal_code = request.form.get('postal_code')
        
        db.session.commit()
        flash("Customer Profile updated successfully!", category='success')
        return redirect(url_for('auth.profile', customer_id=customer.id))

    return render_template('profile.html', customer=customer)


@auth.route('/change-password/<int:customer_id>', methods=['GET', 'POST'])
@login_required
def change_password(customer_id):
    if session.get('user_type') == 'employee':
        flash("Unauthorized action.", category='error')
        return redirect(url_for('views.home'))

    form = PasswordChangeForm()
    customer = db.session.get(Customer, customer_id)
    if not customer or current_user.id != customer.id:
        flash("Unauthorized action.", category='error')
        return redirect(url_for('views.home'))
        
    if form.validate_on_submit():
        current_password = form.current_password.data
        new_password = form.new_password.data
        confirm_new_password = form.confirm_new_password.data

        if customer.verify_password(current_password):
            if new_password == confirm_new_password:
                customer.password = confirm_new_password
                db.session.commit()
                # Log a successful password update transition event
                current_app.logger.info(f"Security Modification: Customer {customer.email} updated account password")
                flash('Password Updated Successfully', category='success')
                return redirect(url_for('auth.profile', customer_id=customer.id))
            else:
                flash('New Passwords do not match!!', category='error')
        else:
            flash('Current Password is Incorrect', category='error')

    return render_template('change_password.html', form=form)


@auth.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form.get('email')
        id_number = request.form.get('id_number')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        customer = Customer.query.filter_by(email=email, id_number=id_number).first()
        
        if not customer:
            current_app.logger.warning(f"Security Alert: Failed password reset query attempt for email '{email}' and ID combo match")
            flash('Account matching that email and ID combination could not be found.', category='error')
            return render_template('forgot_password.html')

        if customer.verify_password(password1):
            flash('Your new password cannot be the same as your current password. Please choose a different password.', category='error')
            return render_template('forgot_password.html')

        if not password1 or len(password1) < 6:
            flash('Password must be 6 characters or more.', category='error')
            return render_template('forgot_password.html')

        if password1 == password2:
            customer.password = password2
            db.session.commit()
            # Log an explicit external recovery password override change operation
            current_app.logger.info(f"Security Reset: Customer {email} modified access keys through forgot-password route registry")
            flash('Password updated successfully. You can now login.', category='success')
            return redirect(url_for('auth.login'))
        else:
            flash('New Passwords do not match!!', category='error')

    return render_template('forgot_password.html')






# API Part for insomnia to work
# -------------------------------------------------------------------

@auth.route('/api/sign-up', methods=['POST'])
def api_signup():
    data = request.get_json(silent=True) or {}
    email = data.get('email')
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    id_number = data.get('id_number')
    password1 = data.get('password1')
    password2 = data.get('password2')

    if not email or not first_name or not last_name or not id_number or not password1:
        return jsonify({"status": "fail", "message": "Missing required fields"}), 400

    if not str(id_number).isdigit() or len(str(id_number)) != 13:
        return jsonify({"status": "fail", "message": "ID number must be exactly 13 digits and numeric"}), 400

    if len(password1) < 6:
        return jsonify({"status": "fail", "message": "Password must be 6 characters or more"}), 400

    if password1 != password2:
        return jsonify({"status": "fail", "message": "Passwords do not match"}), 400

    new_customer = Customer()
    new_customer.email = email
    new_customer.first_name = first_name
    new_customer.last_name = last_name
    new_customer.id_number = id_number
    new_customer.password = password2

    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({
            "status": "success", 
            "message": "Account Created Successfully",
            "customer": {
                "id": new_customer.id,
                "email": new_customer.email,
                "first_name": new_customer.first_name,
                "last_name": new_customer.last_name,
                "id_number": new_customer.id_number
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({"status": "fail", "message": "Account Not Created!! Email or ID number already exists"}), 400


@auth.route('/api/login', methods=['POST'])
def api_login():
    data = request.get_json(silent=True) or {}
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"status": "fail", "message": "Missing email or password"}), 400

    customer = Customer.query.filter_by(email=email).first()
    if customer and customer.verify_password(password=password):
        session['user_type'] = 'customer'
        login_user(customer, remember=True)
        return jsonify({
            "status": "success", 
            "message": "Logged in successfully as Customer!",
            "customer": {
                "id": customer.id,
                "email": customer.email,
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "id_number": customer.id_number
            }
        }), 200

    employee_user = Employee.query.filter_by(email=email).first()
    if employee_user and employee_user.verify_password(password=password):
        session['user_type'] = 'employee'
        login_user(employee_user, remember=True)
        return jsonify({
            "status": "success", 
            "message": "Logged in successfully as Employee!",
            "employee": {
                "id": employee_user.id,
                "email": employee_user.email,
                "first_name": employee_user.first_name,
                "last_name": employee_user.last_name,
                "role": employee_user.role
            }
        }), 200
        
    return jsonify({"status": "fail", "message": "Incorrect Email or Password"}), 401


@auth.route('/api/logout', methods=['POST', 'GET'])
@login_required
def api_logout():
    session.pop('user_type', None)
    logout_user()
    return jsonify({"status": "success", "message": "Logged out successfully"}), 200


@auth.route('/api/profile/<int:customer_id>', methods=['GET'])
@login_required
def api_profile(customer_id):
    if session.get('user_type') == 'employee':
        return jsonify({"status": "fail", "message": "Unauthorized access. Employees do not have client shopping profile cards."}), 403

    customer = db.session.get(Customer, customer_id)
    if not customer:
        return jsonify({"status": "fail", "message": "Customer not found"}), 404
        
    if current_user.id != customer.id:
        return jsonify({"status": "fail", "message": "Unauthorized access"}), 403

    return jsonify({
        "status": "success",
        "data": {
            "id": customer.id,
            "first_name": customer.first_name,
            "last_name": customer.last_name,
            "id_number": customer.id_number,
            "email": customer.email,
            "date_joined": customer.date_joined.isoformat()
        }
    }), 200


@auth.route('/api/change-password', methods=['POST'])
@login_required
def api_change_password():
    if session.get('user_type') == 'employee':
        return jsonify({"status": "fail", "message": "Unauthorized action for employees."}), 403

    data = request.get_json(silent=True) or {}
    current_password = data.get('current_password')
    new_password = data.get('new_password')
    confirm_new_password = data.get('confirm_new_password')

    if not current_password or not new_password or not confirm_new_password:
        return jsonify({"status": "fail", "message": "Missing required fields"}), 400

    if new_password != confirm_new_password:
        return jsonify({"status": "fail", "message": "New passwords do not match"}), 400

    if not current_user.verify_password(current_password):
        return jsonify({"status": "fail", "message": "Current password is incorrect"}), 401

    current_user.password = confirm_new_password
    db.session.commit()
    return jsonify({"status": "success", "message": "Password updated successfully"}), 200


@auth.route('/api/forgot-password', methods=['POST'])
def api_forgot_password():
    data = request.get_json(silent=True) or {}
    email = data.get('email')
    id_number = data.get('id_number')
    password1 = data.get('password1')
    password2 = data.get('password2')

    if not email or not id_number or not password1 or not password2:
        return jsonify({"status": "fail", "message": "Missing required fields"}), 400

    customer = Customer.query.filter_by(email=email, id_number=str(id_number)).first()
    if not customer:
        return jsonify({"status": "fail", "message": "Account matching that email and ID combination could not be found."}), 404

    if customer.verify_password(password1):
        return jsonify({"status": "fail", "message": "Your new password cannot be the same as your current password. Please choose a different password."}), 400

    if len(password1) < 6:
        return jsonify({"status": "fail", "message": "Password must be 6 characters or more"}), 400

    if password1 != password2:
        return jsonify({"status": "fail", "message": "New passwords do not match"}), 400

    try:
        customer.password = password2
        db.session.commit()
        return jsonify({"status": "success", "message": "Password reset successfully."}), 200
    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({"status": "fail", "message": "Database exception during update processing."}), 500








