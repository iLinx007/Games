NUM_ROWS = 5
NUM_COLS = 5
NUM_PLAYERS = 2
NUM_ENTRIES = NUM_ROWS*NUM_COLS

import random
import os
import time

num = NUM_ENTRIES - 1
hidden_board = []
display_board = []
game_alphabets = []
turn = random.randint(1, NUM_PLAYERS)

player1_score = 0
player2_score = 0

# Creating the list that contains the elements for the game

for m in range(65,65+(NUM_ENTRIES//2) - 1):
	game_alphabets.append(chr(m))

for n in range(97,97+(NUM_ENTRIES//2) - 1):
	game_alphabets.append(chr(n))

x = len(game_alphabets)

for i in range(x, NUM_ENTRIES):
	game_alphabets.append('*')


# Filling the board with the elements of the game

for rows in range(NUM_ROWS):
	row = []
	for cols in range(NUM_COLS):
		if num == 0:
			new_entry = game_alphabets[0]
			row.append(new_entry)
			num -= 1
		else:
			new_entry = game_alphabets[random.randint(0, num)]
			row.append(new_entry)
			game_alphabets.remove(new_entry)
			num -= 1
	hidden_board.append(row)

# Playing the game


run_game = True
while run_game == True:
	run_game = False
	# Prints board that will be displayed to the players

	for row in range(NUM_ROWS):
		row_list = []
		for col in range(NUM_COLS):
			row_list.append("#")
		display_board.append(row_list)
	print("Player 1 score: ", player1_score)
	print("Player 2 score: ", player2_score)
	print("  ", end ="")
	for col in range(NUM_COLS):
		print(' ' + str(chr(65 + col)) + " ", end=' ')

	print("\n +" + "---+" * NUM_COLS)
	for row in range(NUM_ROWS):
		print(str(row) + '|', end=' ')
		for col in range(NUM_COLS):
			print(display_board[row][col] + ' | ', end='')
		print("\n +"+"---+"*NUM_COLS)

	# Accepting and validating 1st user coordinate input

	print("Player ", turn, ": Enter a coordinate (e.g. B3):",sep="", end=" ")

	t = -1

	while t != 1:

		player_input1 = input()
		
		if len(player_input1) <= 1 or player_input1[1:].isdigit() != True or player_input1.isnumeric() == True:
			print("Your coordinate is not valid. Please enter a valid coordinate(e.g. B3)")

		else:

			player_col1 = (ord(player_input1[0])-65)
			player_row1 = (int(player_input1[1:]))


			if ord(player_input1[0]) not in range(65,(65+NUM_COLS)) or display_board[player_row1][player_col1] == " ":
				print("Your coordinate is not valid. Please enter a valid coordinate(e.g. B3)")

			elif player_input1[0].isupper() == True and len(player_input1) == 2 and player_input1[1:].isnumeric() == True:
				if int(player_input1[1]) in range(0,NUM_ROWS) and ord(player_input1[0]) in range(65,65+NUM_COLS):
					t = 1

					player_col1 = (ord(player_input1[0])-65)
					player_row1 = (int(player_input1[1:]))
					x = hidden_board[player_row1][player_col1]
					display_board[player_row1][player_col1] = hidden_board[player_row1][player_col1]
					os.system('clear')

					print("Player 1 score: ", player1_score)
					print("Player 2 score: ", player2_score)
					print("  ", end ="")
					for col in range(NUM_COLS):
						print(' ' + str(chr(65 + col)) + " ", end=' ')

					print("\n +" + "---+" * NUM_COLS)
					for row in range(NUM_ROWS):
						print(str(row) + '|', end=' ')
						for col in range(NUM_COLS):
							print(display_board[row][col] + ' | ', end='')
						print("\n +"+"---+"*NUM_COLS)

				else:
					print("Your coordinate is not valid. Please enter a valid coordinate(e.g. B3)")

			elif len(player_input1) < 2:
				print("Your coordinate is not valid. Please enter a valid coordinate(e.g. B3)")

			else:
				print("Your coordinate is not valid. Please enter a valid coordinate(e.g. B3)")

	print("Player ", turn, ": Enter another coordinate (e.g. B3):",sep="", end=" ")


	# Accepting and validating 2nd user coordinate input

	q = -1
	while q != 1:

		player_input2 = input()
		
		if len(player_input2) <= 1 or player_input1[1:].isdigit() != True or player_input2.isnumeric() == True:
			print("Your coordinate is not valid. Please enter a valid coordinate(e.g. B3)")

		else:

			player_col2 = (ord(player_input2[0])-65)
			player_row2 = (int(player_input2[1:]))

			if ord(player_input2[0]) not in range(65,(65+NUM_COLS)) or display_board[player_row2][player_col2] == " ":
				print("Your coordinate is not valid. Please enter a valid coordinate(e.g. B3)")

			elif player_input2[0].isupper() == True and len(player_input2) == 2 and player_input2[1:].isnumeric() == True:
				if int(player_input2[1]) in range(0,NUM_ROWS) and ord(player_input2[0]) in range(65,65+NUM_COLS):
					q = 1
					player_col2 = (ord(player_input2[0])-65)
					player_row2 = (int(player_input2[1:]))
					y = hidden_board[player_row2][player_col2]
					display_board[player_row2][player_col2] = hidden_board[player_row2][player_col2]
					os.system('clear')

					print("Player 1 score: ", player1_score)
					print("Player 2 score: ", player2_score)

					print("  ", end ="")
					for col in range(NUM_COLS):
						print(' ' + str(chr(65 + col)) + " ", end=' ')

					print("\n +" + "---+" * NUM_COLS)
					for row in range(NUM_ROWS):
						print(str(row) + '|', end=' ')
						for col in range(NUM_COLS):
							print(display_board[row][col] + ' | ', end='')
						print("\n +"+"---+"*NUM_COLS)


				else:
					print("Your coordinate is not valid. Please enter a valid coordinate(e.g. B3)")

			elif len(player_input2) < 2:
				print("Your coordinate is not valid. Please enter a valid coordinate(e.g. B3)")

			else:
				print("Your coordinate is not valid. Please enter a valid coordinate(e.g. B3)")


	#Checks if the cards at the coordinates are the same(i.e. upper case and lower case)
	# and either removes them or flips them over

	if ord(x.upper()) == ord(y) or ord(x.lower()) == ord(y):
		display_board[player_row1][player_col1] = " "
		display_board[player_row2][player_col2] = " "

		if turn == 1:
			player1_score += 2
		if turn == 2:
			player2_score += 2

		turn = turn + 0
		os.system('clear')

		print("Player 1 score: ", player1_score)
		print("Player 2 score: ", player2_score)

		print("  ", end ="")
		for col in range(NUM_COLS):
			print(' ' + str(chr(65 + col)) + " ", end=' ')

		print("\n +" + "---+" * NUM_COLS)
		for row in range(NUM_ROWS):
			print(str(row) + '|', end=' ')
			for col in range(NUM_COLS):
				print(display_board[row][col] + ' | ', end='')
			print("\n +"+"---+"*NUM_COLS)

	elif hidden_board[player_row1][player_col1] == "*" or hidden_board[player_row2][player_col2] == "*":
		if hidden_board[player_row1][player_col1] == "*":
			if hidden_board[player_row2][player_col2].islower() == True:
				new_upper = hidden_board[player_row2][player_col2].upper()
				for row in range(NUM_ROWS):
					for cols in range(NUM_COLS):
						if hidden_board[row][cols] == new_upper:
							display_board[row][cols] = " "

			elif hidden_board[player_row2][player_col2].isupper() == True:
				new_lower = hidden_board[player_row2][player_col2].lower()
				for row in range(NUM_ROWS):
					for cols in range(NUM_COLS):
						if hidden_board[row][cols] == new_lower:
							display_board[row][cols] = " "
					
		if hidden_board[player_row2][player_col2] == "*":
			if hidden_board[player_row1][player_col1].islower() == True:
				new_upper = hidden_board[player_row1][player_col1].upper()
				for row in range(NUM_ROWS):
					for cols in range(NUM_COLS):
						if hidden_board[row][cols] == new_upper:
							display_board[row][cols] = " "

			elif hidden_board[player_row1][player_col1].isupper() == True:
				new_lower = hidden_board[player_row1][player_col1].lower()
				for row in range(NUM_ROWS):
					for cols in range(NUM_COLS):
						if hidden_board[row][cols] == new_lower:
							display_board[row][cols] = " "


		display_board[player_row1][player_col1] = " "
		display_board[player_row2][player_col2] = " "

		if turn == 1:
			player1_score += 3
		elif turn == 2:
			player2_score += 3

		turn = turn + 0
		os.system('clear')

		print("Player 1 score: ", player1_score)
		print("Player 2 score: ", player2_score)

		print("  ", end ="")
		for col in range(NUM_COLS):
			print(' ' + str(chr(65 + col)) + " ", end=' ')

		print("\n +" + "---+" * NUM_COLS)
		for row in range(NUM_ROWS):
			print(str(row) + '|', end=' ')
			for col in range(NUM_COLS):
				print(display_board[row][col] + ' | ', end='')
			print("\n +"+"---+"*NUM_COLS)	


	else:
		display_board[player_row1][player_col1] = "#"
		display_board[player_row2][player_col2] = "#"
		os.system('clear')		


		print("Player 1 score: ", player1_score)
		print("Player 2 score: ", player2_score)
		print("  ", end ="")
		for col in range(NUM_COLS):
			print(' ' + str(chr(65 + col)) + " ", end=' ')

		print("\n +" + "---+" * NUM_COLS)
		for row in range(NUM_ROWS):
			print(str(row) + '|', end=' ')
			for col in range(NUM_COLS):
				print(display_board[row][col] + ' | ', end='')
			print("\n +"+"---+"*NUM_COLS)
		if turn == 1:
			turn += 1
		elif turn == 2:
			turn -= 1

	time.sleep(2)
	os.system('clear')

	for row in range(NUM_ROWS):
		for cols in range(NUM_COLS):
			if display_board[row][cols] != " ":
				run_game = True
				
print("Game over")





