import math
import numpy

def eval (board, turnPlayer):
		# determine the players
		if turnPlayer == player1:
			player = 1
		else:
			player = 2
			
		
		# # check the rows
		# for i in range(6):
		# 	count = 0
		# 	print(board[i])
		# 	for j in range(7):
		# 		if board[i][j] == player:	
		# 			count += 1
					
		# 		else:
		# 			if count == 0:
		# 				continue
		# 			if count in output_dict:
		# 				output_dict[count] += 1 
		# 			else:
		# 				output_dict[count] = 1
					
		# 			count = 0
		# 	if count in output_dict and count!=0:
		# 		output_dict[count] += 1 
		# 	elif not(count in output_dict) and count != 0 :
		# 		output_dict[count] = 1
		# 	print(output_dict)


		# # check the columns
		# for i in range(7):
		# 	count = 0
		# 	for j in range(6):
		# 		if board[j][i] == player:	
		# 			count += 1
					
		# 		else:
		# 			if count == 0:
		# 				continue
		# 			if count in output_dict:
		# 				output_dict[count] += 1 
		# 			else:
		# 				output_dict[count] = 1
					
		# 			count = 0
		# 	if count in output_dict and count!=0:
		# 		output_dict[count] += 1 
		# 	elif not(count in output_dict) and count != 0 :
		# 		output_dict[count] = 1
		# 	print(output_dict)
					
			
		
		# Check Diagonals use
		# output_dict = {}
		# for i in range(-2,4):
		# 	count = 0
		# 	row = board.diagonal(i)
		# 	print(row)
		# 	for j in range(len(row)):
				
		# 		if row[j] == player:	
		# 			count += 1
		# 		else:
		# 			if count == 0:
		# 				continue
		# 			if count in output_dict:
		# 				output_dict[count] += 1 
		# 			else:
		# 				output_dict[count] = 1
					
		# 			count = 0
		# 	if count in output_dict and count!=0:
		# 		output_dict[count] += 1 
		# 	elif not(count in output_dict) and count != 0 :
		# 		output_dict[count] = 1
		# 	print(output_dict)
		flipped_board = numpy.fliplr(board)
		print(flipped_board)
		output_dict = {}
		for i in range(-2,4):
			count = 0
			row = flipped_board.diagonal(i)
			print(row)
			for j in range(len(row)):
				
				if row[j] == player:	
					count += 1
				else:
					if count == 0:
						continue
					if count in output_dict:
						output_dict[count] += 1 
					else:
						output_dict[count] = 1
					
					count = 0
			if count in output_dict and count!=0:
				output_dict[count] += 1 
			elif not(count in output_dict) and count != 0 :
				output_dict[count] = 1
			print(output_dict)


a = numpy.array([[1,1,0,0,2,2,2],
				 [1,2,0,2,0,0,2],
				 [2,1,0,2,1,0,1],
				 [2,2,0,2,2,1,1],
				 [1,1,0,2,0,1,0],
				 [1,0,0,2,2,1,0]]
				)
# a_flipped = [[2 2 2 0 0 1 1]
#  			   [2 0 0 2 0 2 1]
#  			   [1 0 1 2 0 1 2]
#  			   [1 1 2 2 0 2 2]
#  			   [0 1 0 2 0 1 1]
#  			   [0 1 2 2 0 0 1]]
# row count answer:

# column count answer:
# {2: 2}
# {2: 2, 1: 3}
# {2: 2, 1: 3}
# {2: 2, 1: 3}
# {2: 2, 1: 4}
# {2: 2, 1: 4, 3: 1}
# {2: 3, 1: 4, 3: 1}

#diagonal answer:

player1 = 1
player = 2
count_player1 = eval(a, 1)
# count_player2 = eval(a, 2)


