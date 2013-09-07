import curses

def startC(stdscr):
	"""Wraps curses initialization."""
	curses.noecho()
	curses.cbreak()
	curses.curs_set(0)
def endC(stdscr):
	"""Wraps curses exit."""
	curses.curs_set(1)
	curses.echo()
	curses.nocbreak()
	curses.endwin()