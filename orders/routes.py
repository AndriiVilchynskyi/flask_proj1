from orders import app
from flask import render_template
from orders.models import Order



@app.route("/")
@app.route("/home")
def home_page():
    return render_template("home.html")


@app.route("/orders")
def order_page():
    orders = Order.query.all()
    return render_template("orders.html", orders=orders)
