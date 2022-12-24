#Circle MidPoint Algorithm
from turtle import *

def plot(x, y):
    t1.up()
    t1.goto(x, y)
    t1.down()
    t1.dot(3)

def circleMidpoint(r):
    x = 0
    y = r
    p = 1 - r

    while x < y:
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
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

r = int(input("Enter the circle radius >>> "))

t1 = Turtle()
t1.speed(0)
t1.ht()
tracer(0)
circleMidpoint(r)

done()