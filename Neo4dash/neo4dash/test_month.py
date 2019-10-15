import unittest
from db import *
db = Database()
import main

class testmonth(unittest.TestCase):

	def testonemonth(self):
		print("Checking if the first node is of correct type (Month)")
		months = db.filter_by_month(2)
		first_node = months[0]
		self.assertEqual(first_node['data']['type'], 'Month')

if __name__ == '__main__':
   	unittest.main( )
