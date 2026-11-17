# imports
from turtle import *

screen = Screen()
screen.setup(600, 400)
screen.bgcolor("white")
screen.title("Python Learning Game")

# (we use screen.update() to show each screen when it is ready)
screen.tracer(0)

# show the welcome picture (the game still works if the picture is missing)
has_picture = True
try:
    screen.bgpic("welcome.gif")
except:
    has_picture = False

# this turtle is only used to write text and draw buttons
writer = Turtle()
writer.hideturtle()
writer.penup()

# add more tasks here (then add a check for them in check_answer below)
tasks = [
    "Print out your name.",
]

# these keep track of where the player is
current_task = 0     # 0 means the first task
state = "welcome"    # welcome, question, correct, or done

# write text on the screen
def write_text(x, y, text, color, size):
    writer.goto(x, y)
    writer.color(color)
    writer.write(text, align="center", font=("Arial", size, "bold"))
# draw a button: a box with text inside
def draw_button(x, y, text):
    writer.color("black")
    writer.goto(x - 60, y - 10)
    writer.setheading(0)
    writer.pendown()
    for i in range(2):
        writer.forward(120)
        writer.left(90)
        writer.forward(35)
        writer.left(90)
    writer.penup()
    write_text(x, y, text, "black", 14)
# check if a click landed on a button
def button_hit(click_x, click_y, button_x, button_y):
    return button_x - 60 <= click_x <= button_x + 60 and button_y - 10 <= click_y <= button_y + 25
# the welcome screen
def show_welcome():
    global state          # "global" lets this function change the variable
    state = "welcome"
    writer.clear()
    if not has_picture:
        write_text(0, 90, "Python Learning Game", "black", 24)
    draw_button(0, -40, "Continue")
    draw_button(0, -100, "End")
    screen.update()       # Show everything we just drew
# a task screen (message is the feedback, like "Not quite!")
def show_question(message="", color="black"):
    global state
    state = "question"
    writer.clear()
    write_text(0, 130, "Task " + str(current_task + 1) + " of " + str(len(tasks)), "blue", 14)
    write_text(0, 90, tasks[current_task], "black", 14)
    write_text(0, 55, "Click Answer, then type your code.", "gray", 12)
    draw_button(0, -30, "Answer")
    write_text(0, -90, message, color, 16)
    screen.update()
# shown when the answer is right
def show_correct():
    global state
    state = "correct"
    writer.clear()
    write_text(0, 60, "Correct! Well done!", "green", 20)
    if current_task == len(tasks) - 1:
        draw_button(0, -30, "Finish")
    else:
        draw_button(0, -30, "Continue")
    screen.update()
# shown after the last task
def show_done():
    global state
    state = "done"
    writer.clear()
    write_text(0, 60, "You finished all the tasks!", "green", 20)
    write_text(0, 20, "Great job learning Python!", "black", 14)
    draw_button(0, -60, "End")
    screen.update()
# Task 1 check: print("name") with at least one letter inside the quotes
def check_print_name(answer):
    # it must look like print( ... )
    if not (answer.startswith("print(") and answer.endswith(")")):
        return False
    # get the part between print( and )
    inside = answer[6:-1]
    # ut must start and end with the same quote mark, like "Sam" or 'Sam'
    if len(inside) < 3:
        return False
    if inside[0] != "\"" and inside[0] != "'":
        return False
    if inside[-1] != inside[0]:
        return False

    # looks at the name between the quotes and search for a letter
    name = inside[1:-1]
    found_letter = False
    for character in name:
        if character.isalpha():
            found_letter = True
    return found_letter
# decide if the typed answer is right for the current task
def check_answer(answer):
    # remove extra spaces and make it lowercase so it is easier to check
    answer = answer.strip().lower()

    if current_task == 0:
        return check_print_name(answer)
    elif current_task == 1:
        return answer == "import turtle" or answer.startswith("from turtle import")
    elif current_task == 2:
        return "forward(" in answer and "100" in answer
    elif current_task == 3:
        return "left(" in answer and "90" in answer
    elif current_task == 4:
        return answer.startswith("for") and "range(4)" in answer and answer.endswith(":")
    return False


# open the box where the player types their answer
def ask_question():
    answer = screen.textinput("Task " + str(current_task + 1), "Type your code here:")
    if answer is None:        # they pressed Cancel
        return
    if check_answer(answer):
        show_correct()
    else:
        show_question("Not quite! Try again.", "red")
# go to the next task or finish if there are no more
def next_task():
    global current_task
    current_task = current_task + 1
    if current_task < len(tasks):
        show_question()
    else:
        show_done()
# start the game from the welcome screen
def start_game():
    global current_task
    current_task = 0
    screen.bgpic("nopic")     # removes the welcome picture
    screen.bgcolor("white")
    show_question()
# closse the window
def end_game():
    screen.bye()
# runs every time the player clicks
def click_action(x, y):
    if state == "welcome":
        if button_hit(x, y, 0, -40):
            start_game()
        elif button_hit(x, y, 0, -100):
            end_game()
    elif state == "question":
        if button_hit(x, y, 0, -30):
            ask_question()
    elif state == "correct":
        if button_hit(x, y, 0, -30):
            next_task()
    elif state == "done":
        if button_hit(x, y, 0, -60):
            end_game()

screen.onclick(click_action)
show_welcome()
done()