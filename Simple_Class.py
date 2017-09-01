# Simple Python class

class Overwatch:

	def __init__(self, name, main, bracket):
		self.name = name
		self.main = main
		self.bracket = bracket

	def name_with_main(self): 
		return self.name + ', ' + self.main

	def name_with_bracket(self):
		return self.name + ', ' + self.bracket

	def bracket_feedback(self, bracket):
		if bracket == 'Bronze':
			print ("They've got work to do.")
		elif bracket == 'Silver':
			print ("Still not very good.")
		elif bracket == 'Gold':
			print ("Pretty average player.")
		elif bracket == 'Platinum':
			print ("Slightly above average.")
		elif bracket == 'Diamond':
			print ("Very good player.")
		elif bracket == 'Master':
			print ("Amazing skill.")
		elif bracket == 'Grandmaster':
			print ("Top 5% of all players")
		elif bracket == 'Top 500':
			print ("Should be a professional.")
		else:
			print ("That's not a valid bracket.")

Player_1 = Overwatch("Chris", "Junkrat", "Platinum")

print (Player_1.name_with_main())
print (Player_1.name_with_bracket())
print (Player_1.bracket_feedback('Platinum'))