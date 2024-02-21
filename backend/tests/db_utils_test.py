import unittest
from unittest.mock import patch, MagicMock
from app.db_utils import (
    get_mysql_connection,
    create_user,
    get_user_by_username,
    if_username_exist,
    get_all_users_from_db,
    get_all_products_from_db,
    get_user_by_id_from_db,
    delete_user_by_id_from_db,
)

class TestYourModule(unittest.TestCase):

    @patch('your_module_name.mysql.connector.connect')
    def test_get_mysql_connection(self, mock_connect):
        get_mysql_connection()
        mock_connect.assert_called_with(
            host='localhost',
            user='root',
            password='123456',
            database='shop'
        )

    @patch('your_module_name.get_mysql_connection')
    def test_create_user(self, mock_connection):
        mock_cursor = MagicMock()
        mock_connection.return_value.cursor.return_value = mock_cursor

        create_user('test_user', 'test_password', 'John', 'Doe', 'john@example.com')

        mock_cursor.execute.assert_called_with(
            "INSERT INTO user (Username, Password, Firstname, Lastname, Email) "
            "VALUES (%s, %s, %s, %s, %s)",
            ('test_user', 'test_password', 'John', 'Doe', 'john@example.com')
        )
        mock_connection.return_value.commit.assert_called_once()

    @patch('your_module_name.get_mysql_connection')
    def test_get_user_by_username(self, mock_connection):
        mock_cursor = MagicMock()
        mock_connection.return_value.cursor.return_value = mock_cursor

        get_user_by_username('test_user')

        mock_cursor.execute.assert_called_with("SELECT * FROM user WHERE username = %s", ('test_user',))
        mock_cursor.fetchone.assert_called_once()

    @patch('your_module_name.get_mysql_connection')
    def test_if_username_exist(self, mock_connection):
        mock_cursor = MagicMock()
        mock_connection.return_value.cursor.return_value = mock_cursor

        if_username_exist('test_user')

        mock_cursor.execute.assert_called_with("SELECT * FROM user WHERE username = %s", ('test_user',))
        mock_cursor.fetchone.assert_called_once()

    @patch('your_module_name.get_mysql_connection')
    def test_get_all_users_from_db(self, mock_connection):
        mock_cursor = MagicMock()
        mock_connection.return_value.cursor.return_value = mock_cursor

        get_all_users_from_db()

        mock_cursor.execute.assert_called_with("SELECT * FROM user")
        mock_cursor.fetchall.assert_called_once()

    @patch('your_module_name.get_mysql_connection')
    def test_get_all_products_from_db(self, mock_connection):
        mock_cursor = MagicMock()
        mock_connection.return_value.cursor.return_value = mock_cursor

        get_all_products_from_db()

        mock_cursor.execute.assert_called_with("SELECT * FROM products")
        mock_cursor.fetchall.assert_called_once()

    @patch('your_module_name.get_mysql_connection')
    def test_get_user_by_id_from_db(self, mock_connection):
        mock_cursor = MagicMock()
        mock_connection.return_value.cursor.return_value = mock_cursor

        get_user_by_id_from_db(1)

        mock_cursor.execute.assert_called_with("SELECT * FROM user WHERE ID = %s", (1,))
        mock_cursor.fetchone.assert_called_once()

    @patch('your_module_name.get_mysql_connection')
    def test_delete_user_by_id_from_db(self, mock_connection):
        mock_cursor = MagicMock()
        mock_connection.return_value.cursor.return_value = mock_cursor

        delete_user_by_id_from_db(1)

        mock_cursor.execute.assert_called_with("DELETE FROM user WHERE ID = %s", (1,))
        mock_connection.return_value.commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()
