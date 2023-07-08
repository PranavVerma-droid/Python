# pip install PythonTurtle

from turtle import *


bgcolor("black")
speed(1)
showturtle()
color("orange")



def draw_square(sideLength):
    showturtle()
    penup()
    forward(sideLength / 2)
    pendown()
    left(90)
    forward(sideLength / 2)
    left(90)
    fd(sideLength)
    left(90)
    fd(sideLength)
    left(90)
    fd(sideLength)
    left(90)
    fd(sideLength / 2)
    penup()
    goto(0, 0)
    hideturtle()


def text():
    penup()
    showturtle()
    goto(-132, 0)
    pendown()
    write("PranavVerma-droid", font=("Jetbrains Mono", 20, "normal"))
    penup()
    goto(0,0)
    hideturtle()




    

draw_square(500)
text()



done()