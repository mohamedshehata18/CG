# Ellipse Algorithm
from turtle import *

def plot(x, y):
    t1.up()
    t1.goto(x, y)
    t1.down()
    t1.dot(3)

def ellipse(rx, ry, xCenter, yCenter):
    x = 0
    y = ry
    d1 = ((ry* ry) -(rx* rx* ry) +(0.25 * rx* rx))
    dx = 2 * ry* ry* x
    dy = 2 * rx* rx*y

    while (dx < dy):
        print("(", x + xCenter, ",", y + yCenter, ")")
        print("(",-x + xCenter,",", y + yCenter, ")")
        print("(",x + xCenter,",", -y + yCenter,")")
        print("(",-x + xCenter, ",", -y + yCenter, ")")

        plot(x + xCenter, y + yCenter)
        plot(-x + xCenter, y + yCenter)
        plot(x + xCenter, -y + yCenter)
        plot(-x + xCenter, -y + yCenter)
        
        if (d1 < 0):
            x = x + 1
            dx = dx + (2 * ry* ry)
            d1 = d1 + dx + (ry* ry)
        else:
            x = x + 1
            y = y - 1
            dx = dx + (2 * ry* ry)
            dy= dy-(2 * rx* rx)
            d1 = d1 + dx -dy+ (ry* ry)
            d2 = (((ry* ry) * ((x + 0.5) * (x + 0.5))) + ((rx* rx) * ((y -1) * (y -1))) - (rx* rx* ry* ry))
    
    while (y >= 0):
        print("(", x + xCenter, ",", y + yCenter, ")")
        print("(", -x + xCenter, ",", y + yCenter, ")")
        print("(", x + xCenter, ",", -y + yCenter, ")")
        print("(", -x + xCenter, ",", -y + yCenter, ")")

        plot(x + xCenter, y + yCenter)
        plot(-x + xCenter, y + yCenter)
        plot(x + xCenter, -y + yCenter)
        plot(-x + xCenter, -y + yCenter)
        
        if (d2 > 0):
            y = y - 1
            dy= dy-(2 * rx* rx)
            d2 = d2 -dy + (rx* rx)
        else:
            y = y - 1
            x = x + 1
            dx = dx + (2 * ry* ry)
            dy= dy-(2 * rx* rx)
            d2 = d2 + dx -dy+ (rx* rx)

rx = int(input("Enter the ellipse rx >>> "))
ry = int(input("Enter the ellipse ry >>> "))
xCenter = int(input("Enter the ellipse xCenter >>> "))
yCenter = int(input("Enter the ellipse yCenter >>> "))

t1 = Turtle()
t1.speed(0)
t1.ht()
tracer(0)
ellipse(rx, ry, xCenter, yCenter)
# ellipse(20, 35, 12, 3, t1)

done()
