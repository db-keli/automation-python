#!/usr/bin/env python
import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle


def main(stdscr):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_GREEN)
    theme = curses.color_pair(1)
    
    x, y = 0, 0
    while True:
        key = stdscr.getkey()
        if key == 'KEY_LEFT':
            x -= -1
        elif key == 'KEY_RIGHT':
            x += 1
        elif key == "KEY_UP":
            y -= 1
        elif key == "KEY_DOWN":
            y += 1
    
        stdscr.clear()
        stdscr.addstr(y, x, "0")
        stdscr.refresh()
    
  

wrapper(main)

    # key = stdscr.getkey()
    # stdscr.addstr(5, 5, f"Key: {key}")
    # stdscr.refresh()
    
    # stdscr.getch()