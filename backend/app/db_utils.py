import mysql.connector

def get_mysql_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='123456',
        database='shop'
    )

def create_user(username, password, firstname, lastname, email):
    connection = get_mysql_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            "INSERT INTO user (Username, Password, Firstname, Lastname, Email) "
            "VALUES (%s, %s, %s, %s, %s)",
            (username, password, firstname, lastname, email)
        )
        connection.commit()
    except mysql.connector.Error as err:
        # Handle any MySQL errors
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def get_user_by_username(username):
    connection = get_mysql_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        return user_data
    except mysql.connector.Error as err:
        # Handle any MySQL errors
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def if_username_exist(username):
    connection = get_mysql_connection()
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        existing_user = cursor.fetchone()
        return existing_user
    except mysql.connector.Error as err:
        # Handle any MySQL errors
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()

def test(aa):
    connection = get_mysql_connection()
    cursor = connection.cursor()


    try:
        # Use the cursor to execute the SQL query
        cursor.execute(
            "INSERT INTO test (aaa) "
            "VALUES (%s)",
            (aa,)
        )

        # Commit the transaction
        connection.commit()

        return 'cc'
    except mysql.connector.Error as err:
        # Handle any MySQL errors
        print(f"Error: {err}")

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()