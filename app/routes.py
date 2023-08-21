from flask import render_template, redirect, url_for
from app import app, db
from app.models import Order

@app.route('/new_orders')
def new_orders():
    new_orders = Order.get_new_orders()
    return render_template('new_orders.html', new_orders=new_orders)

@app.route('/process_order/<int:order_id>')
def process_order(order_id):
    order = Order.query.get_or_404(order_id)
    if not order.processed:
        if order.generate_shipping_label():
            return redirect(url_for('new_orders'))
        else:
            return "Failed to generate shipping label."
    return "Order already processed."
