#!/usr/bin/env python3

import curwrap
import curses
import snake
import time
import os
import sys

stdscr = curses.initscr()

def restart_snake():
	curwrap.endC(stdscr)
	python = sys.executable
	os.execl(python, python, * sys.argv)

def main():
	on = True
	score = 0
	y, x = stdscr.getmaxyx()

	main = curses.newwin(y-1, x, 0, 0)
	stat = curses.newwin(1, x, y-1, 1)
	board = curses.newwin(y-3, x-3, 1, 1)
	boardy, boardx = board.getmaxyx()

	s = snake.Snake(board)
	
	facing = 'r'

	stdscr.nodelay(1)

	foo = snake.Food(10, 10, y - 3, boardx, board)

	grow = False

	while on:
		if score == 0:
			time.sleep(.1)
		else:
			time.sleep(.05 / score * 2)

		if s.parts[0].x == foo.x and s.parts[0].y == foo.y:
			score += 1
			foo.new()
			grow = True

		for i in range(y-1): #left
			main.addstr(i, 0, ' ', curses.A_REVERSE)
		for i in range(y-1): #right
			main.addstr(i, x-2, ' ', curses.A_REVERSE)
		for i in range(x-1): #top
			main.addstr(0, i, ' ', curses.A_REVERSE)
		for i in range(x-1): #bottom
			main.addstr(y-2, i, ' ', curses.A_REVERSE)

		stat.addstr(0, 0, 'Score : ' + str(score))

		c = stdscr.getch()

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


		if c == ord('q'):
			break

		foo.display()

		
		facing = s.move(facing, direction)

		if not grow:
			s.delete()
		else:
			grow = False
		
		if s.parts[0].x == -1 or s.parts[0].x == boardx or s.parts[0].y == -1 or s.parts[0].y == boardy:
			restart_snake()
		else:
			s.display()

		main.refresh()
		stat.refresh()
		board.refresh()
	stdscr.nodelay(0)

try:
	curwrap.startC(stdscr)
	main()
	curwrap.endC(stdscr)
except:
	curwrap.endC(stdscr)
	raise