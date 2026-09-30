from flask import Blueprint, render_template, flash, send_from_directory, redirect, jsonify, request, session, url_for, current_app
from flask_login import login_required, current_user
from .forms import ShopItemsForm
from werkzeug.utils import secure_filename
from .models import Product, Order, Employee, CustomerReturn
from . import db
import os
from datetime import datetime

admin = Blueprint('admin', __name__)

@admin.route('/media/<path:filename>')
def get_image(filename):
    return send_from_directory('../media', filename)


@admin.route('/add-shop-items', methods=['GET', 'POST'])
@login_required
def add_shop_items():
    if session.get('user_type') == 'employee':
        form = ShopItemsForm()

        if form.validate_on_submit():
            product_name = form.product_name.data
            category = form.category.data
            current_price = form.current_price.data
            previous_price = form.previous_price.data
            in_stock = form.in_stock.data
            flash_sale = form.flash_sale.data

            file = form.product_picture.data
            if file and file.filename != '':
                file_name = secure_filename(file.filename)
                file_path = f'./media/{file_name}'
                file.save(file_path)
            else:
                file_path = './static/images/no_image.png'

            new_shop_item = Product()
            new_shop_item.product_name = product_name
            new_shop_item.category = category
            new_shop_item.current_price = current_price
            new_shop_item.previous_price = previous_price
            new_shop_item.in_stock = in_stock
            new_shop_item.flash_sale = flash_sale
            new_shop_item.product_picture = file_path

            try:
                db.session.add(new_shop_item)
                db.session.commit()
                # Log creation of a brand-new entity mapping record
                current_app.logger.info(f"Inventory Management: Employee {current_user.email} successfully added a new product: '{product_name}'")
                flash(f'{product_name} added successfully', category='success')
                print('Product Added')
                
                return redirect(url_for('admin.add_shop_items'))
            except Exception as e:
                db.session.rollback()
                # Log critical transaction rollbacks
                current_app.logger.error(f"Inventory Error: Exception occurred while Employee {current_user.email} tried adding product '{product_name}' - Error: {str(e)}")
                print(e)
                flash('Product Not Added!!', category='error')

        return render_template('add-shop-items.html', form=form)

    return render_template('404.html') 


@admin.route('/shop-items', methods=['GET', 'POST'])
@login_required
def shop_items():
    if session.get('user_type') == 'employee':
        page = request.args.get('page', 1, type=int)
        selected_category = request.args.get('category', '')
        start_date_str = request.args.get('start_date', '')
        end_date_str = request.args.get('end_date', '')

        query = Product.query

        if selected_category:
            query = query.filter_by(category=selected_category)

        if start_date_str:
            try:
                start_date = datetime.strptime(start_date_str, '%Y-%m-%d').replace(hour=0, minute=0, second=0)
                query = query.filter(Product.date_added >= start_date)
            except ValueError:
                pass

        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, '%Y-%m-%d').replace(hour=23, minute=59, second=59)
                query = query.filter(Product.date_added <= end_date)
            except ValueError:
                pass

        items_pagination = query.order_by(Product.date_added.desc()).paginate(page=page, per_page=5, error_out=False)
        items = items_pagination.items

        return render_template(
            'shop_items.html', 
            items=items, 
            items_pagination=items_pagination, 
            selected_category=selected_category, 
            start_date=start_date_str, 
            end_date=end_date_str
        )
        
    return render_template('404.html')

