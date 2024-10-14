from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data
menu = [
    {"id": 1, "item": "Pizza", "price": 10.99},
    {"id": 2, "item": "Burger", "price": 8.99},
    {"id": 3, "item": "Pasta", "price": 12.99}
]

orders = []


@app.route('/api/menu', methods=['GET'])
def get_menu():
    menu = {
        "status": "success",
        "data": [
            {
                "id": 1,
                "name": "Margherita",
                "unitPrice": 12,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-1.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "basil"
                ],
                "soldOut": False
            },
            {
                "id": 2,
                "name": "Capricciosa",
                "unitPrice": 14,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-2.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "ham",
                    "mushrooms",
                    "artichoke"
                ],
                "soldOut": True
            },
            {
                "id": 3,
                "name": "Romana",
                "unitPrice": 15,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-3.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "prosciutto"
                ],
                "soldOut": False
            },
            {
                "id": 4,
                "name": "Prosciutto e Rucola",
                "unitPrice": 16,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-4.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "prosciutto",
                    "arugula"
                ],
                "soldOut": False
            },
            {
                "id": 5,
                "name": "Diavola",
                "unitPrice": 16,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-5.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "spicy salami",
                    "chili flakes"
                ],
                "soldOut": False
            },
            {
                "id": 6,
                "name": "Vegetale",
                "unitPrice": 13,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-6.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "bell peppers",
                    "onions",
                    "mushrooms"
                ],
                "soldOut": False
            },
            {
                "id": 7,
                "name": "Napoli",
                "unitPrice": 16,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-7.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "fresh tomato",
                    "basil"
                ],
                "soldOut": False
            },
            {
                "id": 8,
                "name": "Siciliana",
                "unitPrice": 16,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-8.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "anchovies",
                    "olives",
                    "capers"
                ],
                "soldOut": True
            },
            {
                "id": 9,
                "name": "Pepperoni",
                "unitPrice": 14,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-9.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "pepperoni"
                ],
                "soldOut": False
            },
            {
                "id": 10,
                "name": "Hawaiian",
                "unitPrice": 15,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-10.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "pineapple",
                    "ham"
                ],
                "soldOut": False
            },
            {
                "id": 11,
                "name": "Spinach and Mushroom",
                "unitPrice": 15,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-11.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "spinach",
                    "mushrooms"
                ],
                "soldOut": False
            },
            {
                "id": 12,
                "name": "Mediterranean",
                "unitPrice": 16,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-12.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "sun-dried tomatoes",
                    "olives",
                    "artichoke"
                ],
                "soldOut": False
            },
            {
                "id": 13,
                "name": "Greek",
                "unitPrice": 16,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-13.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "spinach",
                    "feta",
                    "olives",
                    "pepperoncini"
                ],
                "soldOut": True
            },
            {
                "id": 14,
                "name": "Abruzzese",
                "unitPrice": 16,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-14.jpg",
                "ingredients": [
                    "tomato",
                    "mozzarella",
                    "prosciutto",
                    "arugula"
                ],
                "soldOut": False
            },
            {
                "id": 15,
                "name": "Pesto Chicken",
                "unitPrice": 16,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-15.jpg",
                "ingredients": [
                    "pesto",
                    "mozzarella",
                    "chicken",
                    "sun-dried tomatoes",
                    "spinach"
                ],
                "soldOut": False
            },
            {
                "id": 16,
                "name": "Eggplant Parmesan",
                "unitPrice": 15,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-16.jpg",
                "ingredients": [
                    "marinara",
                    "mozzarella",
                    "eggplant",
                    "parmesan"
                ],
                "soldOut": False
            },
            {
                "id": 17,
                "name": "Roasted Veggie",
                "unitPrice": 15,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-17.jpg",
                "ingredients": [
                    "marinara",
                    "mozzarella",
                    "zucchini",
                    "eggplant",
                    "peppers",
                    "onions"
                ],
                "soldOut": False
            },
            {
                "id": 18,
                "name": "Tofu and Mushroom",
                "unitPrice": 15,
                "imageUrl": "https://dclaevazetcjjkrzczpc.supabase.co/storage/v1/object/public/pizzas/pizza-18.jpg",
                "ingredients": [
                    "marinara",
                    "mozzarella",
                    "tofu",
                    "mushrooms",
                    "bell peppers"
                ],
                "soldOut": False
            }
        ]
    }
    return jsonify(menu)


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


if __name__ == '__main__':
    app.run(debug=True)
