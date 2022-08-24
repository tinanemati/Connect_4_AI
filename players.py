from cmath import inf
from copy import deepcopy
import random
import sys
import time
import pygame
import numpy as np
import math


class connect4Player(object):
	def __init__(self, position, seed=0):
		self.position = position
		self.opponent = None
		self.seed = seed
		random.seed(seed)

	def play(self, env, move):
		move = [-1]

class human(connect4Player):

	def play(self, env, move):
		move[:] = [int(input('Select next move: '))]
		while True:
			if int(move[0]) >= 0 and int(move[0]) <= 6 and env.topPosition[int(move[0])] >= 0:
				break
			move[:] = [int(input('Index invalid. Select next move: '))]

class human2(connect4Player):

	def play(self, env, move):
		done = False
		while(not done):
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

				if event.type == pygame.MOUSEMOTION:
					pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
					posx = event.pos[0]
					if self.position == 1:
						pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE/2)), RADIUS)
					else: 
						pygame.draw.circle(screen, YELLOW, (posx, int(SQUARESIZE/2)), RADIUS)
				pygame.display.update()

				if event.type == pygame.MOUSEBUTTONDOWN:
					posx = event.pos[0]
					col = int(math.floor(posx/SQUARESIZE))
					move[:] = [col]
					done = True

class randomAI(connect4Player):

	def play(self, env, move):
		possible = env.topPosition >= 0
		indices = []
		for i, p in enumerate(possible):
			if p: indices.append(i)
		move[:] = [random.choice(indices)]

class stupidAI(connect4Player):

	def play(self, env, move):
		possible = env.topPosition >= 0
		indices = []
		for i, p in enumerate(possible):
			if p: indices.append(i)
		if 3 in indices:
			move[:] = [3]
		elif 2 in indices:
			move[:] = [2]
		elif 1 in indices:
			move[:] = [1]
		elif 5 in indices:
			move[:] = [5]
		elif 6 in indices:
			move[:] = [6]
		else:
			move[:] = [0]

