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
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        print(user_data)
        if user_data:
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


def get_all_users_from_db():
    print('ccca')
    connection = get_mysql_connection()
    print('ccc')
    cursor = connection.cursor(dictionary=True)
    print('ccc')
    try:
        cursor.execute("SELECT * FROM user")
        users = cursor.fetchall()

        user_list = [dict(user) for user in users]

        return user_list

    except mysql.connector.Error as err:
        # Handle any MySQL errors
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


def get_all_products_from_db():
    connection = get_mysql_connection()
    # Use dictionary cursor for easier JSON conversion
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()

        # Convert the result to a list of dictionaries
        product_list = [dict(product) for product in products]

        return product_list
    except mysql.connector.Error as err:
        # Handle any MySQL errors
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
