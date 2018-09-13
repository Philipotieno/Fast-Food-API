''' Write test for status codes for variouse endpoints'''

import unittest
from fast_food import *

class TestFastFood(unittest.TestCase):
    def test_home(self):
        with app.test_client() as tester:
            response = tester.get('/',)
            self.assertEqual(response.status_code, 200)

    def test_home_data(self):
        with app.test_client() as tester:
            result = tester.get('/')
            self.assertEqual(result.data, b'{"message":"welcome to Fast-Food-Fast"}\n')

    def test_wrongmethod(self):
        self.assertEqual(app.test_client().post('/').status_code, 405)


    def test_register(self):
        with app.test_client() as tester:
            response = tester.get('/api/v1/register',)
            self.assertEqual(response.status_code, 405)

    def test_login(self):
        with app.test_client() as tester:
            response = tester.get('/api/v1/login')
            self.assertEqual(response.status_code, 405)


    def test_make_order(self):
        with app.test_client() as tester:
            response = tester.get('/api/v1/make_order',)
            self.assertEqual(response.status_code, 405)


    def test_update_order(self):
        with app.test_client() as tester:
            self.assertEqual(tester.get('api/v1/update_order/1').status_code, 405)
            self.assertEqual(tester.get('api/v1/update_order').status_code, 404)

    def test_delete_order(self):
        with app.test_client() as tester:
            self.assertEqual(tester.get('/api/v1/delete_order/1').status_code, 405)


if __name__ == '__main__':
    unittest.main()
