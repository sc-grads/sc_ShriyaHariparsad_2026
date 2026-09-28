import hashlib
import urllib.parse
import uuid
import os
from dotenv import load_dotenv
from flask import Blueprint, render_template, flash, redirect, request, jsonify, session, url_for, current_app
from flask_login import login_required, current_user
from .models import Product, Cart, Order, Wishlist, CustomerReturn
from . import db
from urllib.parse import unquote

base_dir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(base_dir, '../.env'))

views = Blueprint('views', __name__)

PAYFAST_MERCHANT_ID = os.getenv('PAYFAST_MERCHANT_ID')
PAYFAST_MERCHANT_KEY = os.getenv('PAYFAST_MERCHANT_KEY')
PAYFAST_PASSPHRASE = ''
PAYFAST_URL = 'https://sandbox.payfast.co.za/eng/process'


def generate_payfast_signature(data, passphrase=""):
    payload = ""
    for key in sorted(data.keys()):
        if key != 'signature' and data[key] != "":
            payload += f"{key}={urllib.parse.quote_plus(str(data[key]).strip())}&"
            
    payload = payload[:-1]
    if passphrase:
        payload += f"&passphrase={urllib.parse.quote_plus(passphrase.strip())}"
        
    return hashlib.md5(payload.encode('utf-8')).hexdigest()


@views.route('/')
def home():
    items = Product.query.filter_by(flash_sale=True)
    
    is_customer = current_user.is_authenticated and session.get('user_type') == 'customer'
    cart_items = Cart.query.filter_by(customer_link=current_user.id).all() if is_customer else []
    wish_items = Wishlist.query.filter_by(customer_link=current_user.id).all() if is_customer else []

    return render_template('home.html', items=items, cart=cart_items, wishlist=wish_items)


@views.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form.get('search', '').strip()
        session['last_search'] = search_query
    else:
        search_query = session.get('last_search', '')
        
    items = Product.query.filter(Product.product_name.like(f'%{search_query}%')).all()
    
    is_customer = current_user.is_authenticated and session.get('user_type') == 'customer'
    cart_items = Cart.query.filter_by(customer_link=current_user.id).all() if is_customer else []
    wish_items = Wishlist.query.filter_by(customer_link=current_user.id).all() if is_customer else []
    
    return render_template('search_results.html', items=items, cart=cart_items, wishlist=wish_items, query=search_query)


@views.route('/category/<path:val>')
def category_view(val):
    category_decoded = unquote(val).strip()
    page = request.args.get('page', 1, type=int)
    
    query = Product.query.filter_by(category=category_decoded)
    
    items_pagination = query.order_by(Product.date_added.desc()).paginate(page=page, per_page=4, error_out=False)
    items = items_pagination.items
    
    is_customer = current_user.is_authenticated and session.get('user_type') == 'customer'
    cart_items = Cart.query.filter_by(customer_link=current_user.id).all() if is_customer else []
    wish_items = Wishlist.query.filter_by(customer_link=current_user.id).all() if is_customer else []

    return render_template(
        'category_products.html', 
        items=items, 
        items_pagination=items_pagination, 
        category_name=category_decoded, 
        cart=cart_items, 
        wishlist=wish_items
    )

