from app import mysql

def create_user(username, password, firstname, lastname, email):
    cursor = mysql.connection.cursor()
    cursor.execute(
        "INSERT INTO user (Username, Password, Firstname, Lastname, Email) "
        "VALUES (%s, %s, %s, %s, %s)",
        (username, password, firstname, lastname, email)
    )
    mysql.connection.commit()
    cursor.close()


def get_user_by_username(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE username = %s", (username,))
    user_data = cursor.fetchone()
    cursor.close()
    return user_data


def if_username_exist(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM user WHERE username = %s", (username.data,))
    existing_user = cursor.fetchone()
    cursor.close()

    return existing_user
