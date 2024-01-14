import unittest
from flask import Flask
from server import app


class FizzBuzzTest(unittest.TestCase):

	def setUp(self):
		# set up a test client
		self.app = app.test_client()
		self.app.testing = True


	def test_fizz_buzz_endpoint(self):
		# Test the POST endpoint `/api/fizz-buzz`
		
		# Define the datae to be sent the request 
		data = {"int1":3,"int2":5,"limit":50,"str1":"fizz","str2":"buzz"}
		
		#Send the Post request 
		response = self.app.post('/api/fizz-buzz',json=data)

		# check the response status code
		self.assertEqual(response.status_code, 200)

		# check the response data
		result = response.get_data(as_text=True)
		self.assertEqual(result,'1,2,fizz,4,buzz,fizz,7,8,fizz,buzz,11,fizz,13,14,fizzbuzz,16,17,fizz,19,buzz,fizz,22,23,fizz,buzz,26,fizz,28,29,fizzbuzz,31,32,fizz,34,buzz,fizz,37,38,fizz,buzz,41,fizz,43,44,fizzbuzz,46,47,fizz,49,buzz')


	def test_fizz_buzz_missing_data(self):
		# Test the case data is missing
		
		#Send the Post request 
		response = self.app.post('/api/fizz-buzz',json={})

		# check the response status code
		self.assertEqual(response.status_code, 400)

		# check the response data
		result = response.get_data(as_text=True)
		self.assertEqual(result,"{'int1': ['Missing data for required field.'], 'int2': ['Missing data for required field.'], 'limit': ['Missing data for required field.'], 'str1': ['Missing data for required field.'], 'str2': ['Missing data for required field.']}")


	def test_fizz_buzz_validate_data(self):
		# Test the case data is missing
		data = {"int1":3,"int2":"abc","limit":50,"str1":"fizz","str2":"buzz"}
		#Send the Post request 
		response = self.app.post('/api/fizz-buzz',json=data)

		# check the response status code
		self.assertEqual(response.status_code, 400)

		# check the response data
		result = response.get_data(as_text=True)
		self.assertEqual(result,"{'int2': ['Not a valid integer.']}")
		
	def test_most_frequent_endpoint(self):
		response = self.app.get('/api/most-frequent')
		self.assertEqual(response.status_code, 200)
		result = response.get_json()
		self.assertIn('most_frequent_endpoint', result)
		self.assertIn('hit_count', result)



if __name__ == '__main__':
	unittest.main()