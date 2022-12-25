from turtle import *

tu = Turtle()

tu.speed(0)
tu.hideturtle()
tu.pensize(5)
tu.color("blue")
tu.seth(20)
# first star
for i in range(7):
    tu.fd(45)
    tu.lt(51.4)
    tu.fd(45)
    tu.lt(128.6)
    tu.fd(45)
    tu.lt(51.4)
    tu.fd(45)
    tu.lt(180)

tu.up()
tu.setpos(110,-50)
tu.down()

# second star
for i in range(7):
    tu.fd(45)
    tu.lt(51.4)
    tu.fd(45)
    tu.lt(128.6)
    tu.fd(45)
    tu.lt(51.4)
    tu.fd(45)
    tu.lt(180)

# the octagonal shape
tu.seth(67.4)
tu.circle(120,360,8)


#the letter drawing
tu.up()
tu.setpos(335,65)
tu.seth(180)
tu.down()
tu.pensize(10)
tu.color("black")
tu.seth(135)
tu.circle(100,270,3)
tu.seth(135)
tu.circle(100,270,3)
done()