import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A_ta25!wbY66@",
    database="mydb"
)
cursor = conn.cursor()

# --- JOIN: See who borrowed which book and who wrote it ---
def show_borrowings():
    query = """
        SELECT books.title, authors.name, members.member_name, borrowings.borrow_date
        FROM borrowings
        INNER JOIN books ON borrowings.book_id = books.id
        INNER JOIN authors ON books.author_id = authors.id
        INNER JOIN members ON borrowings.member_id = members.id
    """
    cursor.execute(query)
    results = cursor.fetchall()
    print("\n📚 Library Borrowings:")
    print("-" * 55)
    for row in results:1

        print(f"📖 {row[0]} | ✍️ {row[1]} | 👤 {row[2]} | 📅 {row[3]}")
    print("-" * 55)

# --- ADD a new borrowing ---
def borrow_book(book_id, member_id, date):
    sql = "INSERT INTO borrowings (book_id, member_id, borrow_date) VALUES (%s, %s, %s)"
    cursor.execute(sql, (book_id, member_id, date))
    conn.commit()
    print(f"✅ Book ID {book_id} borrowed by Member ID {member_id}!")

# --- MENU ---
while True:
    print("\n📚 Library System")
    print("1. Show all borrowings")
    print("2. Borrow a book")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        show_borrowings()
    elif choice == "2":
        b = input("Book ID (1=Harry Potter, 2=Animal Farm): ")
        m = input("Member ID (1=Violet, 2=Alice): ")
        d = input("Date (YYYY-MM-DD): ")
        borrow_book(b, m, d)
    elif choice == "3":
        print("Goodbye!")
        conn.close()
        break