@views.route('/add-to-cart/<int:item_id>')
@login_required
def add_to_cart(item_id):
    if session.get('user_type') == 'employee':
        flash("Employees cannot perform customer shopping actions.", category='error')
        return redirect(url_for('views.home'))

    item_to_add = db.session.get(Product, item_id)
    if not item_to_add or item_to_add.in_stock <= 0:
        flash("This product is currently out of stock.", category='error')
        return redirect(request.referrer or url_for('views.home'))

    item_exists = Cart.query.filter_by(product_link=item_id, customer_link=current_user.id).first()
    
    if item_exists:
        if item_exists.quantity >= item_to_add.in_stock:
            flash(f"Cannot add more! Only {item_to_add.in_stock} units are currently available in stock.", category='error')
            return redirect(request.referrer or url_for('views.home'))

        try:
            item_exists.quantity = item_exists.quantity + 1
            
            wish_to_clear = Wishlist.query.filter_by(product_link=item_id, customer_link=current_user.id).first()
            if wish_to_clear:
                db.session.delete(wish_to_clear)
                
            db.session.commit()
            # Log increment action event state change only
            current_app.logger.info(f"Cart Modification: Customer {current_user.email} increased quantity for product '{item_to_add.product_name}' (ID: {item_to_add.id})")
            flash(f'Quantity of { item_exists.product.product_name } has been updated')
            return redirect(request.referrer or url_for('views.home'))
        except Exception as e:
            # Log structural storage runtime exception failures
            current_app.logger.error(f"Cart Exception: Failed incrementing product quantity for {current_user.email} - Error: {str(e)}")
            flash(f'Quantity of { item_exists.product.product_name } not updated')
            return redirect(request.referrer or url_for('views.home'))

    new_cart_item = Cart()
    new_cart_item.quantity = 1
    new_cart_item.product_link = item_to_add.id
    new_cart_item.customer_link = current_user.id

    try:
        db.session.add(new_cart_item)
        
        wish_to_clear = Wishlist.query.filter_by(product_link=item_id, customer_link=current_user.id).first()
        if wish_to_clear:
            db.session.delete(wish_to_clear)
            
        db.session.commit()
        # Log a brand new creation entry event addition to cart database
        current_app.logger.info(f"New Cart Insertion: Customer {current_user.email} added product '{item_to_add.product_name}' (ID: {item_to_add.id}) to cart")
        flash(f'{new_cart_item.product.product_name} added to cart')
    except Exception as e:
        db.session.rollback()
        # Log structural storage runtime exception failures
        current_app.logger.error(f"Cart Exception: Failed adding brand new product to cart registry for {current_user.email} - Error: {str(e)}")
        flash(f'{new_cart_item.product.product_name} has not been added to cart')

    return redirect(request.referrer or url_for('views.home'))


@views.route('/cart')
def show_cart():
    if session.get('user_type') == 'employee':
        flash("Employees do not manage shopping carts.", category='error')
        return redirect(url_for('views.home'))

    if not current_user.is_authenticated:
        last_logged_record = Order.query.order_by(Order.id.desc()).first()
        active_customer_id = last_logged_record.customer_link if last_logged_record else None
    else:
        active_customer_id = current_user.id

    if not active_customer_id:
        flash("Please log in to view your shopping cart.", category="error")
        return redirect(url_for('auth.login'))

    cart = Cart.query.filter_by(customer_link=active_customer_id).all()
    wish_items = Wishlist.query.filter_by(customer_link=active_customer_id).all()
    amount = 0
    for item in cart:
        amount += item.product.current_price * item.quantity

    return render_template('cart.html', cart=cart, wishlist=wish_items, amount=amount, total=amount+150)


@views.route('/pluscart')
def plus_cart():
    if session.get('user_type') == 'employee':
        return jsonify({"status": "fail", "message": "Unauthorized action"}), 403

    if not current_user.is_authenticated:
        last_logged_record = Order.query.order_by(Order.id.desc()).first()
        active_customer_id = last_logged_record.customer_link if last_logged_record else None
    else:
        active_customer_id = current_user.id

    if not active_customer_id:
        return jsonify({"status": "fail", "message": "Login required"}), 401

    if request.method == 'GET':
        cart_id = request.args.get('cart_id')
        cart_item = db.session.get(Cart, cart_id)
        if cart_item and cart_item.customer_link == active_customer_id:
            product_info = db.session.get(Product, cart_item.product_link)
            if product_info and cart_item.quantity >= product_info.in_stock:
                return jsonify({"status": "fail", "message": f"Maximum available stock ({product_info.in_stock}) reached."}), 400
                
            cart_item.quantity = cart_item.quantity + 1
            db.session.commit()
            # Log active state quantity adjustment change event tracking metric
            user_log_name = current_user.email if current_user.is_authenticated else f"Anonymous (Guest matching ID: {active_customer_id})"
            current_app.logger.info(f"Cart Modification (Asynchronous): User {user_log_name} incremented quantity for cart entry #{cart_id}")

        cart = Cart.query.filter_by(customer_link=active_customer_id).all()
        amount = 0
        for item in cart:
            amount += item.product.current_price * item.quantity

        data = {
            'quantity': cart_item.quantity if cart_item else 0,
            'amount': amount,
            'total': amount + 150
        }
        return jsonify(data)






