#import connecttomysql
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
#import other models
import pprint


db="cookies_schema"

class Order:
    def __init__(self, data):
        self.id = data['id']
        self.customer_name = data['customer_name']
        self.cookie_type = data['cookie_type']
        self.num_of_boxes = data['num_of_boxes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def show_orders(cls):
        query = """SELECT * from orders
        """
        results = connectToMySQL(db).query_db(query)
        orders = []
        for row in results:
            orders.append(cls(row))
        return orders

    @classmethod
    def save_order(cls, data):
        query = """INSERT INTO orders(customer_name, cookie_type, num_of_boxes)
        VALUES(%(customer_name)s, %(cookie_type)s, %(num_of_boxes)s);
        """
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validation(orders):
        is_valid = True
        if len(orders['customer_name']) < 3:
            flash("Name must be longer than 3 characeters")
            is_valid = False
        if orders['cookie_type'].lower() not in ["thin mint", "thin mints", "samoas", "tagalongs", "do-si-dos", "dosidos", "trefoils", "lemonades", "toffee tastic",
        "toffee-tastic"]:
            flash("Please insert valid girl scout cookie.")
            is_valid = False
        return is_valid

    @classmethod
    def get_orders_by_id(cls, id):
        query = """SELECT * FROM orders
                WHERE id = %(id)s;
        """
        data = {"id": id}
        results = connectToMySQL(db).query_db(query, data)
        pprint.pprint(results)
        if results:
            return cls(results[0])
        else:
            return None

    @classmethod
    def update_order(cls, data): 
        query = """UPDATE orders
                SET customer_name=%(customer_name)s,cookie_type=%(cookie_type)s,num_of_boxes=%(num_of_boxes)s
                WHERE id = %(id)s;
        """
        results = connectToMySQL(db).query_db(query, data)
        return results