# my attempt at the Battleship! assignment from codeacademy.com


from random import randint

board = []

for quadrant in range(6):
	board.append(['O'] * 6)

def display_board(board):
	for row in board:
		print (" ".join(row))

print ("Let's play Battleship!")
display_board(board)

def new_row(board):
	return randint(0, len(board) - 1)

def new_col(board):
	return randint(0, len(board) - 1)

game_row = new_row(board)
game_col = new_col(board)

print (game_col)
print (game_row)

guess = 0
for guess in range(5):
	guess += 1
	user_row = int(input("Guess row: "))
	user_col = int(input("Guess column: "))

	if user_row == game_row and user_col == game_col:
		print ("You sunk my battleship! Curses!!")
		print ("You win!")
		break

	else:
		if user_row not in range(6) or user_col not in range(6):
			print ("Your guess is not even in the ocean.  Maybe improve your aim?")

		elif board[user_row][user_col] == 'X':
			print ("You have already unsuccessfully guessed that sector of the game board.")

		else:
			if guess == 5:
				print ("Game Over.")
			else:
				print ("You missed my battleship!")
				board[user_row][user_col] = 'X'
				print ("Guess", guess + 1)

		display_board(board)