import csv
import os
import psycopg2
from config import load_config

def setup_database(cur):
    """Resets the database table and reloads functions/procedures from SQL files."""
    print("Initializing database...")
    cur.execute("DROP TABLE IF EXISTS contacts CASCADE;")
    cur.execute("""
        CREATE TABLE contacts (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)

    with open('functions.sql', 'r', encoding='utf-8') as f:
        cur.execute(f.read())

    with open('procedures.sql', 'r', encoding='utf-8') as f:
        cur.execute(f.read())
    print("Table and procedures successfully loaded.")

def insert_from_csv(cur, file_path):
    """Imports contacts from a CSV file using the bulk_insert_contacts procedure."""
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return

    names = []
    phones = []
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) >= 2:
                    name, phone = row[0].strip(), row[1].strip()
                    # Skip headers if present
                    if name.lower() in ("username", "name") or phone.lower() in ("phone", "phone_number"):
                        continue
                    names.append(name)
                    phones.append(phone)

        if names:
            # Execute database bulk procedure with validation
            cur.execute("CALL bulk_insert_contacts(%s, %s, %s);", (names, phones, None))
            rejected = cur.fetchone()[0]
            print(f"Import finished. Rejected records (invalid format): {rejected}")
        else:
            print("No valid data found in the CSV file.")
    except Exception as e:
        print(f"Error during CSV import: {e}")


def main():
    config = load_config()
    conn = psycopg2.connect(**config)
    conn.autocommit = True
    cur = conn.cursor()

    # Prompt user whether to recreate schema on startup
    setup_database(cur)

    while True:
        print("\n=== PhoneBook CLI (Procedures & Functions) ===")
        print("1. Add/Update Contact (Upsert)")
        print("2. Import from CSV (Bulk Insert)")
        print("3. Find Contacts by Name Pattern")
        print("4. List Contacts (Pagination)")
        print("5. Delete Contact")
        print("0. Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            name = input("Enter contact name: ").strip()
            phone = input("Enter phone number: ").strip()
            if name and phone:
                cur.execute("CALL upsert_contact(%s, %s);", (name, phone))
                print(f"Upsert procedure executed for '{name}'.")
            else:
                print("Name and phone fields cannot be empty!")

        elif choice == "2":
            path = input("Enter path to CSV file (e.g., contacts.csv): ").strip()
            insert_from_csv(cur, path)

        elif choice == "3":
            pattern = input("Enter name pattern or substring to search: ").strip()
            cur.execute("SELECT * FROM get_contacts_by_pattern(%s);", (pattern,))
            results = cur.fetchall()

            print(f"\nMatches found: {len(results)}")
            for row in results:
                print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")

        elif choice == "4":
            try:
                limit = int(input("Enter row limit (default 10): ").strip() or 10)
                offset = int(input("Enter offset/rows to skip (default 0): ").strip() or 0)
                cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
                results = cur.fetchall()

                print(f"\nData Page (Limit: {limit}, Offset: {offset}):")
                for row in results:
                    print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
            except ValueError:
                print("Error: Limit and Offset must be valid integers.")

        elif choice == "5":
            name_to_delete = input("Enter the exact contact name to delete: ").strip()
            if name_to_delete:
                cur.execute("CALL delete_contact(%s);", (name_to_delete,))
                print(f"Delete procedure executed for '{name_to_delete}'.")
            else:
                print("Name cannot be empty.")

        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid command. Please try again.")

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
