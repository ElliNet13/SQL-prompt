import sqlite3

# Function to execute SQL commands
def execute_sql_command(conn, command):
    cursor = conn.cursor()
    try:
        cursor.execute(command)
        if command.strip().lower().startswith('select'):
            rows = cursor.fetchall()
            if rows:
                print("Result:")
                for row in rows:
                    print(row)
            else:
                print("No rows found.")
        else:
            print("Command executed successfully.")
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error executing command: {e}")
    finally:
        cursor.close()

# Function to connect to a database
def connect_to_database(database_name):
    try:
        conn = sqlite3.connect(database_name)
        print("Connected to database successfully.")
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return None

# Main function
def main():
    # Input database name
    database_name = input("Enter database name (e.g., my_database.db): ")
    conn = connect_to_database(database_name)
    if not conn:
        return

    while True:
        # Input SQL command
        command = input("Enter SQL command (or type 'exit' to quit)> ")
        if command.lower() == 'exit':
            break
        execute_sql_command(conn, command)

    conn.close()
    print("Connection closed.")

if __name__ == "__main__":
    main()