@views.route('/minuscart')
def minus_cart():
    if session.get('user_type') == 'employee':
        return jsonify({"status": "fail", "message": "Unauthorized action"}), 403

    if not current_user.is_authenticated:
        last_logged_record = Order.query.order_by(Order.id.desc()).first()
        active_customer_id = last_logged_record.customer_link if last_logged_record else None
    else:
        active_customer_id = current_user.id

    if not active_customer_id:
        return jsonify({"status": "fail", "message": "Login required"}), 401

    if request.method == 'GET':
        cart_id = request.args.get('cart_id')
        cart_item = db.session.get(Cart, cart_id)
        if cart_item and cart_item.customer_link == active_customer_id:
            if cart_item.quantity <= 1:
                return jsonify({"status": "fail", "message": "Quantity cannot be less than 1."}), 400
                
            cart_item.quantity = cart_item.quantity - 1
            db.session.commit()
            # Log active state quantity decrease event tracking metric
            user_log_name = current_user.email if current_user.is_authenticated else f"Anonymous (Guest ID: {active_customer_id})"
            current_app.logger.info(f"Cart Modification (Asynchronous): User {user_log_name} decremented quantity for cart entry #{cart_id}")

        cart = Cart.query.filter_by(customer_link=active_customer_id).all()
        amount = 0
        for item in cart:
            amount += item.product.current_price * item.quantity

        data = {
            'quantity': cart_item.quantity if cart_item else 0,
            'amount': amount,
            'total': amount + 150
        }
        return jsonify(data)


@views.route('/removecart')
def remove_cart():
    if session.get('user_type') == 'employee':
        return jsonify({"status": "fail", "message": "Unauthorized action"}), 403

    if not current_user.is_authenticated:
        last_logged_record = Order.query.order_by(Order.id.desc()).first()
        active_customer_id = last_logged_record.customer_link if last_logged_record else None
    else:
        active_customer_id = current_user.id

    if not active_customer_id:
        return jsonify({"status": "fail", "message": "Login required"}), 401

    if request.method == 'GET':
        cart_id = request.args.get('cart_id')
        cart_item = db.session.get(Cart, cart_id)
        if cart_item and cart_item.customer_link == active_customer_id:
            product_name = cart_item.product.product_name
            db.session.delete(cart_item)
            db.session.commit()
            # Log database elimination deletion event change state
            user_log_name = current_user.email if current_user.is_authenticated else f"Anonymous (Guest ID: {active_customer_id})"
            current_app.logger.info(f"Cart Removal (Asynchronous): User {user_log_name} completely removed item '{product_name}' (Entry #{cart_id}) from cart")

        # Fetch remaining items to compute correct counters
        cart = Cart.query.filter_by(customer_link=active_customer_id).all()
        amount = 0
        for item in cart:
            amount += item.product.current_price * item.quantity

        data = {
            'quantity': cart_item.quantity if cart_item else 0,
            'amount': amount,
            'total': amount + 150,
            'cart_length': len(cart)  
        }
        return jsonify(data)



