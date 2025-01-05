import sqlite3

class ContactManager:
    def __init__(self, db_name='contacts.db'):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        """Create contacts table if it doesn't exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT NOT NULL
        )""")
        self.connection.commit()

    def add_contact(self, name, phone, email):
        """Add a new contact to the database."""
        self.cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        self.connection.commit()

    def view_contacts(self):
        """Retrieve and display all contacts."""
        self.cursor.execute("SELECT * FROM contacts")
        contacts = self.cursor.fetchall()
        if contacts:
            for contact in contacts:
                print(f"Name: {contact[1]}, Phone: {contact[2]}, Email: {contact[3]}")
        else:
            print("No contacts found.")

    def edit_contact(self, old_name, new_name=None, new_phone=None, new_email=None):
        """Edit an existing contact."""
        if new_name:
            self.cursor.execute("UPDATE contacts SET name = ? WHERE name = ?", (new_name, old_name))
        if new_phone:
            self.cursor.execute("UPDATE contacts SET phone = ? WHERE name = ?", (new_phone, old_name))
        if new_email:
            self.cursor.execute("UPDATE contacts SET email = ? WHERE name = ?", (new_email, old_name))
        
        self.connection.commit()

    def delete_contact(self, name):
        """Delete a contact from the database."""
        self.cursor.execute("DELETE FROM contacts WHERE name = ?", (name,))
        self.connection.commit()

    def close(self):
        """Close the database connection."""
        self.connection.close()

def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            old_name = input("Enter the name of the contact to edit: ")
            new_name = input("Enter new name (leave blank to keep current): ")
            new_phone = input("Enter new phone number (leave blank to keep current): ")
            new_email = input("Enter new email address (leave blank to keep current): ")
            manager.edit_contact(old_name, new_name or None, new_phone or None, new_email or None)
        elif choice == '4':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)
        elif choice == '5':
            manager.close()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
