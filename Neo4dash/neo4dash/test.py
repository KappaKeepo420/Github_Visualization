import unittest
from db import *
db = Database()
import main

class Test_Filter(unittest.TestCase):

	def testoneday(self):
		print("Checking if the first node is of correct type (day)")
		days = db.filter_by_day(2)
		first_node = days[0]
		self.assertEqual(first_node['data']['type'], 'Day')	

	def testonemonth(self):
		print("Checking if the first node is of correct type (Month)")
		months = db.filter_by_month(2)
		first_node = months[0]
		self.assertEqual(first_node['data']['type'], 'Month')

	def testoneyear(self):
		print("Checking if the first node is of correct type (Year)")
		years = db.filter_by_year(2019)
		first_node = years[0]
		self.assertEqual(first_node['data']['type'], 'Year')



if __name__ == '__main__':
   	unittest.main( )
	

