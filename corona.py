import turtle
turtle.title("Mohamed Shehata")
sc = turtle.Screen()
t = turtle.Turtle()
sc.bgcolor('black')
t.color('green')
t.penup()
t.goto(0,170)
t.speed(30)
t.hideturtle()
t.pendown()
b = 0
while b < 200:
    t.right(b)
    t.forward(b*3)
    b = b + 1
turtle.done()