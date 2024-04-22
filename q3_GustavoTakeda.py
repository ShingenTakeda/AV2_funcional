import mysql.connector

# Function to establish a connection to the database


def connect_to_database(host, user, password, database):
    return mysql.connector.connect(host=host, user=user, password=password, database=database)

# Function to execute a SQL query and return the results


def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    cursor.close()
    return results

# Function to execute a SQL operation without returning results (insertion, deletion, etc.)


def execute_operation(connection, query, params=None):
    cursor = connection.cursor()
    cursor.execute(query, params)
    connection.commit()
    cursor.close()


# Functions for specific user operations
def insert_user(connection, id, name, country, id_console): return execute_operation(
    connection, "INSERT INTO USERS (id, name, country, id_console) VALUES (%s, %s, %s, %s)", (id, name, country, id_console))


def remove_user(connection, user_id): return execute_operation(
    connection, "DELETE FROM USERS WHERE id = %s", (user_id,))


def get_all_users(connection): return execute_query(
    connection, "SELECT * FROM USERS")

# Main function


def main():
    # Database credentials
    host = "host"
    user = "username"
    password = "password"
    database = "database"

    # Establish connection
    connection = connect_to_database(host, user, password, database)

    # Example usage of functions
    insert_user(connection, 1, "Jonhas", "Brasil", 1)
    print("Users after insertion:")
    print(get_all_users(connection))

    remove_user(connection, 1)
    print("Users after removal:")
    print(get_all_users(connection))

    # Close connection
    connection.close()


if __name__ == "__main__":
    main()