class minimaxAI(connect4Player):
	# Evaluation Functions For miniMax AI
	# eval(env) = 1 C1 + 5 C2 + 10 C3
	def eval (self, env):
		# determine the players
		# if self.position == 1:
		# 	player = 1
		# else:
		# 	player = 2
		
		output_dict = {}
		output_dict2 = {}
		# check the rows for self
		for i in range(6):
			count = 0
			#print(self.board[i])
			for j in range(7):
				if env.board[i][j] == self.position:	
					count += 1
				
				# if env.board[i][j] == 2:	
				# 	count -= 1
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
			#print(output_dict)
		# check the rows for opponents
		for i in range(6):
			count = 0
			#print(self.board[i])
			for j in range(7):
				if env.board[i][j] == self.opponent.position:	
					count += 1
				
				# if env.board[i][j] == 2:	
				# 	count -= 1
				else:
					if count == 0:
						continue
					if count in output_dict2:
						output_dict2[count] += 1 
					else:
						output_dict2[count] = 1
						
					count = 0

			if count in output_dict2 and count!=0:
				output_dict2[count] += 1 
			elif not(count in output_dict2) and count != 0 :
				output_dict2[count] = 1
			#print(output_dict)


		# check the columns for self
		for i in range(7):
			count = 0
			for j in range(6):
				if env.board[j][i] == self.position:	
					count += 1
				# elif env.board[j][i] == self.opponent.position:	
				# 	count -= 1
					
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
			#print(output_dict)
		# check the columns for opponents
		for i in range(7):
			count = 0
			for j in range(6):
				if env.board[j][i] == self.opponent.position:	
					count += 1
				# elif env.board[j][i] == self.opponent.position:	
				# 	count -= 1
					
				else:
					if count == 0:
						continue
					if count in output_dict2:
						output_dict2[count] += 1 
					else:
						output_dict2[count] = 1
					count = 0

			if count in output_dict2 and count!=0:
				output_dict2[count] += 1 
			elif not(count in output_dict2) and count != 0 :
				output_dict2[count] = 1
			#print(output_dict)
					
			
		# Check Diagonals for self
		for i in range(-2,4):
			count = 0
			row = env.board.diagonal(i)
			#print(row)
			for j in range(len(row)):
				
				if row[j] == self.position:	
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
			#print(output_dict)
		# Check Diagonals for opponent
		for i in range(-2,4):
			count = 0
			row = env.board.diagonal(i)
			#print(row)
			for j in range(len(row)):
				
				if row[j] == self.opponent.position:	
					count += 1
				else:
					if count == 0:
						continue
					if count in output_dict2:
						output_dict2[count] += 1 
					else:
						output_dict2[count] = 1
					count = 0

			if count in output_dict2 and count!=0:
				output_dict2[count] += 1 
			elif not(count in output_dict2) and count != 0 :
				output_dict2[count] = 1
			#print(output_dict)

		flipped_board = np.fliplr(env.board)
		# check left diagnoals for self
		#print(flipped_board)
		for i in range(-2,4):
			count = 0
			row = flipped_board.diagonal(i)
			#print(row)
			for j in range(len(row)):
				if row[j] == self.position:	
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
		# check left diagnoals for opponent
		#print(flipped_board)
		for i in range(-2,4):
			count = 0
			row = flipped_board.diagonal(i)
			#print(row)
			for j in range(len(row)):
				if row[j] == self.opponent.position:
					count += 1
				else:
					if count == 0:
						continue
					if count in output_dict2:
						output_dict2[count] += 1 
					else:
						output_dict2[count] = 1
					count = 0

			if count in output_dict2 and count!=0:
				output_dict2[count] += 1 
			elif not(count in output_dict2) and count != 0 :
				output_dict2[count] = 1

		#this is where I had to chage the res, but it is still not right
		# I don't know exactly how does it word to fix it. 	
		#print(output_dict)
		#res = 1 * output_dict[1] + 5 * output_dict[2] + 10 * output_dict[3]
		res_self = 1 * output_dict.get(1,0) + 5 * output_dict.get(2,0) + 10 * output_dict.get(3,0)
		res_opponent = 1 * output_dict2.get(1,0) + 5 * output_dict2.get(2,0) + 10 * output_dict2.get(3,0)
		#print("score res from eval: " + res)


		return res_self - res_opponent

	def simulateMove(self, env, move, player):
		env.board[env.topPosition[move]][move] = player
		env.topPosition[move] -= 1
		env.history[0].append(move)
		return env

	def MAX(self, env, prev_move, depth): 
		if env.gameOver(prev_move,self.opponent.position):
			return -inf
		if depth == 0:
			return self.eval(env)
		
		possible = env.topPosition >= 0
		max_v = -inf
		for idx,move in enumerate(possible):
			if move:
				child = self.simulateMove(deepcopy(env), idx, self.opponent.position) 
				max_v = max(max_v, self.MIN(child, idx, depth-1))
		return max_v

	def MIN(self, env,prev_move, depth):
		if env.gameOver(prev_move,self.position):
			return inf
		if depth == 0:
			return self.eval(env)
		possible = env.topPosition >= 0
		max_v = inf
		for idx, move in enumerate(possible):
			if move:
				child = self.simulateMove(deepcopy(env), idx, self.position)
				max_v = min(max_v, self.MAX(child, idx, depth-1)) 
		return max_v
	
	def Minimax(self,env, move, max_depth):
		possible = env.topPosition >= 0
		max_v = -inf
		for idx, next_move in enumerate(possible):
			if next_move: #move is true if possible
				child = self.simulateMove(deepcopy(env), idx, self.opponent.position)
				v = self.MIN(child, idx, max_depth-1)
				if v > max_v:
					max_v = v
					move[:] = [idx]

	def play(self, env, move):
		self.Minimax(deepcopy(env), move, 5)
		print("Finished")

