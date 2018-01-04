#python class example using an integer calculator with the four basic operations

class Calculator():

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def add(self):
		return self.x + self.y

	def subtract(self):
		return self.x - self.y

	def multiply(self):
		return self.x * self.y

	def divide(self):
		return self.x / self.y

print("This is a simple integer calculator.")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer = Calculator(x,y)
choice = 1

while choice != 0:
	print("1. Addition")
	print("2. Subtraction")
	print("3. Multiplication")
	print("4. Division")
	print("0. Quit")
	choice = int(input("Select an operation: "))

	if choice == 1:
		print("Result: ", obj.add())
	elif choice == 2:
		print("Result: ", obj.subtract())
	elif choice == 3:
		print("Result: ", obj.multiply())
	elif choice == 4:
		print("Result: ", obj.divide())
	elif choice == 0:
		print("Exiting")
	else:
		print("Please enter a valid number (0-4): ")



