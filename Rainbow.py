# Name: Mohamed Mohamed Shehata Badawy
# CS department
import turtle
turtle.title("Mohamed Shehata")
rainbow = turtle.Turtle()
turtle.bgcolor("lightblue")
rainbow.speed(20000)
rainbow.width(10)
for _ in range(90):
    rainbow.penup()
    rainbow.forward(120)
    rainbow.pendown()
    
    rainbow.pencolor("violet")
    rainbow.forward(20)
    
    
    rainbow.pencolor("indigo")
    rainbow.forward(20)
    
        
    rainbow.pencolor("blue")
    rainbow.forward(20)
    
        
    rainbow.pencolor("green")
    rainbow.forward(20)
    
        
    rainbow.pencolor("yellow")
    rainbow.forward(20)
    
        
    rainbow.pencolor("orange")
    rainbow.forward(20)
    
    rainbow.pencolor("red")
    rainbow.forward(20)
    
    rainbow.penup()
    rainbow.setposition(0,0)
    rainbow.penup()
    
    rainbow.left(2)
    
turtle.write("Mohamed Shehata")
turtle.done()

