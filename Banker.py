
class Bank:

	def __init__(self, name, age, balance):
		self.name = name
		self.age = age
		self.balance = balance

	def withdrawal(self, amt):
		if self.balance - amt < 0:
			print ("Insufficient funds.  See a banker for details, or perform a deposit.")
		else:
			self.balance -= amt
			return self.balance

	def deposit(self, amt):
		balance += amt
		return self.balance

	def get_balance(self):
		return self.balance

	def customer_info(self):
		return self.name + ', ' + str(self.age) + ', ' + str(self.balance)


Customer_1 = Bank("Chris Huffman", 32, 10478)
Customer_2 = Bank("Jim Poorman", 49, 220)

print (Customer_1.withdrawal(500))
print ("")
print (Customer_2.withdrawal(221))  
print ("")
print (Customer_1.customer_info())
print ("")
print (Customer_2.customer_info())
print ("")


