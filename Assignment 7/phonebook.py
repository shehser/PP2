import csv
import os
from connect import get_connection

# CRUD OPERATIONS

def insert_from_console(username, phone):
    #1. Insert or update a contact from the console input.
    query = """
    INSERT INTO contacts (username, phone_number)
    VALUES (%s, %s)
    ON CONFLICT (username)
    DO UPDATE SET phone_number = EXCLUDED.phone_number;
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (username, phone))
        conn.commit()
    print(f"Contact '{username}' successfully saved/updated.")


def insert_from_csv(file_path):
    #2. Bulk import contacts from a CSV file
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    query = """
    INSERT INTO contacts (username, phone_number)
    VALUES (%s, %s)
    ON CONFLICT (username)
    DO UPDATE SET phone_number = EXCLUDED.phone_number;
    """
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            with get_connection() as conn:
                with conn.cursor() as cursor:
                    count = 0
                    for row in reader:
                        if len(row) >= 2:
                            username, phone = row[0].strip(), row[1].strip()
                            cursor.execute(query, (username, phone))
                            count += 1
                conn.commit()
        print(f"Successfully imported {count} contacts from CSV.")
    except Exception as e:
        print(f"Error during CSV import: {e}")


def update_contact(old_name, new_name=None, new_phone=None):
    #3. Update a contact's username, phone number, or both.
    if not new_name and not new_phone:
        print("No update data provided.")
        return

    # Dynamic SQL generation based on provided arguments
    if new_name and new_phone:
        query = "UPDATE contacts SET username = %s, phone_number = %s WHERE username = %s;"
        params = (new_name, new_phone, old_name)
    elif new_name:
        query = "UPDATE contacts SET username = %s WHERE username = %s;"
        params = (new_name, old_name)
    else:
        query = "UPDATE contacts SET phone_number = %s WHERE username = %s;"
        params = (new_phone, old_name)

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            updated_rows = cursor.rowcount
        conn.commit()

    if updated_rows > 0:
        print("Contact successfully updated.")
    else:
        print("Contact not found.")


def query_contacts(filter_type, value):
    """4. Query contacts using specific filters (substring or prefix)."""
    if filter_type == "name":
        # ILIKE is used for case-insensitive substring matching
        query = "SELECT username, phone_number FROM contacts WHERE username ILIKE %s;"
        params = (f"%{value}%",)
    elif filter_type == "prefix":
        # Matches phone numbers starting with a specific prefix
        query = "SELECT username, phone_number FROM contacts WHERE phone_number LIKE %s;"
        params = (f"{value}%",)
    else:
        print("Invalid filter type.")
        return []

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()


def delete_contact(value, by_phone=False):
    """5. Delete a contact by either username or phone number."""
    if by_phone:
        query = "DELETE FROM contacts WHERE phone_number = %s;"
    else:
        query = "DELETE FROM contacts WHERE username = %s;"

    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (value,))
            deleted_rows = cursor.rowcount
        conn.commit()

    if deleted_rows > 0:
        print(f"Successfully deleted {deleted_rows} contact(s).")
    else:
        print("No matching contact found to delete.")


# COMMAND LINE INTERFACE (CLI)

def main():
    while True:
        print("\n=== PhoneBook CLI ===")
        print("1. Add Contact (Console)")
        print("2. Import from CSV")
        print("3. Update Contact (Name/Phone)")
        print("4. Search Contacts")
        print("5. Delete Contact")
        print("0. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            name = input("Enter username: ").strip()
            phone = input("Enter phone number: ").strip()
            if name and phone:
                insert_from_console(name, phone)
            else:
                print("Username and phone number fields cannot be empty!")

        elif choice == "2":
            path = input("Enter path to CSV file (e.g., contacts.csv): ").strip()
            insert_from_csv(path)

        elif choice == "3":
            old_name = input("Enter CURRENT username to modify: ").strip()
            print("Leave the field empty if you do not wish to change it.")
            new_name = input("New username: ").strip() or None
            new_phone = input("New phone number: ").strip() or None
            update_contact(old_name, new_name, new_phone)

        elif choice == "4":
            print("Select filter type:\n1. By Name (or substring)\n2. By Phone Prefix (e.g., +7707)")
            f_choice = input("> ").strip()
            val = input("Enter search query: ").strip()

            if f_choice == "1":
                results = query_contacts("name", val)
            elif f_choice == "2":
                results = query_contacts("prefix", val)
            else:
                print("Invalid choice.")
                continue

            print(f"\nFound {len(results)} record(s):")
            for name, phone in results:
                print(f"name {name} — phone {phone}")

        elif choice == "5":
            print("Delete by:\n1. Username\n2. Phone Number")
            d_choice = input("> ").strip()
            val = input("Enter value to delete: ").strip()

            if d_choice == "1":
                delete_contact(val, by_phone=False)
            elif d_choice == "2":
                delete_contact(val, by_phone=True)
            else:
                print("Invalid choice.")

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
