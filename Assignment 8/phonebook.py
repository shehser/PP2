import psycopg2
from config import load_config

def setup_database(cur):
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

def main():
    config = load_config()
    conn = psycopg2.connect(**config)
    conn.autocommit = True
    cur = conn.cursor()

    setup_database(cur)

    # 1. Test Upsert Procedure
    print("\n=== Testing Upsert Procedure ===")
    cur.execute("CALL upsert_contact(%s, %s);", ("John Doe", "1112223333"))
    cur.execute("CALL upsert_contact(%s, %s);", ("John Doe", "4445556666"))
    print("Upsert executed.")

    # 2. Test Bulk Insert with Validation
    print("\n=== Testing Bulk Insert with Validation ===")
    names = ["Alice Smith", "Bob Jones", "Charlie Brown"]
    phones = ["7778889999", "invalid_phone_format", "5556667777"]

    # FIX: Use %s placeholder instead of raw 'None' keyword inside the SQL query string
    cur.execute("CALL bulk_insert_contacts(%s, %s, %s);", (names, phones, None))
    rejected = cur.fetchone()[0]
    print(f"Rejected Records: {rejected}")

    # 3. Test Pattern Search Function
    print("\n=== Testing Pattern Search Function ===")
    cur.execute("SELECT * FROM get_contacts_by_pattern(%s);", ("John",))
    for row in cur.fetchall():
        print(f"Match: {row}")

    # 4. Test Pagination Function
    print("\n=== Testing Pagination Function (Limit 2, Offset 0) ===")
    cur.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (2, 0))
    for row in cur.fetchall():
        print(f"Row: {row}")

    # 5. Test Delete Procedure
    print("\n=== Testing Delete Procedure ===")
    cur.execute("CALL delete_contact(%s);", ("John Doe",))
    print("Delete executed.")

    cur.close()
    conn.close()

if __name__ == '__main__':
    main()
