NUM_ROWS = 4
NUM_COLS = 4
NUM_PLAYERS = 2
NUM_ENTRIES = NUM_COLS*NUM_ROWS
board = []
checkers = ["X","O","V","H","M"]
num_entries = 0
import random
import os

player_turn = random.randint(0, NUM_PLAYERS - 1)

# Creating the empty board

for row in range(NUM_ROWS):
	row_list = []
	for col in range(NUM_COLS):
		row_list.append(" ")
	board.append(row_list)



game_run = True
game_end = "win"

while game_run == True:


	print("  ", end="")
	for col in range(NUM_COLS):
		print(' ' + str(chr(65 + col)) + " ", end=' ')

	print("\n +" + "---+" * NUM_COLS)
	for row in range(NUM_ROWS):
		print(" " + '|', end=' ')
		for col in range(NUM_COLS):
			print(board[row][col] + ' | ', end='')
		print("\n +"+"---+"*NUM_COLS)

	# Choosing a random player to start the game

	print("Player ", checkers[player_turn], ", please enter a column:",sep="", end=" ")


	t = 1

	while t != -1:	 	
		player_input = input()

		# Checking the validity of player input

		if len(player_input) != 1  or ord(player_input) not in range(65, 65+NUM_COLS):
			print("Invalid column entry, please enter a valid column")

		else:
			player_col = ord(player_input) - 65
			t = -1		

			# Placing the checker in board using the valid player column entry.

			for row in range(NUM_ROWS-1, -1, -1):
				if board[row][player_col] == " ":
					board[row][player_col] = checkers[player_turn]
					num_entries += 1
					break
				else:
					pass

			player_turn = (player_turn + 1) % NUM_PLAYERS

		# Printing the board

		print("  ", end="")
		for col in range(NUM_COLS):
			print(' ' + str(chr(65 + col)) + " ", end=' ')

		print("\n +" + "---+" * NUM_COLS)
		for row in range(NUM_ROWS):
			print(" " + '|', end=' ')
			for col in range(NUM_COLS):
				print(board[row][col] + ' | ', end='')
			print("\n +"+"---+"*NUM_COLS)

		print("Player ", checkers[player_turn], ", please enter a column:",sep="")


		# Checking for possible win or draw conditions

		# Draw conditions
		if num_entries == NUM_ENTRIES:
			game_run = False
			game_end = "draw"

		# Win conditions

		for row in range(NUM_ROWS-1, -1, -1):
			for col in range(NUM_COLS):
				if board[row][col] != " ":
					try:
						if col < NUM_COLS-3 and row >= NUM_ROWS-3:
							if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]:
								game_run = False
															
							elif board[row][col] == board[row-1][col+1] == board[row-2][col+2] == board[row-3][col+3]:
								game_run = False
															
							elif board[row][col] == board[row-1][col] == board[row-2][col] == board[row-3][col]:
								game_run = False
															

						elif col < NUM_COLS-3 and row <= NUM_ROWS-3:
							if board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]:
								game_run = False
															
							elif board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]:
								game_run = False
							
								
							elif board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]:
								game_run = False
															

						elif col >= NUM_COLS-3 and row >= NUM_ROWS-3:
							if board[row][col] == board[row-1][col] == board[row-2][col] == board[row-3][col]:
								game_run = False
															
							elif board[row][col] == board[row][col-1] == board[row][col-2] == board[row][col-3]:
								game_run = False
															
							elif board[row][col] == board[row-1][col-1] == board[row-2][col-2] == board[row-3][col-3]:
								game_run = False
															

						elif col >= NUM_COLS-3 and row <= NUM_ROWS-3:
							if board[row][col] == board[row][col-1] == board[row][col-2] == board[row][col-3]:
								game_run = False
															
							elif board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]:
								game_run = False
								
							elif board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3]:
								game_run = False
					except IndexError:
						pass
							

				else:
					pass

		

	os.system("clear")


print("  ", end="")
for col in range(NUM_COLS):
	print(' ' + str(chr(65 + col)) + " ", end=' ')

print("\n +" + "---+" * NUM_COLS)
for row in range(NUM_ROWS):
	print(" " + '|', end=' ')
	for col in range(NUM_COLS):
		print(board[row][col] + ' | ', end='')
	print("\n +"+"---+"*NUM_COLS)


# Printing the results of the game

if game_end == "win":
	print("Game over\n" "Player", checkers[(player_turn + 1) % NUM_PLAYERS], "wins")
elif game_end == "draw":
	print("Game over\n" "Drawn game")




