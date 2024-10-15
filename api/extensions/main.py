from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from database.menu import menu
import time
import random
import datetime
from pizza_assistant import PizzaAssistant

app = Flask(__name__)
CORS(app)

# Order Database
orders = []


@app.route('/api/menu', methods=['POST'])
def get_menu():
    filter = request.json

    # Check if filter has a 'query' key and not empty
    filteredMenu = menu
    if 'query' in filter and filter['query']:
        pizzaAssistant = PizzaAssistant()
        filteredMenu = pizzaAssistant.get_automated_menu(filter['query'])

    payload = {
        "status": "success",
        "data": filteredMenu,
        "filter": filter
    }
    return jsonify(payload)


@ app.route('/api/order/<int:id>', methods=['GET'])
def get_order(id):
    order = next((order for order in orders if order['id'] == id), None)
    if order:
        payload = {
            "status": "success",
            "data": order
        }
        return jsonify(payload)
    else:
        return jsonify({"error": "Order not found"}), 404


@ app.route('/api/order', methods=['POST'])
def create_order():
    new_order = request.json
    new_order['id'] = len(orders) + 1
    orders.append(new_order)

    # Set the order status to 'preparing'
    new_order['status'] = 'preparing'
    # Set the order createdAt and estimatedDelivery
    new_order['createdAt'] = datetime.datetime.fromtimestamp(
        time.time()).strftime("%Y-%m-%dT%H:%M:%S")
    new_order['estimatedDelivery'] = datetime.datetime.fromtimestamp(
        time.time() + random.randint(1800, 3600)).strftime("%Y-%m-%dT%H:%M:%S")
    # Calculate the order price: sum of each menu item price * quantity
    new_order['orderPrice'] = sum(
        [menu_item['unitPrice'] * menu_item['quantity'] for menu_item in new_order['cart']])
    # Calculate the priority price: 20% of the order price
    new_order['priorityPrice'] = new_order['orderPrice'] * 0.2

    payload = {
        "status": "success",
        "data": new_order
    }
    return jsonify(payload), 201


@ app.route('/api/order', methods=['PUT'])
def update_order():
    updated_order = request.json
    order = next(
        (order for order in orders if order['id'] == updated_order['id']), None)
    if order:
        order.update(updated_order)
        payload = {
            "status": "success",
            "data": order
        }
        return jsonify(payload)
    else:
        return jsonify({"error": "Order not found"}), 404


@ app.route('/api/image/<string:id>', methods=['GET'])
def get_image(id):
    return send_from_directory('database/images', id)


if __name__ == '__main__':
    app.run(debug=True, port=8889)