@admin.route('/update-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def update_item(item_id):
    if session.get('user_type') == 'employee':
        form = ShopItemsForm()
        item_to_update = db.session.get(Product, item_id)

        if not item_to_update:
            return render_template('404.html')

        if request.method == 'GET':
            form.product_name.data = item_to_update.product_name
            form.category.data = item_to_update.category
            form.previous_price.data = item_to_update.previous_price
            form.current_price.data = item_to_update.current_price
            form.in_stock.data = item_to_update.in_stock
            form.flash_sale.data = item_to_update.flash_sale

        if form.validate_on_submit():
            product_name = form.product_name.data
            category = form.category.data
            current_price = form.current_price.data
            previous_price = form.previous_price.data
            in_stock = form.in_stock.data
            flash_sale = form.flash_sale.data

            file = form.product_picture.data

            if file:
                file_name = secure_filename(file.filename)
                file_path = f'./media/{file_name}'

                if item_to_update.product_picture and os.path.exists(item_to_update.product_picture):
                    if item_to_update.product_picture != file_path:
                        try:
                            os.remove(item_to_update.product_picture)
                        except Exception as file_err:
                            print("Old image removal failed:", file_err)
                file.save(file_path)
            else:
                file_path = item_to_update.product_picture

            try:
                # Track field updates to only log when actual property fields change state values
                changes = []
                if item_to_update.product_name != product_name: changes.append(f"Name from '{item_to_update.product_name}' to '{product_name}'")
                if item_to_update.current_price != current_price: changes.append(f"Price from R{item_to_update.current_price} to R{current_price}")
                if item_to_update.in_stock != in_stock: changes.append(f"Stock Level from {item_to_update.in_stock} to {in_stock}")
                if item_to_update.flash_sale != flash_sale: changes.append(f"Flash Sale status from {item_to_update.flash_sale} to {flash_sale}")

                Product.query.filter_by(id=item_id).update(dict(
                    product_name=product_name,
                    category=category,
                    current_price=current_price,
                    previous_price=previous_price,
                    in_stock=in_stock,
                    flash_sale=flash_sale,
                    product_picture=file_path
                ))
                db.session.commit()
                
                # Write to trace file log strictly if property fields changed state values
                if changes:
                    current_app.logger.info(f"Inventory Modification: Employee {current_user.email} updated product ID #{item_id}. Changes: {', '.join(changes)}")
                
                flash(f'{product_name} updated successfully')
                print('Product updated')
                return redirect(url_for('admin.shop_items'))
            except Exception as e:
                db.session.rollback()
                current_app.logger.error(f"Inventory Error: Exception raised while Employee {current_user.email} was modifying product ID #{item_id} - Error: {str(e)}")
                print('Product not updated', e)
                flash('Item not updated!!!')

        return render_template('update_item.html', form=form, item=item_to_update)
        
    return render_template('404.html')



@admin.route('/update-order-status/<int:order_id>', methods=['POST'])
@login_required
def update_order_status(order_id):
    if session.get('user_type') == 'employee':
        order = db.session.get(Order, order_id)
        if order:
            new_status = request.form.get('status')
            
            if order.status != new_status:
                old_status = order.status
                order.status = new_status
                db.session.commit()
                current_app.logger.info(f"Fulfillment Transition: Employee {current_user.email} changed Order #{order_id} status from '{old_status}' to '{new_status}'")
                flash('Order Status Updated Successfully', category='success')
            else:
                flash('Order status is already set to this option.', category='info')
                
        return redirect(url_for('admin.view_orders'))
    return render_template('404.html')



@admin.route('/delete-item/<int:item_id>', methods=['GET', 'POST'])
@login_required
def delete_item(item_id):
    if session.get('user_type') == 'employee':
        try:
            item_to_delete = db.session.get(Product, item_id)
            if item_to_delete:
                deleted_name = item_to_delete.product_name
                if item_to_delete.product_picture and os.path.exists(item_to_delete.product_picture):
                    try:
                        os.remove(item_to_delete.product_picture)
                    except Exception as file_err:
                        print("Image asset file deletion failed:", file_err)
                
                db.session.delete(item_to_delete)
                db.session.commit()
                # Log structural entity elimination events explicitly
                current_app.logger.info(f"Inventory Purge: Employee {current_user.email} completely deleted product mapping reference ID #{item_id} ('{deleted_name}')")
                flash('One item deleted')
            else:
                flash('Item not found!!')
            return redirect(url_for('admin.shop_items'))
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Inventory Error: Exception caught while Employee {current_user.email} attempted to drop product ID #{item_id} - Error: {str(e)}")
            print('Item not deleted', e)
            flash('Item not deleted!')
        return redirect(url_for('admin.shop_items'))

    return render_template('404.html')


from flask import request, session, render_template

@admin.route('/view-orders')
@login_required
def view_orders():
    if session.get('user_type') == 'employee':
        page = request.args.get('page', 1, type=int)
        selected_status = request.args.get('status_filter', '')

        query = Order.query

        if selected_status:
            query = query.filter_by(status=selected_status)

        orders_pagination = query.order_by(Order.date_ordered.desc()).paginate(page=page, per_page=5, error_out=False)
        all_orders = orders_pagination.items

        return render_template(
            'view_orders.html', 
            orders=all_orders, 
            orders_pagination=orders_pagination, 
            selected_status=selected_status
        )
        
    return render_template('404.html')




@admin.route('/manage-returns')
@login_required
def manage_returns():
    if session.get('user_type') != 'employee':
        return render_template('404.html')
        
    page = request.args.get('page', 1, type=int)
    selected_return_status = request.args.get('return_status_filter', '')

    query = CustomerReturn.query

    if selected_return_status:
        query = query.filter_by(status=selected_return_status)

    returns_pagination = query.order_by(CustomerReturn.date_logged.desc()).paginate(page=page, per_page=5, error_out=False)
    active_returns = returns_pagination.items

    return render_template(
        'manage_returns.html', 
        returns=active_returns, 
        returns_pagination=returns_pagination, 
        selected_return_status=selected_return_status
    )



@admin.route('/process-return-action/<int:return_id>', methods=['POST'])
@login_required
def process_return_action(return_id):
    if session.get('user_type') != 'employee':
        return jsonify({"status": "fail", "message": "Unauthorized"}), 403
        
    action_type = request.form.get('action_type')
    return_record = db.session.get(CustomerReturn, return_id)
    
    if return_record:
        old_status = return_record.status
        new_status = 'Refund Processed' if action_type == 'Approve' else 'Rejected'
        
        # Execute processing logic and log entry strictly if a new action transition state occurs
        if old_status != new_status:
            if action_type == 'Approve':
                return_record.status = 'Refund Processed'
                return_record.order.status = 'Returned & Refunded'
                return_record.order.product.in_stock += return_record.order.quantity
                flash(f"Return approved successfully. Stock balance updated.", category="success")
            elif action_type == 'Reject':
                return_record.status = 'Rejected'
                flash("Return ticket declined safely.", category="info")
                
            db.session.commit()
            current_app.logger.info(f"Return Management: Employee {current_user.email} marked Return Ticket #{return_id} (Order #{return_record.order_link}) as '{new_status}'")
            
    return redirect(url_for('admin.manage_returns'))











# API Part for insomnia to work
# -------------------------------------------------------------------

@admin.route('/api/add-shop-items', methods=['POST'])
@login_required
def api_add_shop_items():
    if session.get('user_type') != 'employee':
        return jsonify({"status": "fail", "message": "Unauthorized. Employee access required."}), 403

    product_name = request.form.get('product_name')
    category = request.form.get('category')
    current_price = request.form.get('current_price')
    previous_price = request.form.get('previous_price')
    in_stock = request.form.get('in_stock')
    flash_sale = request.form.get('flash_sale') == 'True'

    if not product_name or not category or not current_price or not in_stock:
        return jsonify({"status": "fail", "message": "Missing required fields"}), 400

    file = request.files.get('product_picture')
    if file and file.filename != '':
        file_name = secure_filename(file.filename)
        file_path = f'./media/{file_name}'
        file.save(file_path)
    else:
        file_path = './static/images/no_image.png'

    new_shop_item = Product()
    new_shop_item.product_name = product_name
    new_shop_item.category = category
    new_shop_item.current_price = float(current_price)
    new_shop_item.previous_price = float(previous_price) if previous_price else None
    new_shop_item.in_stock = int(in_stock)
    new_shop_item.flash_sale = flash_sale
    new_shop_item.product_picture = file_path

    try:
        db.session.add(new_shop_item)
        db.session.commit()
        # Log successful API insertion
        current_app.logger.info(f"API Inventory Management: Employee {current_user.email} successfully added product '{product_name}' via API endpoint link target")
        return jsonify({
            "status": "success", 
            "message": f"{product_name} added successfully",
            "product_id": new_shop_item.id 
        }), 201
    except Exception as e:
        db.session.rollback()
        # Log runtime processing error exceptions
        current_app.logger.error(f"API Inventory Error: Exception caught while Employee {current_user.email} was trying to create product '{product_name}' over API context parameters - Error: {str(e)}")
        print(e)
        return jsonify({"status": "fail", "message": "Product could not be added to database"}), 500


@admin.route('/api/update-item/<int:item_id>', methods=['POST'])
@login_required
def api_update_item(item_id):
    if session.get('user_type') != 'employee':
        return jsonify({"status": "fail", "message": "Unauthorized. Employee access required."}), 403

    item_to_update = db.session.get(Product, item_id)
    if not item_to_update:
        return jsonify({"status": "fail", "message": "Item not found"}), 404

    product_name = request.form.get('product_name') or item_to_update.product_name
    category = request.form.get('category') or item_to_update.category
    current_price = request.form.get('current_price') or item_to_update.current_price
    previous_price = request.form.get('previous_price')
    in_stock = request.form.get('in_stock') or item_to_update.in_stock
    flash_sale_raw = request.form.get('flash_sale')
    
    flash_sale = flash_sale_raw == 'True' if flash_sale_raw is not None else item_to_update.flash_sale

    file = request.files.get('product_picture')
    if file and file.filename != '':
        file_name = secure_filename(file.filename)
        file_path = f'./media/{file_name}'
        
        if item_to_update.product_picture and os.path.exists(item_to_update.product_picture):
            if item_to_update.product_picture != file_path and item_to_update.product_picture != './static/images/no_image.png':
                try:
                    os.remove(item_to_update.product_picture)
                except Exception as file_err:
                    print("Old image removal failed via API:", file_err)
                    
        file.save(file_path)
    else:
        file_path = item_to_update.product_picture

    if previous_price is not None:
        final_previous_price = float(previous_price) if previous_price.strip() != '' else None
    else:
        final_previous_price = item_to_update.previous_price

    try:
        # Construct exact delta track arrays to enforce logging only when state fields change values
        changes = []
        if item_to_update.product_name != product_name: changes.append(f"Name from '{item_to_update.product_name}' to '{product_name}'")
        if float(item_to_update.current_price) != float(current_price): changes.append(f"Price from R{item_to_update.current_price} to R{current_price}")
        if int(item_to_update.in_stock) != int(in_stock): changes.append(f"Stock from {item_to_update.in_stock} to {in_stock}")
        if item_to_update.flash_sale != flash_sale: changes.append(f"Flash Sale from {item_to_update.flash_sale} to {flash_sale}")

        Product.query.filter_by(id=item_id).update(dict(
            product_name=product_name,
            category=category,
            current_price=float(current_price),
            previous_price=final_previous_price,
            in_stock=int(in_stock),
            flash_sale=flash_sale,
            product_picture=file_path
        ))
        db.session.commit()
        
        # Write statement to logger only on true value mutations
        if changes:
            current_app.logger.info(f"API Inventory Modification: Employee {current_user.email} updated product ID #{item_id} over endpoints. Changes: {', '.join(changes)}")
            
        return jsonify({"status": "success", "message": f"{product_name} updated successfully"}), 200
    except Exception as e:
        db.session.rollback()
        # Log runtime processing error exceptions
        current_app.logger.error(f"API Inventory Error: Exception raised while Employee {current_user.email} tried mutating product ID #{item_id} inside API tree endpoints - Error: {str(e)}")
        print(e)
        return jsonify({"status": "fail", "message": "Item could not be updated"}), 500


@admin.route('/api/delete-item/<int:item_id>', methods=['DELETE'])
@login_required
def api_delete_item(item_id):
    if session.get('user_type') != 'employee':
        return jsonify({"status": "fail", "message": "Unauthorised. Employee access required."}), 403

    try:
        item_to_delete = db.session.get(Product, item_id)
        if not item_to_delete:
            return jsonify({"status": "fail", "message": "Item not found"}), 404

        deleted_name = item_to_delete.product_name
        if item_to_delete.product_picture and os.path.exists(item_to_delete.product_picture):
            if item_to_delete.product_picture != './static/images/no_image.png':
                try:
                    os.remove(item_to_delete.product_picture)
                except Exception as file_err:
                    print("Image file deletion failed via API:", file_err)

        db.session.delete(item_to_delete)
        db.session.commit()
        # Log structural resource deletion events
        current_app.logger.info(f"API Inventory Purge: Employee {current_user.email} completely deleted product registry map reference ID #{item_id} ('{deleted_name}') over API endpoints")
        return jsonify({"status": "success", "message": "Item deleted successfully"}), 200
    except Exception as e:
        db.session.rollback()
        # Log runtime processing error exceptions
        current_app.logger.error(f"API Inventory Error: Exception caught while Employee {current_user.email} called drop endpoint on product ID #{item_id} inside API tree context - Error: {str(e)}")
        print(e)
        return jsonify({"status": "fail", "message": "Item could not be deleted"}), 500



@admin.route('/api/update-order-status', methods=['POST'])
@login_required
def api_update_order_status():
    if session.get('user_type') != 'employee':
        return jsonify({"status": "fail", "message": "Unauthorised. Employee access required."}), 403

    order_id = request.json.get('order_id')
    new_status = request.json.get('status')
    
    order_to_modify = db.session.get(Order, order_id)
    if not order_to_modify:
        return jsonify({"status": "fail", "message": "Order record not found"}), 404
        
    try:
        # Check old status state against incoming selection parameters to log state updates only
        if order_to_modify.status != new_status:
            old_status = order_to_modify.status
            order_to_modify.status = new_status
            db.session.commit()
            current_app.logger.info(f"API Fulfillment Transition: Employee {current_user.email} updated Order #{order_id} status from '{old_status}' to '{new_status}' via API endpoint")
            return jsonify({"status": "success", "message": f"Order status updated to {new_status} successfully"}), 200
            
        return jsonify({"status": "success", "message": "No state change detected"}), 200
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"API Order Status Error: Exception raised while Employee {current_user.email} updated Order #{order_id} - Error: {str(e)}")
        print(e)
        return jsonify({"status": "fail", "message": "Could not execute database save operation"}), 500


