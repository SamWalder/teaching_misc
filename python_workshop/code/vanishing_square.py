from turtle import *
from math import *

def square(side):

    for i in range(0,4):
        tom.forward(side)
        tom.right(90)

def new_length(side, ratio):
    return sqrt(pow(side*ratio,2)+pow(side*(1-ratio),2))

def angle(side,ratio):
    return atan((1-ratio)/ratio)/(8*atan(1))*360

tom=Turtle()

tom.penup()
tom.goto(x=-150,y=150)
tom.pendown()

n=100
side=350.
ratio=0.95
color=1.

for i in range(0,n):
    actual_color=1-color
    tom.pencolor((actual_color,actual_color,actual_color))
    square(side)
    tom.forward((1-ratio)*side)
    tom.right(angle(side,ratio))
    side=new_length(side,ratio)
    color*=ratio

#this hides the turtle
tom.hideturtle()

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="vanishing_square.eps")

#this is needed in some situations to keep the turtle console open
tom.getscreen()._root.mainloop()

