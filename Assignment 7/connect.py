import psycopg2
from config import DB_CONFIG

def get_connection():
    #returns a connection to the PostgreSQL database.

    return psycopg2.connect(**DB_CONFIG)

def create_tables():
   #Creates the contacts table if it does not already exist
    query = """
    CREATE TABLE IF NOT EXISTS contacts (
        id SERIAL PRIMARY KEY,
        username VARCHAR(100) NOT NULL UNIQUE,
        phone_number VARCHAR(20) NOT NULL
    );
    """
    conn = get_connection()
    if conn:
        try:
            with conn.cursor() as cursor:
                cursor.execute(query)
            conn.commit()
            print("Table 'contacts' successfully initialized.")
        except Exception as e:
            print(f"Error while creating table: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    create_tables()
