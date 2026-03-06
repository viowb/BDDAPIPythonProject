import mysql.connector

# --- Connect ---
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A_ta25!wbY66@",
    database="mydb"
)
cursor = conn.cursor()

# --- CREATE: Add a contact ---
def add_contact(name, phone, email):
    sql = "INSERT INTO contacts (name, phone, email) VALUES (%s, %s, %s)"
    cursor.execute(sql, ('Violet', 946372897, '123@gmail.com'))
    conn.commit()
    print(f"✅ Contact '{name}' added!")

# --- READ: Show all contacts ---
def show_contacts():
    cursor.execute("SELECT * FROM contacts")
    results = cursor.fetchall()
    if not results:
        print("No contacts found.")
    for row in results:
        print(f"[{row[0]}] {row[1]} | 📞 {row[2]} | ✉️ {row[3]}")

# --- UPDATE: Change a phone number ---
def update_phone(contact_id, new_phone):
    sql = "UPDATE contacts SET phone = %s WHERE id = %s"
    cursor.execute(sql, (new_phone, contact_id))
    conn.commit()
    print(f"✅ Phone updated for ID {contact_id}")

# --- DELETE: Remove a contact ---
def delete_contact(contact_id):
    sql = "DELETE FROM contacts WHERE id = %s"
    cursor.execute(sql, (contact_id,))
    conn.commit()
    print(f"🗑️ Contact ID {contact_id} deleted.")

# --- MENU ---
while True:
    print("\n📒 Contact Book")
    print("1. Add contact")
    print("2. Show all contacts")
    print("3. Update phone number")
    print("4. Delete contact")
    print("5. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        n = input("Name: ")
        p = input("Phone: ")
        e = input("Email: ")
        add_contact(n, p, e)
    elif choice == "2":
        show_contacts()
    elif choice == "3":
        i = input("Contact ID: ")
        p = input("New phone: ")
        update_phone(i, p)
    elif choice == "4":
        i = input("Contact ID to delete: ")
        delete_contact(i)
    elif choice == "5":
        print("Goodbye!")
        conn.close()
        break