@views.route('/place-order', methods=['POST'])
@login_required
def place_order():
    if session.get('user_type') == 'employee':
        flash("Employees cannot place marketplace orders.", category='error')
        return redirect(url_for('views.home'))

    customer_cart = Cart.query.filter_by(customer_link=current_user.id).all()
    if not customer_cart:
        flash("Your cart is empty.", category="error")
        return redirect(url_for('views.show_cart'))

    address = request.form.get('address', '').strip()
    city = request.form.get('city', '').strip()
    postal_code = request.form.get('postal_code', '').strip()

    if not address or not city or not postal_code:
        flash("Please fill in all delivery details (Address, City, and Postal Code).", category="error")
        return redirect(url_for('views.show_cart'))

    for item in customer_cart:
        if item.quantity > item.product.in_stock:
            # Log concrete processing exception failure before flashing warnings
            current_app.logger.warning(f"Order Attempt Blocked: Out of stock scenario during validation checkpoint layout for customer {current_user.email} looking for product '{item.product.product_name}'")
            flash(f"Order failed! '{item.product.product_name}' only has {item.product.in_stock} items left in stock, but you have {item.quantity} in your cart.", category="error")
            return redirect(url_for('views.show_cart'))

    amount = 0
    for item in customer_cart:
        amount += item.product.current_price * item.quantity
    total_amount = amount + 150

    custom_m_id = str(uuid.uuid4().hex[:8].upper())

    session['last_address'] = address
    session['last_city'] = city
    session['last_postal_code'] = postal_code

    payfast_data = {
        'merchant_id': PAYFAST_MERCHANT_ID,
        'merchant_key': PAYFAST_MERCHANT_KEY,
        'return_url': url_for('views.payment_success', _external=True),
        'cancel_url': url_for('views.show_cart', _external=True),
        'notify_url': url_for('views.payfast_notify', _external=True),
        'name_first': current_user.first_name,
        'name_last': current_user.last_name,
        'email_address': current_user.email,
        'm_payment_id': custom_m_id,
        'amount': f"{total_amount:.2f}",
        'item_name': f"Order {custom_m_id}",
        'custom_str1': address,
        'custom_str2': city,
        'custom_str3': postal_code
    }

    payfast_data['signature'] = generate_payfast_signature(payfast_data, PAYFAST_PASSPHRASE)
    
    # Log a checkout redirection signature setup generation initialization event mapping metric
    current_app.logger.info(f"Checkout Initialized: Customer {current_user.email} generated PayFast payload for transaction reference '{custom_m_id}' totaling R{payfast_data['amount']}")

    return render_template('payfast_checkout.html', payfast_data=payfast_data, payfast_url=PAYFAST_URL)



@views.route('/payment-success')
@login_required
def payment_success():
    customer_cart = Cart.query.filter_by(customer_link=current_user.id).all()
    if not customer_cart:
        return redirect(url_for('views.orders'))

    try:
        simulated_tx_id = f"PF-{uuid.uuid4().hex[:8].upper()}"
        items_logged_summary = []
        
        for item in customer_cart:
            new_order = Order()
            new_order.quantity = item.quantity
            new_order.price = item.product.current_price
            new_order.product_link = item.product_link
            new_order.customer_link = current_user.id
            new_order.status = "Pending Delivery"
            new_order.payment_id = simulated_tx_id
            new_order.address = session.get('last_address', '')
            new_order.city = session.get('last_city', '')
            new_order.postal_code = session.get('last_postal_code', '')
            
            db.session.add(new_order)
            item.product.in_stock -= item.quantity
            
            items_logged_summary.append(f"'{item.product.product_name}' (Qty: {item.quantity})")
            db.session.delete(item)
            
        db.session.commit()
        # Log successful order completion and fulfillment state transformation
        current_app.logger.info(f"Order Completed: Customer {current_user.email} successfully completed transaction {simulated_tx_id}. Products: {', '.join(items_logged_summary)}")
        flash("Payment authorised! Your purchase has been logged successfully.", category="success")
    except Exception as e:
        db.session.rollback()
        # Log database recovery exception tracks
        current_app.logger.error(f"Fulfillment Exception: Database processing failed during payment validation check for {current_user.email} - Error: {str(e)}")
        flash("An error occurred while saving your purchase records.", category="error")

    return redirect(url_for('views.orders'))


@views.route('/payfast-notify', methods=['POST'])
def payfast_notify():
    return '', 200


@views.route('/orders')
def orders():
    if session.get('user_type') == 'employee':
        flash("Employees do not access customer personal history boards.", category='error')
        return redirect(url_for('views.home'))

    if not current_user.is_authenticated:
        last_logged_record = Order.query.order_by(Order.id.desc()).first()
        active_customer_id = last_logged_record.customer_link if last_logged_record else None
    else:
        active_customer_id = current_user.id

    if not active_customer_id:
        flash("Please log in to view your purchases.", category="error")
        return redirect(url_for('auth.login'))

    page = request.args.get('page', 1, type=int)
    
    orders_pagination = Order.query.filter_by(customer_link=active_customer_id).order_by(Order.date_ordered.desc()).paginate(page=page, per_page=3, error_out=False)
    customer_orders = orders_pagination.items

    return render_template(
        'orders.html', 
        orders=customer_orders, 
        orders_pagination=orders_pagination
    )


@views.route('/about-us')
def about_us():
    return render_template('about_us.html')


@views.route('/contact-us')
def contact_us():
    if session.get('user_type') == 'employee':
        flash("Employees do not use customer communication portals.", category='error')
        return redirect(url_for('views.home'))
    return render_template('contact_us.html')


