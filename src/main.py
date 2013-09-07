#!/usr/bin/env python3

import curwrap
import curses
import snake
import time
import os
import sys

# initializes the curses standard screen
stdscr = curses.initscr()

def restart_snake():
	"""Restarts the CLSnake process."""
	
	# exits curses loop
	curwrap.endC(stdscr)

	# executes CLSnake
	python = sys.executable
	os.execl(python, python, * sys.argv)

	# end of program

def main():
	"""Contains the main loop and game logic."""

	# holds score
	score = 0

	# holds dimensions of terminal window
	y, x = stdscr.getmaxyx()

	#defines the main, stats, and board windows
	main = curses.newwin(y-1, x, 0, 0)
	stat = curses.newwin(1, x, y-1, 1)
	board = curses.newwin(y-3, x-3, 1, 1)

	# holds dimensions for the board window
	boardy, boardx = board.getmaxyx()

	# sets s as the "Snake" object from the snake module
	s = snake.Snake(board)
	
	#sets the direction that the snake initially moves in
	facing = 'r'

	# prevents curses from waiting for character inputs
	stdscr.nodelay(1)

	# initializes first food object
	foo = snake.Food(10, 10, y - 3, boardx, board)

	grow = False

	# main loop
	while True:

		# increases (arbitrary) game speed based on score
		if score == 0:
			time.sleep(.1)
		else:
			time.sleep(.05 / score * 2)

		# adds score if player eats food
		if s.parts[0].x == foo.x and s.parts[0].y == foo.y:
			score += 1
			foo.new()
			grow = True

		# adds snake parts depending on direction
		for i in range(y-1): #left
			main.addstr(i, 0, ' ', curses.A_REVERSE)
		for i in range(y-1): #right
			main.addstr(i, x-2, ' ', curses.A_REVERSE)
		for i in range(x-1): #top
			main.addstr(0, i, ' ', curses.A_REVERSE)
		for i in range(x-1): #bottom
			main.addstr(y-2, i, ' ', curses.A_REVERSE)

		# displays score
		stat.addstr(0, 0, 'Score : ' + str(score))

		# gets pressed character
		c = stdscr.getch()

		# assigns wasd keys to directions
		if c == ord('s'):
			direction = 'd'
		elif c == ord('w'):
			direction = 'u'
		elif c == ord('d'):
			direction = 'r'
		elif c == ord('a'):
			direction = 'l'
		else:
			direction = None

		# quits on press of "q" key
		if c == ord('q'):
			break

		# displays food
		foo.display()
		
		# moves snake based off of direction facing and new direction
		facing = s.move(facing, direction)

		# deletes leftover snake parts if not growing
		if not grow:
			s.delete()
		else:
			grow = False
		
		# sets world boundaries
		if s.parts[0].x == -1 or s.parts[0].x == boardx or s.parts[0].y == -1 or s.parts[0].y == boardy:
			restart_snake()
		else:
			s.display()

		# refreshes all displays
		main.refresh()
		stat.refresh()
		board.refresh()

	# resets to normal character delay
	stdscr.nodelay(0)

# attempts to initialize curses, then start main loop
# if an error occurs, it exits curses as to prevent the terminal from flipping out
try:
	curwrap.startC(stdscr)
	main()
	curwrap.endC(stdscr)
except:
	curwrap.endC(stdscr)
	raise