import curses

def startC(stdscr):
	curses.noecho()
	curses.cbreak()
	curses.curs_set(0)
def endC(stdscr):
	curses.curs_set(1)
	curses.echo()
	curses.nocbreak()
	curses.endwin()