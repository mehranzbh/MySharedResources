import pandas as pd
import mysql.connector
from mysql.connector import Error

#password='3OR74u'
# Load the CSV file
csv_file_path = './access-code.csv'
df = pd.read_csv(csv_file_path)

# Database connection details
config = {
    'user': 'pythonuser',  # replace with your MySQL username
    'password': '3OR74u',  # replace with your MySQL password
    'host': 'localhost',  # or your database host
    'database': 'sakila',  # replace with your database name
}

# Function to connect to the MySQL database and return the connection object
def connect_to_database(config):
    try:
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print("Successfully connected to the database.")
            return conn
    except Error as e:
        print(f"Error: {e}")
        return None

# Function to update the actor table with access codes
def update_actor_access_codes(df, conn):
    cursor = conn.cursor()
    
    # Check if the 'access_code' column exists, and add it if it does not
    cursor.execute("SHOW COLUMNS FROM actor LIKE 'access_code';")
    result = cursor.fetchone()
    if result is None:
        cursor.execute("ALTER TABLE actor ADD COLUMN access_code VARCHAR(255);")
        print("Added 'access_code' column to 'actor' table.")

    # Update the actor table with access codes from the CSV
    for index, row in df.iterrows():
        try:
            cursor.execute(
                "UPDATE actor SET access_code = %s WHERE actor_id = %s;",
                (row['access_code'], row['actor_id'])
            )
            conn.commit()
        except Error as e:
            print(f"Error: {e}")
            conn.rollback()  # rollback the transaction on error

    cursor.close()

# Main process
def main():
    # Connect to the database
    conn = connect_to_database(config)
    if conn is not None:
        try:
            # Update access codes in the actor table
            update_actor_access_codes(df, conn)
            print("The actor table has been updated with access codes.")
        finally:
            # Close the connection
            if conn.is_connected():
                conn.close()
                print("Database connection closed.")

# Run the main function
if __name__ == "__main__":
    main()