class alphaBetaAI(connect4Player):

		# Evaluation Functions For miniMax AI
	# eval(env) = 1 C1 + 5 C2 + 10 C3
	def eval (self, env):
		# determine the players
		# if self.position == 1:
		# 	player = 1
		# else:
		# 	player = 2
		
		output_dict = {}
		output_dict2 = {}
		# check the rows for self
		for i in range(6):
			count = 0
			#print(self.board[i])
			for j in range(7):
				if env.board[i][j] == self.position:	
					count += 1
				
				# if env.board[i][j] == 2:	
				# 	count -= 1
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
			#print(output_dict)
		# check the rows for opponents
		for i in range(6):
			count = 0
			#print(self.board[i])
			for j in range(7):
				if env.board[i][j] == self.opponent.position:	
					count += 1
				
				# if env.board[i][j] == 2:	
				# 	count -= 1
				else:
					if count == 0:
						continue
					if count in output_dict2:
						output_dict2[count] += 1 
					else:
						output_dict2[count] = 1
						
					count = 0

			if count in output_dict2 and count!=0:
				output_dict2[count] += 1 
			elif not(count in output_dict2) and count != 0 :
				output_dict2[count] = 1
			#print(output_dict)


		# check the columns for self
		for i in range(7):
			count = 0
			for j in range(6):
				if env.board[j][i] == self.position:	
					count += 1
				# elif env.board[j][i] == self.opponent.position:	
				# 	count -= 1
					
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
			#print(output_dict)
		# check the columns for opponents
		for i in range(7):
			count = 0
			for j in range(6):
				if env.board[j][i] == self.opponent.position:	
					count += 1
				# elif env.board[j][i] == self.opponent.position:	
				# 	count -= 1
					
				else:
					if count == 0:
						continue
					if count in output_dict2:
						output_dict2[count] += 1 
					else:
						output_dict2[count] = 1
					count = 0

			if count in output_dict2 and count!=0:
				output_dict2[count] += 1 
			elif not(count in output_dict2) and count != 0 :
				output_dict2[count] = 1
			#print(output_dict)
					
			
		# Check Diagonals for self
		for i in range(-2,4):
			count = 0
			row = env.board.diagonal(i)
			#print(row)
			for j in range(len(row)):
				
				if row[j] == self.position:	
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
			#print(output_dict)
		# Check Diagonals for opponent
		for i in range(-2,4):
			count = 0
			row = env.board.diagonal(i)
			#print(row)
			for j in range(len(row)):
				
				if row[j] == self.opponent.position:	
					count += 1
				else:
					if count == 0:
						continue
					if count in output_dict2:
						output_dict2[count] += 1 
					else:
						output_dict2[count] = 1
					count = 0

			if count in output_dict2 and count!=0:
				output_dict2[count] += 1 
			elif not(count in output_dict2) and count != 0 :
				output_dict2[count] = 1
			#print(output_dict)

		flipped_board = np.fliplr(env.board)
		# check left diagnoals for self
		#print(flipped_board)
		for i in range(-2,4):
			count = 0
			row = flipped_board.diagonal(i)
			#print(row)
			for j in range(len(row)):
				if row[j] == self.position:	
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
		# check left diagnoals for opponent
		#print(flipped_board)
		for i in range(-2,4):
			count = 0
			row = flipped_board.diagonal(i)
			#print(row)
			for j in range(len(row)):
				if row[j] == self.opponent.position:
					count += 1
				else:
					if count == 0:
						continue
					if count in output_dict2:
						output_dict2[count] += 1 
					else:
						output_dict2[count] = 1
					count = 0

			if count in output_dict2 and count!=0:
				output_dict2[count] += 1 
			elif not(count in output_dict2) and count != 0 :
				output_dict2[count] = 1

		#this is where I had to chage the res, but it is still not right
		# I don't know exactly how does it word to fix it. 	
		#print(output_dict)
		#res = 1 * output_dict[1] + 5 * output_dict[2] + 10 * output_dict[3]
		res_self = 1 * output_dict.get(1,0) + 5 * output_dict.get(2,0) + 10 * output_dict.get(3,0)
		res_opponent = 1 * output_dict2.get(1,0) + 5 * output_dict2.get(2,0) + 10 * output_dict2.get(3,0)
		#print("score res from eval: " + res)


		return res_self - res_opponent
		
	def simulateMove(self, env, move, player):
		env.board[env.topPosition[move]][move] = player
		env.topPosition[move] -= 1
		env.history[0].append(move)
		return env

	def MAX(self, env, prev_move, depth, alpha, beta): 
		if env.gameOver(prev_move,self.opponent.position):
			return -inf
		if depth == 0:
			return self.eval(env)
		
		possible = env.topPosition >= 0
		max_v = -inf
		alpha = -inf
		beta = inf
		for idx,move in enumerate(possible):
			if move:
				child = self.simulateMove(deepcopy(env), idx, self.opponent.position) 
				max_v = max(max_v, self.MIN(child, idx, depth-1, alpha, beta))
				alpha = max(alpha, max_v)
				if max_v >= beta:
					break
		return max_v

	def MIN(self, env,prev_move, depth, alpha, beta):
		if env.gameOver(prev_move,self.position):
			return inf
		if depth == 0:
			return self.eval(env)
		possible = env.topPosition >= 0
		max_v = inf
		alpha = -inf
		beta = inf
		for idx, move in enumerate(possible):
			if move:
				child = self.simulateMove(deepcopy(env), idx, self.position)
				max_v = min(max_v, self.MAX(child, idx, depth-1, alpha, beta)) 
				beta = min(beta,max_v)
				if max_v <= alpha:
					break
		return max_v
	
	def AlphabetaPruning(self,env, move, max_depth, alpha,beta):
		possible = env.topPosition >= 0
		max_v = -inf
		for idx, next_move in enumerate(possible):
			if next_move: #move is true if possible
				child = self.simulateMove(deepcopy(env), idx, self.opponent.position)
				v = self.MIN(child, idx, max_depth-1, alpha, beta)
				if v > max_v:
					max_v = v
					move[:] = [idx]

	def play(self, env, move):
		alpha = -inf
		beta = inf
		self.AlphabetaPruning(deepcopy(env), move, 5, alpha, beta)
		print("Finished")


SQUARESIZE = 100
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

ROW_COUNT = 6
COLUMN_COUNT = 7

pygame.init()

SQUARESIZE = 100

width = COLUMN_COUNT * SQUARESIZE
height = (ROW_COUNT+1) * SQUARESIZE

size = (width, height)

RADIUS = int(SQUARESIZE/2 - 5)

screen = pygame.display.set_mode(size)



