# See
# http://programmingpraxis.com/2012/07/17/breshenhams-line-drawing-algorithm/

import curses


def breshenham(x0, y0, x1, y1, fn):
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy

    while x0 != x1 and y0 != y1:
        fn(x0, y0)
        err2 = err * 2
        if err2 > -dy:
            err -= dy
            x0 += sx
        if err2 < dx:
            err += dx
            y0 += sy


def draw_line(screen, x0, y0, x1, y1):

    def putpixel(x, y):
        screen.addch(y, x, '*')

    screen.border()
    breshenham(x0, y0, x1, y1, putpixel)
    screen.getch()

curses.wrapper(draw_line, 5, 5, 20, 20)
