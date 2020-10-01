import graphics

def start():

    win_size = float(input("\nWindow Size: "))
    timeElapsed = 0
    x = float(input("Starting X Pos: "))
    y = float(input("Starting Y Pos: "))
    x_force = float(input("X Force: "))

    y_force = float(input("Gravity Force: "))
    win = graphics.GraphWin("Gravity", win_size, win_size)

    while True:
        point = graphics.Point(x, y)
        y_force = y_force + y_force
        y = y + y_force
        point.setFill("red")
        timeElapsed = timeElapsed + 1
        x = x + x_force
        try:
            point.draw(win)
        except:
            start()
start()

