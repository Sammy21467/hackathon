# imports
from turtle import *
import random

# choose a random picture
picture = random.randint(1, 5)

# start of drawing

if picture == 1:
    # image 1 - half circle
    penup()
    goto(200, -50)
    pendown()
    circle(75, 180)

elif picture == 2:
    # image 2 - triangle
    penup()
    goto(0, 0)
    pendown()
    for i in range(3):
        forward(100)
        left(120)

elif picture == 3:
    # image 3 - square
    penup()
    goto(0, 0)
    pendown()
    for i in range(4):
        forward(100)
        left(90)

elif picture == 4:
    # image 4
    penup()
    goto(0, 0)
    pendown()
    for i in range(5):
        forward(200)
        left(90)
        forward(100)

elif picture == 5:
    # image 5 - circle
    penup()
    goto(-300, 200)
    pendown()
    for i in range(1):
        circle(100, 360)

done()