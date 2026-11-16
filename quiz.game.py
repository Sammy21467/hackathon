
from turtle import *

# Set up screen
screen = Screen()
screen.setup(600, 400)
screen.bgcolor("white")
screen.bgpic("welcome.gif")
screen.title("Python Learning Game")

# Hide turtle
writer = Turtle()
writer.hideturtle()
writer.penup()
writer.speed(0)

# Button positions
btn1_x, btn1_y = 300, 50
btn2_x, btn2_y = 300, -20

# Draw buttons
def draw_button(x, y, text):
    writer.goto(x, y)
    writer.color("black")
    writer.write(text, align="center",
                 font=("Arial", 14, "bold"))

draw_button(btn1_x, btn1_y, "Continue")
draw_button(btn2_x, btn2_y, "End")


# Continue action
def continue_action():
    writer.clear()

    # Remove welcome picture
    screen.bgpic("nopic")
    screen.bgcolor("white")

    # Show task
    writer.goto(-200, 100)
    writer.color("black")
    writer.write("Task 1: Print out your name.",
                 font=("Arial", 14, "bold"))

    writer.goto(-200, 50)
    writer.write("Type your answer in the box.",
                 font=("Arial", 12, "normal"))

    # Ask for answer
    answer = screen.textinput("Task 1", "Type your code here:")

    # Check answer
    if answer != None and answer.startswith("print(") and answer.endswith(")") and len(answer) > 7:
        writer.goto(-200, -20)
        writer.color("green")
        writer.write("Correct! Well done!",
                     font=("Arial", 16, "bold"))
    else:
        writer.goto(-200, -20)
        writer.color("red")
        writer.write("Not quite! Try again.",
                     font=("Arial", 16, "bold"))


# End action
def end_action():
    screen.bye()


# Detect button clicks
def click_action(x, y):

    # Continue button
    if 250 <= x <= 350 and 40 <= y <= 70:
        continue_action()

    # End button
    elif 250 <= x <= 350 and -30 <= y <= 0:
        end_action()


# Listen for clicks
screen.onclick(click_action)

done()
# Answer
answer = screen.textinput("Task 2", "Type your code here:")

# Question 2

if answer != None and answer.startswith("import") and answer.endswith("turtle") and len(answer) > 7:
        writer.goto(-200, -20)
        writer.color("green")
        writer.write("Correct! Well done!",
                     font=("Arial", 16, "bold"))
else:
    writer.goto(-200, -20)
    writer.color("red")
    writer.write("Not quite! Try again.",
        font=("Arial", 16, "bold"))
                 