@views.route('/wishlist')
@login_required
def wishlist():
    if session.get('user_type') == 'employee':
        flash("Employees do not manage shopper interest wishlists.", category='error')
        return redirect(url_for('views.home'))
        
    is_customer = current_user.is_authenticated and session.get('user_type') == 'customer'
    cart_items = Cart.query.filter_by(customer_link=current_user.id).all() if is_customer else []
    wishlist_items = Wishlist.query.filter_by(customer_link=current_user.id).all() if is_customer else []
    
    return render_template('wishlist.html', wishlist=wishlist_items, cart=cart_items)


@views.route('/add-to-wishlist/<int:item_id>')
@login_required
def add_to_wishlist(item_id):
    if session.get('user_type') == 'employee':
        flash("Employees cannot perform wishlist actions.", category='error')
        return redirect(url_for('views.home'))

    item_exists = Wishlist.query.filter_by(product_link=item_id, customer_link=current_user.id).first()
    if item_exists:
        flash("This product is already present in your wishlist.", category='info')
        return redirect(request.referrer or url_for('views.home'))

    new_wish_item = Wishlist()
    new_wish_item.product_link = item_id
    new_wish_item.customer_link = current_user.id

    try:
        db.session.add(new_wish_item)
        db.session.commit()
        # Log a brand new creation storage action on customer wishlists
        product_ref = db.session.get(Product, item_id)
        product_name = product_ref.product_name if product_ref else f"ID: {item_id}"
        current_app.logger.info(f"New Wishlist Insertion: Customer {current_user.email} saved product '{product_name}' to wishlist")
        flash("Product added to wishlist successfully.", category='success')
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Wishlist Exception: Error processing add action for {current_user.email} - Error: {str(e)}")
        flash("Could not add product to wishlist.", category='error')

    return redirect(request.referrer or url_for('views.home'))


@views.route('/remove-from-wishlist/<int:wish_id>')
@login_required
def remove_from_wishlist(wish_id):
    wish_item = db.session.get(Wishlist, wish_id)
    if wish_item and wish_item.customer_link == current_user.id:
        try:
            product_name = wish_item.product.product_name if wish_item.product else f"ID: {wish_item.product_link}"
            db.session.delete(wish_item)
            db.session.commit()
            # Log structural database elimination change step
            current_app.logger.info(f"Wishlist Removal: Customer {current_user.email} deleted product '{product_name}' from wishlist")
            flash("Product removed from wishlist.")
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Wishlist Exception: Error removing row reference {wish_id} for {current_user.email} - Error: {str(e)}")
            flash("Could not remove item from wishlist.")
    return redirect(url_for('views.wishlist'))


@views.route('/submit-return-request', methods=['POST'])
@login_required
def submit_return_request():
    if session.get('user_type') == 'employee':
        flash("Employees cannot submit customer return tickets.", category="error")
        return redirect(url_for('views.home'))
        
    order_id = request.form.get('order_id')
    reason_text = request.form.get('reason', '').strip()
    
    order_record = db.session.get(Order, order_id)
    if order_record and order_record.customer_link == current_user.id:
        new_return = CustomerReturn()
        new_return.order_link = order_id
        new_return.reason = reason_text
        new_return.status = 'Pending Review'
        
        try:
            db.session.add(new_return)
            db.session.commit()
            # Log initialization of a brand new customer package return ticket request
            current_app.logger.info(f"New Return Ticket: Customer {current_user.email} submitted return request for Order #{order_id}. Reason: '{reason_text}'")
            flash("Your return request has been successfully submitted to our Durban dispatch hub for review.", category="success")
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Return Exception: Failed logging new entry for Order #{order_id} - Error: {str(e)}")
            flash("An error occurred while logging your return.", category="error")
            
    return redirect(url_for('views.orders'))




@views.route('/print-receipt/<int:order_id>')
@login_required
def print_receipt(order_id):
    order = db.session.get(Order, order_id)
    if not order or order.customer_link != current_user.id:
        flash("Unauthorised action or receipt not found.", category="error")
        return redirect(url_for('views.orders'))
        
    current_app.logger.info(f"Receipt Print Triggered: Customer {current_user.email} opened print template view for Order #{order.id}")
    return render_template('receipt.html', order=order)