@admin.route('/api/manage-returns', methods=['GET'])
@login_required
def api_manage_returns():
    if session.get('user_type') != 'employee':
        return jsonify({"status": "fail", "message": "Unauthorised. Employee access required."}), 403
        
    active_returns = CustomerReturn.query.order_by(CustomerReturn.date_logged.desc()).all()
    returns_list = []
    
    for item in active_returns:
        returns_list.append({
            "return_id": item.id,
            "order_id": item.order.id,
            "product_name": item.order.product.product_name,
            "customer_name": f"{item.order.customer.first_name} {item.order.customer.last_name}",
            "customer_email": item.order.customer.email,
            "reason": item.reason,
            "refund_value": item.order.price * item.order.quantity,
            "status": item.status,
            "date_logged": item.date_logged.strftime('%Y-%m-%d %H:%M:%S') if item.date_logged else None
        })
        
    return jsonify({"status": "success", "returns": returns_list}), 200


@admin.route('/api/process-return-action', methods=['POST'])
@login_required
def api_process_return_action():
    if session.get('user_type') != 'employee':
        return jsonify({"status": "fail", "message": "Unauthorised. Employee access required."}), 403
        
    return_id = request.json.get('return_id')
    action_type = request.json.get('action_type')  # Expects 'Approve' or 'Reject'
    
    return_record = db.session.get(CustomerReturn, return_id)
    if not return_record:
        return jsonify({"status": "fail", "message": "Return record not found"}), 404
        
    try:
        old_status = return_record.status
        new_status = 'Refund Processed' if action_type == 'Approve' else 'Rejected'
        
        # Guard logging tracking logic block to trigger exclusively on field changes
        if old_status != new_status:
            if action_type == 'Approve':
                return_record.status = 'Refund Processed'
                return_record.order.status = 'Returned & Refunded'
                return_record.order.product.in_stock += return_record.order.quantity
                db.session.commit()
                current_app.logger.info(f"API Return Management: Employee {current_user.email} marked Return Ticket #{return_id} (Order #{return_record.order_link}) as 'Refund Processed' over API endpoints")
                return jsonify({"status": "success", "message": "Return approved via API. Inventory updated."}), 200
            elif action_type == 'Reject':
                return_record.status = 'Rejected'
                db.session.commit()
                current_app.logger.info(f"API Return Management: Employee {current_user.email} marked Return Ticket #{return_id} (Order #{return_record.order_link}) as 'Rejected' over API endpoints")
                return jsonify({"status": "success", "message": "Return rejected via API."}), 200
            else:
                return jsonify({"status": "fail", "message": "Invalid action type specified"}), 400
                
        return jsonify({"status": "success", "message": "No action state change required"}), 200
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"API Return Error: Exception caught while Employee {current_user.email} updated Return Ticket #{return_id} over API endpoints - Error: {str(e)}")
        print(e)
        return jsonify({"status": "fail", "message": "Could not execute database action"}), 500









    







        