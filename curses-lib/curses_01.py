#!/usr/bin/env python

import curses
import time
from curses import wrapper


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_RED)

    pad = curses.newpad(100, 100)
    stdscr.refresh()

    for i in range(100):
        for j in range(26):
            char = chr(67 + j)
            color = curses.color_pair(1)
            pad.addstr(char, color)

    for i in range(50):
        stdscr.clear()
        stdscr.refresh()
        pad.refresh(i, 0, 0, 0, 20, 20)
        time.sleep(0.2)

    pad.refresh(5, 5, 5, 5, 25, 25)
    stdscr.getch()


wrapper(main)
