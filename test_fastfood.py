import unittest
from fastfood import *

class Test_fastfood(unittest.TestCase):

	def test_home(self):
		with app.test_client() as p:
			response = p.get('/api/v1/',)
			self.assertEqual(response.status_code, 200)

	def test_wrongmethod(self):
		self.assertEqual(app.test_client().post('/api/v1/').status_code, 405)
	
	def test_register(self):
		with app.test_client() as h:
			response = h.get('/api/v1/register',)
			self.assertEqual(response.status_code, 405)

	def test_login(self):
		with app.test_client() as i:
			response = i.get('/api/v1/login')
			self.assertEqual(response.status_code, 405)
			
	def test_make_order(self):
		with app.test_client() as l:
			response = l.get('/api/v1/make_order',)
			self.assertEqual(response.status_code, 405)

	def test_update_order(self):
		with app.test_client() as p:
			self.assertEqual(p.get('api/v1/update_order/1').status_code, 405)
			self.assertEqual(p.get('api/v1/update_order').status_code, 404)


	def test_delete_order(self):
		with app.test_client() as tester:
			self.assertEqual(tester.get('/api/v1/delete_order/1').status_code, 405)

if __name__ == '__main__':
	unittest.main()