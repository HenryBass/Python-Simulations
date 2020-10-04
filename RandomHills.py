from graphics import *
import random
import time

win_size = 400
win = GraphWin("Hills", win_size, win_size)

while True:
    y = 0
    x = 1
    b = 0
    g = 0
    lasty = 200
    for i in range(0, win_size):
        while y != (lasty - 1) and y != (lasty + 1):
            y = random.randint(0, 400)
        if y > lasty:
            r = 255
        else:
            r = 0
        color = color_rgb(r, g, b)
        point = Point(x, y)
        point.setFill(color)

        try:
            point.draw(win)
        except:
            win.close()
        x += 1
        lasty = y
        time.sleep(.01)
    shape = Rectangle(Point(0, 0), Point(400, 400))
    shape.setFill("white")
    try:
        shape.draw(win)
    except:
        win.close()
