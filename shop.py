import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A_ta25!wbY66@",
    database="mydb"
)
cursor = conn.cursor()

# --- SHOW all products ---
def show_products():
    cursor.execute("SELECT * FROM products")
    results = cursor.fetchall()
    print("\n🛒 Available Products:")
    print("-" * 45)
    for row in results:
        print(f"[{row[0]}] {row[1]} | 💰 ${row[2]} | 📦 Stock: {row[3]}")
    print("-" * 45)

# --- PLACE an order ---
def place_order(user_id, product_id, quantity):
    # Check stock first
    cursor.execute("SELECT stock, name, price FROM products WHERE id = %s", (product_id,))
    product = cursor.fetchone()

    if not product:
        print("❌ Product not found!")
        return

    if product[0] < quantity:
        print(f"❌ Not enough stock! Only {product[0]} left.")
        return

    # Create the order
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
    total = product[2] * quantity
    print(f"✅ Order placed! {quantity}x {product[1]} | Total: ${total:.2f}")

# --- SHOW all orders ---
def show_orders():
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
    print("\n📋 All Orders:")
    print("-" * 60)
    for row in results:
        total = row[3] * row[4]
        print(f"Order[{row[0]}] 👤 {row[1]} | 📦 {row[2]} x{row[3]} | 💰 ${total:.2f} | 📅 {row[5]}")
    print("-" * 60)

# --- MENU ---
while True:
    print("\n🏪 Online Shop")
    print("1. Show products")
    print("2. Place an order")
    print("3. Show all orders")
    print("4. Quit")

    choice = input("Choose an option: ")

  #The `int()` wrapper converts the text `"2"` into the number `2` — problem solved!
    if choice == "1":
        show_products()
    elif choice == "2":
        show_products()
        u = int(input("Your User ID (1=Alice, 2=Bob): "))
        p = int(input("Product ID: "))
        q = int(input("Quantity: "))
        place_order(u, p, q)
    #### 💡 Rule to Remember
#input()  always returns TEXT
#int()    converts text to a whole number
#loat()  converts text to a decimal number

    elif choice == "3":
        show_orders()
    elif choice == "4":
        print("Goodbye! 👋")
        conn.close()
        break