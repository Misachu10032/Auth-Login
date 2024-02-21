import unittest
from flask_testing import TestCase
from ..app import app

class TestApp(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_sign_up(self):
        response = self.client.post('/api/sign_up', data=dict(
            username='testuser',
            password='testpassword',
            firstname='Test',
            lastname='User',
            email='test@example.com'
        ))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Form validated successfully')

    def test_login(self):
        response = self.client.post('/api/login', data=dict(
            username='testuser',
            password='testpassword'
        ))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json['error'], 'incorrect username or password')

    def test_logout(self):
        response = self.client.post('/api/logout')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Logout successful')

    def test_get_all_users(self):
        response = self.client.get('/api/get_all_users')
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_list', response.json)

    def test_get_all_products(self):
        response = self.client.get('/api/get_all_products')
        self.assertEqual(response.status_code, 200)
        self.assertIn('product_list', response.json)

    def test_get_user_by_id(self):
        response = self.client.get('/api/get_user_by_id/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('user', response.json)

# if __name__ == '__main__':
#     unittest.main()
