import curses
import random

class Part(object):
	"""Main component of Snake and Food."""
	x = y = 0

	def __init__(self, y, x):
		self.y = y
		self.x = x

class Food(Part):
	"""Food class that can display at given Part coordinates."""
	screen = None

	def __init__(self, y, x, maxy, maxx, screen):
		super().__init__(y, x)
		self.screen = screen
		self.maxy = maxy
		self.maxx = maxx

	def display(self):
		"""Displays part with \"*\" character."""
		self.screen.addstr(self.y, self.x, '*')

	def new(self):
		"""Generates new part coordinates out of terminal dimensions."""
		self.screen.addstr(self.y, self.x, ' ')
		self.x = random.randrange(0, self.maxx)
		self.y = random.randrange(0, self.maxy)

class Snake(object):
	"""Contains the part data of the snake."""
	parts = []
	screen = None

	def __init__(self, screen, length=5):

		self.screen = screen

		for i in range(length):
			self.parts.append(Part(5, 15 - i))

	def display(self):
		"""Displays all of the snake parts."""
		for i in range(len(self.parts)):
			self.screen.addstr(self.parts[i].y, self.parts[i].x, 'x')

	def delete(self):
		"""Deletes the last snake part in the array."""
		self.screen.addstr(self.parts[-1].y, self.parts[-1].x, ' ')
		del self.parts[-1]

	def move(self, facing, direction=None):
		"""Creates a new snake part in the given direction to add the appearence of movement."""

		if direction == 'u' and facing != 'd':
			self.parts.insert(0, Part(self.parts[0].y - 1, self.parts[0].x))
			return 'u'
		elif direction == 'd' and facing != 'u':
			self.parts.insert(0, Part(self.parts[0].y + 1, self.parts[0].x))
			return 'd'
		elif direction == 'l' and facing != 'r':
			self.parts.insert(0, Part(self.parts[0].y, self.parts[0].x - 1))
			return 'l'
		elif direction == 'r' and facing != 'l':
			self.parts.insert(0, Part(self.parts[0].y, self.parts[0].x + 1))
			return 'r'
		else:
			if facing == 'u':
				self.parts.insert(0, Part(self.parts[0].y - 1, self.parts[0].x))
			elif facing == 'd':
				self.parts.insert(0, Part(self.parts[0].y + 1, self.parts[0].x))
			elif facing == 'l':
				self.parts.insert(0, Part(self.parts[0].y, self.parts[0].x - 1))
			elif facing == 'r':
				self.parts.insert(0, Part(self.parts[0].y, self.parts[0].x + 1))

			return facing
