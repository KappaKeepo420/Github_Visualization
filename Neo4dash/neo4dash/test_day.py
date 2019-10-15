import unittest
from db import *
db = Database()
import main

class testday(unittest.TestCase):

	def testoneday(self):
		print("Checking if the first node is of correct type (day)")
		days = db.filter_by_day(2)
		first_node = days[0]
		self.assertEqual(first_node['data']['type'], 'Day')

if __name__ == '__main__':
   	unittest.main( )
	


