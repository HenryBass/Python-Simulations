import graphics

win_size = 400
x = 0
xcount = 0
y = 0
ycount = 0
redcount = 0

win = graphics.GraphWin("Primes", win_size, win_size)
graph = graphics.GraphWin("Prime Population", win_size, win_size)
time = 0

print("This is a Map of Primes less than 160000 \n"
      "and a Live Graph of Prime Population per 400 Integers.")
while x < win_size * win_size:
    point = graphics.Point(x, y)

    color = "red"
    i = 2

    while i < xcount:

        if xcount%i == 0:
            color = "black"
            break
        i = i+1


    if color == "red":
        redcount += 1
    point.setFill(color)

    x+= 1
    xcount += 1
    if y > win_size ^ 2:
        break
    try:
        point.draw(win)
    except:
        quit()
    if x >= win_size:
        y+= 1
        ycount += 1
        x = 0
        primepop = win_size / redcount
        time += 1
        graphdot = graphics.Point(time, primepop)
        graphdot.setFill("red")
        try:
            graphdot.draw(graph)
        except:
            quit()
        redcount = 0

try:
    win.getMouse()
except:
    win.close()
