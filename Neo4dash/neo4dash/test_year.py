import unittest
from db import *
db = Database()
import main

class testyear(unittest.TestCase):

	def testoneyear(self):
		print("Checking if the first node is of correct type (Year)")
		years = db.filter_by_year(2019)
		print(years)
		first_node = years[0]
		self.assertEqual(first_node['data']['type'], 'Year')

if __name__ == '__main__':
   	unittest.main( )
