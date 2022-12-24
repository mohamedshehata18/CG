# Line MidPoint Algorithm
from graphics import *

def plot(x, y):
    p = Point(x, y)
    p.draw(win)

def lineMidpoint(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    d = 2 * dy - dx

    x = x1
    y = y1

    while x <= x2:
        print("(", x, " , ", y, ")")
        plot(x, y)
        
        x += 1
        if d < 0:
            d += 2 * dy
        else:
            y += 1
            d += 2 * (dy - dx)

x1 = int(input("Enter start point x >>> "))
y1 = int(input("Enter start point y >>> "))
x2 = int(input("Enter end point x >>> "))
y2 = int(input("Enter end point y >>> "))

win = GraphWin("Midpoint Line Algorithm", 600, 600)
lineMidpoint(x1, y1, x2, y2)

win.getMouse()
win.close()