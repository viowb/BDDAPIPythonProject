from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# --- Database Connection ---
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="A_ta25!wbY66@",
        database="mydb"
    )

# --- ROUTE 1: Home ---
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my Shop API! 🛒",
        "routes": [
            "/products - See all products",
            "/orders - See all orders",
            "/order - Place an order (POST)"
        ]
    })

# --- ROUTE 2: Get all products ---
@app.route('/products')
def get_products():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    conn.close()

    products = []
    for row in results:
        products.append({
            "id": row[0],
            "name": row[1],
            "price": float(row[2]),
            "stock": row[3]
        })
    return jsonify(products)

# --- ROUTE 3: Get all orders ---
@app.route('/orders')
def get_orders():
    conn = get_db()
    cursor = conn.cursor()
    query = """
        SELECT orders.id, users.name, products.name,
               order_items.quantity, products.price, orders.order_date
        FROM orders
        INNER JOIN users ON orders.user_id = users.id
        INNER JOIN order_items ON orders.id = order_items.order_id
        INNER JOIN products ON order_items.product_id = products.id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    orders = []
    for row in results:
        orders.append({
            "order_id": row[0],
            "customer": row[1],
            "product": row[2],
            "quantity": row[3],
            "total": float(row[4] * row[3]),
            "date": str(row[5])
        })
    return jsonify(orders)

# --- ROUTE 4: Place an order (POST) ---
@app.route('/order', methods=['POST'])
def place_order():
    data = request.get_json()
    user_id = data['user_id']
    product_id = data['product_id']
    quantity = data['quantity']

    conn = get_db()
    cursor = conn.cursor()

    # Check stock
    cursor.execute("SELECT stock, name, price FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()

    if not product:
        return jsonify({"error": "Product not found!"}), 404

    if product[0] < quantity:
        return jsonify({"error": f"Not enough stock! Only {product[0]} left."}), 400

    # Create order
    cursor.execute(
        "INSERT INTO orders (user_id, order_date) VALUES (%s, CURDATE())",
        (user_id,)
    )
    order_id = cursor.lastrowid

    # Add order item
    cursor.execute(
        "INSERT INTO order_items (order_id, product_id, quantity) VALUES (%s, %s, %s)",
        (order_id, product_id, quantity)
    )

    # Deduct stock
    cursor.execute(
        "UPDATE products SET stock = stock - %s WHERE id = %s",
        (quantity, product_id)
    )

    conn.commit()
    conn.close()

    total = product[2] * quantity
    return jsonify({
        "message": f"✅ Order placed!",
        "product": product[1],
        "quantity": quantity,
        "total": float(total)
    })

# --- Run the app ---
if __name__ == '__main__':
    app.run(debug=True)




### Step 3 — Run it! Run `app.py` in PyCharm and you should see:* Running on http://127.0.0.1:5000* Debug mode: on




### Step 4 — Open your browser and test: Visit these URLs one by one:**Home:**http://127.0.0.1:5000/```**See all products:**```http://127.0.0.1:5000/products```**See all orders:**```http://127.0.0.1:5000/orders
