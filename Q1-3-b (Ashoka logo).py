import turtle
import math

t = turtle.Turtle()
t.speed(0)

def circles(r, n):
    for i in range(n):
        angle = i * (360 / n)
        
        t.penup()
        x = (r * 0.6) * math.cos(math.radians(angle))  
        y = (r * 0.6) * math.sin(math.radians(angle))
        t.goto(x, y)
        
        t.pendown()
        t.color("maroon")
        t.circle(r)

circles(80, 13)  

turtle.done()
