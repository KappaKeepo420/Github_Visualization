import unittest
from db import *
db = Database()
import main
import filter

class Test_Filter(unittest.TestCase):

	def testoneday(self):
		print("Checking if the first node is of correct type (day)")
		data2, data3 = db.get_all_data(merge=False)
		data4, data5 = filter.filter_by_day(data2, data3, 2)
		days = data4 + data5
		first_node = days[0]
		self.assertEqual(first_node['data']['type'], 'Day')	

	def testonemonth(self):
		print("Checking if the first node is of correct type (Month)")
		month2, month3 = db.get_all_data(merge=False)
		month4, month5 = filter.filter_by_month(month2, month3, 5)
		months = month4 + month5
		first_node = months[1]
		self.assertEqual(first_node['data']['type'], 'Month')

	def testoneyear(self):
		print("Checking if the first node is of correct type (Year)")
		year2, year3 = db.get_all_data(merge=False)
		year4, year5 = filter.filter_by_year(year2, year3, 2019)
		years = year4 + year5
		first_node = years[1]
		self.assertEqual(first_node['data']['type'], 'Year')

if __name__ == '__main__':
   	unittest.main( )
	

