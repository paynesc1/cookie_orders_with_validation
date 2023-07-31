from flask_app.config.mysqlconnection import connectToMySQL
#import app
from flask_app import app
#import renders
from flask import render_template, request, redirect, session, flash
#import models
from flask_app.models.order_model import Order




#render show all orders page route
@app.route("/")
def show_orders():
    #get-all route in model
    orders = Order.show_orders()
    return render_template("cookies.html", orders=orders)

#render log new order page route
@app.route("/cookies/new")
def cookies_new():
    return render_template("log/order.html")

#render change order page route
@app.route("/cookies/edit/<int:id>")
def cookies_edit(id):
    #get orders by id method
    order = Order.get_orders_by_id(id)
    return render_template("cookies_edit.html", order=order)



#route to save order from html form
@app.route("/cookies/save", methods=['POST'])
def save_order():
    #save method
    if not Order.validation(request.form):
        return redirect("/cookies/new")
    Order.save_order(request.form)
    return redirect("/")

@app.route("/cookies/edit/<int:id>", methods=['POST'])
def update_order(id):
    #update method
    if not Order.validation(request.form):
        return redirect(f"/cookies/edit/{id}")
    Order.update_order({**request.form, 'id':id})
    return redirect("/")