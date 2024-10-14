from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from database.menu import menu

app = Flask(__name__)
CORS(app)

# Order Database
orders = []


@app.route('/api/menu', methods=['GET'])
def get_menu():
    payload = {
        "status": "success",
        "data": menu
    }
    return jsonify(payload)


@app.route('/api/order/<int:id>', methods=['GET'])
def get_order(id):
    order = next((order for order in orders if order['id'] == id), None)
    if order:
        return jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404


@app.route('/api/order', methods=['POST'])
def create_order():
    new_order = request.json
    new_order['id'] = len(orders) + 1
    orders.append(new_order)
    return jsonify(new_order), 201


@app.route('/api/order', methods=['PUT'])
def update_order():
    updated_order = request.json
    order = next(
        (order for order in orders if order['id'] == updated_order['id']), None)
    if order:
        order.update(updated_order)
        return jsonify(order)
    else:
        return jsonify({"error": "Order not found"}), 404


@app.route('/api/image/<string:id>', methods=['GET'])
def get_image(id):
    return send_from_directory('database/images', id)


if __name__ == '__main__':
    app.run(debug=True, port=8889)
