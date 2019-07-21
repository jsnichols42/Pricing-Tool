'''Paper class'''
from decimal import *
class Paper():
	'''This class creates a paper object based on the name, type, and price'''
	def __init__(self, name, typeS, price):
		self.name = name
		self.typeS = typeS
		self.price = price
		
	
	def modify_price(self, newPrice):
		self.price = Decimal(newPrice)

#Instantiated Paper objects for each type of paper
Spaper0 = Paper(0, "1", 6.00)
Spaper1 = Paper(1, "1", 7.00)
Spaper2 = Paper(2, "1", 9.00)
Spaper3 = Paper(3, "1", 9.00)
Spaper4 = Paper(4, "1", 8.00)
Spaper5 = Paper(5, "1", 20.00)

Upaper0 = Paper(0, "2", 4.00)
Upaper1 = Paper(1, "2", 5.00)
Upaper2 = Paper(2, "2", 7.00)
Upaper3 = Paper(3, "2", 7.00)
Upaper4 = Paper(4, "2", 6.00)
Upaper5 = Paper(5, "2", 20.00)