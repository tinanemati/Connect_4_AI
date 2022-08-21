from copy import deepcopy
import random
import time
import pygame
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
		indices = []s
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
	# Evaluation Functions For miniMax AT
	# eval(env) = 1 C1 + 5 C2 + 10 C3
	# Use Hashing to count consecutive pieces
	def eval (self, env):
		env_eval = deepcopy(env)
		output_dict = {}
		# check the rows
		for i in range(6):
			k = 1
			for j in range(len(0, self.board[i]-1)):
				if self.board[i][j] and self.board[i][j] == self.board[i][j+1]:	
					k += 1
				else:
					continue
			count = max(count, k)
			if output_dict[count]:
				output_dict[count] += 1 
			else:
				output_dict[count] = 0
		# check the columns
		for i in range(7):
			k = 1
			for j in range(len(0, self.board[:i]-1)):
				if self.board[:i][j] and self.board[:i][j] == self.board[:i][j+1]:	
					k += 1
				else:
					continue
			count = max(count, k)
			if output_dict[count]:
				output_dict[count] += 1 
			else:
				output_dict[count] = 0

		# Check Diagonals use board.diagonal(0)
		for i in range(-2,3):
			k = 1
			for j in range(len(0, self.board.diagonal(i))):
				if self.board(i)[j] and self.board[i][j] == self.board[i][j+1]:	
					k += 1
				else:
					continue
			count = max(count, k)
			if output_dict[count]:
				output_dict[count] += 1 
			else:
				output_dict[count] = 0

		res = 1 * output_dict[1] + 5 * output_dict[2] + 10 * output_dict[3]
		return res


		

	def play(self, env, move):
		pass

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




