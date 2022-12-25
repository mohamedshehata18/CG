import turtle
turtle.title("Mohamed Shehata")
pt = turtle.Turtle()
def draw_petal(turtle, radius):
    heading = turtle.heading()
    pt.circle(radius, 60)
    pt.left(120)
    pt.circle(radius, 60)
    pt.setheading(heading)

radius = int(turtle.textinput("Radius","What is the radius of the flower? say: 200 "))
petals =int(turtle.textinput("Flower","Enter Number of petals, say: 10"))

pt.speed(20)

for _ in range(petals):
    pt.pencolor("red")
    pt.fillcolor("pink")
    pt.begin_fill()
    draw_petal(pt, radius)
    pt.left(360 / petals)
    pt.end_fill()

turtle.done()



