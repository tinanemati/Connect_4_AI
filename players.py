from cmath import inf
from copy import deepcopy
import random
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

#does the evalution make sense?
class minimaxAI(connect4Player):
	# Evaluation Functions For miniMax AI
	# eval(env) = 1 C1 + 5 C2 + 10 C3
	def eval (self, env):
		# determine the players
		if self.turnPlayer == self.player1:
			player = 1
		else:
			player = 2
		move = self.playTurn()
		# if we win
		if self.gameOver(move, player) and player ==1:
			return inf
		# if we lose
		elif self.gameOver(move, player) and player ==2:
			return -inf
	
		output_dict = {}
		# check the rows
		for i in range(6):
			count = 0
			for j in range(7):
				if self.board[i][j] == player:	
					count += 1
				else:
					if count == 0:
						continue
					if output_dict[count]:
						output_dict[count] += 1 
					else:
						output_dict[count] = 1
					count = 0
			
		# check the columns
		for i in range(7):
			count = 0
			for j in range(6):
				if self.board[j][i] == player:	
					count += 1
				else:
					if count == 0:
						continue
					if output_dict[count]:
						output_dict[count] += 1 
					else:
						output_dict[count] = 1
					count = 0
			
		# Check Diagonals use board.diagonal(0) =  [0, 1, 1, 0, 1, 0, 1]0 to 6
		for i in range(-2,4):
			count = 0
			for j in range(len(self.board.diagonal(i))):
				if self.board[i][j] == player:	
					count += 1
				else:
					if count == 0:
						continue
					if output_dict[count]:
						output_dict[count] += 1 
					else:
						output_dict[count] = 1
					count = 0

		flipped_board = np.fliplr(self.board) 
		for i in range(-3,2):
			count = 0
			for j in range(len(flipped_board.diagonal(i))):
				if self.board[i][j] == player:	
					count += 1
				else:
					if  count == 0:
						continue
					if output_dict[count]:
						output_dict[count] += 1 
					else:
						output_dict[count] = 1
					count = 0
		#how can we know if landas need to be modified?
		#how do we test the eval fundtion?
		res = 1 * output_dict[1] + 5 * output_dict[2] + 10 * output_dict[3]
		#print(res)
		return res

	def simulateMove(self, env, move, player):
		env.board[env.topPosition[move]][move] = player
		env.topPosition[move] -= 1
		env.history[0].append(move)

	def MAX(self, env, depth):
		if env.gameOver(env) or depth == 0:
			return eval(env)
		possible = env.topPosition >= 0
		max_v = -inf
		for move in possible:
			child = self.simulateMove(deepcopy(env), move, self.opponent.position) 
			max_v = max(max_v, self.MIN(child, depth-1))
		return max_v

	def MIN(self, env, depth):
		if env.gameOver(env) or depth == 0:
			return eval(env)
		possible = env.topPosition >= 0
		max_v = inf
		for move in possible:

			child = self.simulateMove(deepcopy(env), move, self.position)
			max_v = min(max_v, self.MAX(child, depth-1))
		return max_v
	
	def Minimax(self,env, move, max_depth):
		possible = env.topPosition >= 0
		max_v = -inf
		for move in possible:
			child = self.simulateMove(deepcopy(env), move, self.opponent.position)
			v = self.MIN(child, max_depth-1)
			if v > max_v:
				max_v = v
				move[:] = [move]

	def play(self, env, move):
		self.Minimax(deepcopy(env), move, 5)
		print("Finished")

class alphaBetaAI(connect4Player):

	def play(self, env, move):
		pass


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




