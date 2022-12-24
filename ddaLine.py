# DDA Line Algorithm
from graphics import *

def plot(x, y):
    p = Point(x, y)
    p.draw(win)

def lineDDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(int(dx)), abs(int(dy)))
    xinc = dx / steps
    yinc = dy / steps
    
    x = x1
    y = y1

    for i in range(steps):
        print("(", round(x), " , ", round(y), ")")
        plot(x, y)
        x += xinc
        y += yinc

x1 = float(input("Enter start point x >>> "))
y1 = float(input("Enter start point y >>> "))
x2 = float(input("Enter end point x >>> "))
y2 = float(input("Enter end point y >>> "))

win = GraphWin("DDA", 600, 600)
lineDDA(x1, y1, x2, y2)

win.getMouse()
win.close()
