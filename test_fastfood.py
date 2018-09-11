import unittest
from fastfood import *

class Test_fastfood(unittest.TestCase):

	def test_home(self):
		with app.test_client() as p:
			response = p.get('/api/v1/')
			self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
	unittest.main()