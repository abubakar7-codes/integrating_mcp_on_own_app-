import sqlite3

DB_FILE = "finance_tracker.db"

def inspect_database():
    """Connects to the database and shows data from the transactions table."""
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        print("\nData from the 'transactions' table:")
        cursor.execute("SELECT * FROM transactions;")
        transactions = cursor.fetchall()
        if transactions:
            # Get column names
            column_names = [description[0] for description in cursor.description]
            print(column_names)
            for transaction in transactions:
                print(transaction)
        else:
            print("No data found in the 'transactions' table.")

        conn.close()

    except sqlite3.Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    inspect_database()
