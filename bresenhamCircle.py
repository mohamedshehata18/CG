#Circle Bresenham's Algorithm
from turtle import *

def plot(x, y):
    t1.up()
    t1.goto(x, y)
    t1.down()
    t1.dot(3)

def circleBresenham(r):
    x = 0
    y = r
    p = 3 - 2 * r

    while y >= x:
        plot(x, y)
        plot(y, x)
        plot(-x, y)
        plot(-y, x)
        plot(-x, -y)
        plot(-y, -x)
        plot(y, -x)
        plot(x, -y)
        print("(", x, " , ", y, ")")
        
        x += 1
        if p > 0:
            y -= 1
            p += 4 * (x-y) + 10
        else:
            p += 4 * x + 6

r = int(input("Enter the circle radius >>> "))
t1 = Turtle()
t1.speed(5)
t1.ht()
tracer(0)
circleBresenham(r)
done()