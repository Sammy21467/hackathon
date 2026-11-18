import turtle

# set up the game window
screen = turtle.Screen()
screen.setup(800, 800)
screen.bgcolor("black")
screen.title("quiz 2 - coding missions")
screen.tracer(0)

# this turtle writes the words and draws the buttons
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# each mission has a question and a small coding challenge
# choices are written as (answer, is it right?)
missions = [
    {
        "name": "mission 1: escape the haunted house",
        "level": "easy",
        "xp": 10,
        "story": "the door needs a secret password to open.",
        "code": ['password = "ghost123"', "", 'if password == "ghost123":',
                 '    print("Door unlocked!")', "else:", '    print("Wrong password!")'],
        "question": "what will happen when this code runs?",
        "choices": [("a. wrong password!", False), ("b. door unlocked!", True),
                    ("c. nothing happens.", False), ("d. an error happens.", False)],
        "hint": "== checks if two values match.",
        "task": "type the line that gives password the secret value:",
        "task_code": ['password = "your password here"'],
        "answer": 'password = "ghost123"',
        "task_hint": 'set password to the text "ghost123".',
    },
    {
        "name": "mission 2: the robot factory",
        "level": "easy",
        "xp": 10,
        "story": "program a robot to put together some boxes.",
        "code": ["for i in range(3):", '    print("Box assembled!")'],
        "question": "how many boxes will the robot assemble?",
        "choices": [("a. 1", False), ("b. 2", False), ("c. 3", True), ("d. 4", False)],
        "hint": "range(3) makes the loop run 3 times: 0, 1, and 2.",
        "task": "type the line that starts a loop that runs 3 times:",
        "task_code": ["# write the for loop line here"],
        "answer": "for i in range(3):",
        "task_hint": "use for i in range(3):",
    },
    {
        "name": "mission 3: the spaceship emergency",
        "level": "easy - medium",
        "xp": 15,
        "story": "the spaceship is running low on fuel.",
        "code": ["fuel = 15", "", "if fuel _____ 20:", '    print("LOW FUEL!")'],
        "question": "which operator makes the warning appear?",
        "choices": [("a. >", False), ("b. <", True), ("c. ==", False), ("d. !=", False)],
        "hint": "< means less than. 15 is less than 20.",
        "task": "type the condition that checks if fuel is below 20:",
        "task_code": ["if fuel _____ 20:"],
        "answer": "fuel < 20",
        "task_hint": "put the variable, less-than sign, and number together.",
    },
    {
        "name": "mission 4: defeat the dragon",
        "level": "medium",
        "xp": 20,
        "story": "your character attacks twice for 20 damage each time.",
        "code": ["int dragonHealth = 100;", "", "dragonHealth -= 20;",
                 "dragonHealth -= 20;", "", "Console.WriteLine(dragonHealth);"],
        "question": "how much health does the dragon have left?",
        "choices": [("a. 20", False), ("b. 40", False), ("c. 60", True), ("d. 80", False)],
        "hint": "-= subtracts from the current value: 100 - 20 - 20 = 60.",
        "task": "the dragon has 200 health. type one line to subtract 50:",
        "task_code": ["int dragonHealth = 200;", "// write your code here!",
                      "Console.WriteLine(dragonHealth);"],
        "answer": "dragonHealth -= 50;",
        "task_hint": "use -= to subtract: dragonHealth -= 50;",
    },
    {
        "name": "mission 5: the treasure chest",
        "level": "medium",
        "xp": 20,
        "story": "find out how many coins you collect.",
        "code": ["coins = 10", "", "coins = coins + 5", "coins = coins * 2", "", "print(coins)"],
        "question": "how many coins do you end up with?",
        "choices": [("a. 15", False), ("b. 20", False), ("c. 25", False), ("d. 30", True)],
        "hint": "first 10 + 5 = 15. then 15 * 2 = 30.",
        "task": "type the line that doubles the number of coins:",
        "task_code": ["coins = 15", "# multiply coins by 2", "print(coins)"],
        "answer": "coins = coins * 2",
        "task_hint": "set coins to its current value times 2.",
    },
    {
        "name": "mission 6: the magic spell",
        "level": "medium - hard",
        "xp": 25,
        "story": "your healing spell works when your mana is high enough.",
        "code": ["int mana = 50;", "", "if (mana >= 40)", "{",
                 '    Console.WriteLine("Spell activated!");', "}", "else", "{",
                 '    Console.WriteLine("Not enough mana!");', "}"],
        "question": "what message will appear?",
        "choices": [("a. not enough mana!", False), ("b. spell activated!", True),
                    ("c. 50", False), ("d. nothing happens.", False)],
        "hint": ">= means greater than or equal to. 50 is greater than 40.",
        "task": "type the condition that checks if mana is at least 40:",
        "task_code": ["if (mana _____ 40)"],
        "answer": "mana >= 40",
        "task_hint": "use >= to mean greater than or equal to: mana >= 40",
    },
    {
        "name": "mission 7: the final boss",
        "level": "hard",
        "xp": 40,
        "story": "the monster loses 25 health each time the loop runs.",
        "code": ["monster_health = 100", "", "while monster_health > 0:",
                 "    monster_health -= 25", "", 'print("Monster defeated!")'],
        "question": "how many times will the loop run?",
        "choices": [("a. 2 times", False), ("b. 3 times", False),
                    ("c. 4 times", True), ("d. 5 times", False)],
        "hint": "it starts at 100 and loses 25 each time. it takes 4 turns to reach 0.",
        "task": "type the condition that loops while health is above 0:",
        "task_code": ["while monster_health _____ :"],
        "answer": "monster_health > 0",
        "task_hint": "use > 0 to loop while health is above zero.",
    },
]

# these remember what part of the game the player is on
current_mission = 0
current_screen = "welcome"
total_xp = 0
button_ys = []


# write one line of text
def write_text(x, y, text, color, size):
    writer.goto(x, y)
    writer.color(color)
    writer.write(text, align="center", font=("arial", size, "bold"))


# write a list of lines, one under the other
def write_lines(lines, y, size):
    for line in lines:
        write_text(0, y, line, "white", size)
        y = y - 22
    return y


# draw a button
def draw_button(y, text, color="white"):
    writer.color(color)
    writer.goto(-270, y - 10)
    writer.setheading(0)
    writer.pendown()
    for i in range(2):
        writer.forward(540)
        writer.left(90)
        writer.forward(34)
        writer.left(90)
    writer.penup()
    write_text(0, y, text, color, 14)


# check if the player clicked a button
def button_hit(x, y, button_y):
    return -275 <= x <= 275 and button_y - 10 <= y <= button_y + 24


# show the first screen
def show_welcome():
    global current_screen
    current_screen = "welcome"
    writer.clear()
    write_text(0, 220, "quiz 2: coding missions", "white", 26)
    write_text(0, 170, "solve each mission, then try writing code yourself!", "white", 15)
    write_text(0, 120, "earn xp as you go. the game is worth 140 xp.", "green", 15)
    draw_button(30, "start missions", "green")
    draw_button(-30, "quit")
    screen.update()


# show a mission and its answer choices
def show_question(wrong_answer=False):
    global current_screen, button_ys
    current_screen = "question"
    writer.clear()
    mission = missions[current_mission]

    write_text(0, 350, mission["name"], "white", 19)
    info = "mission " + str(current_mission + 1) + " of 7"
    info = info + "   |   " + mission["level"] + "   |   " + str(mission["xp"]) + " xp"
    write_text(0, 320, info, "green", 13)
    write_text(0, 285, mission["story"], "white", 14)

    y = write_lines(mission["code"], 250, 13) - 10
    write_text(0, y, mission["question"], "white", 15)

    button_ys = []
    y = y - 38
    for choice in mission["choices"]:
        button_ys.append(y)
        draw_button(y, choice[0])
        y = y - 43

    if wrong_answer:
        write_text(0, y - 5, "not quite. try again!", "red", 15)
        write_text(0, y - 28, mission["hint"], "red", 12)

    screen.update()


# show a message after a right answer
def show_right_answer():
    global current_screen
    current_screen = "right"
    writer.clear()
    mission = missions[current_mission]
    write_text(0, 210, "correct!", "green", 28)
    write_text(0, 155, "nice work! now try a small coding challenge.", "white", 16)
    write_text(0, 105, "you can earn " + str(mission["xp"]) + " xp.", "green", 15)
    draw_button(20, "start coding challenge", "green")
    screen.update()


# show the coding challenge
def show_challenge(wrong_answer=False):
    global current_screen
    current_screen = "challenge"
    writer.clear()
    mission = missions[current_mission]
    write_text(0, 300, "your turn: " + mission["name"], "white", 18)
    write_text(0, 260, mission["task"], "white", 14)
    write_lines(mission["task_code"], 210, 14)
    write_text(0, -80, "click the button and type your code.", "white", 13)

    if wrong_answer:
        write_text(0, -125, "not quite. try again!", "red", 15)
        write_text(0, -153, mission["task_hint"], "red", 12)

    draw_button(-215, "try code", "green")
    screen.update()


# show the score after a mission
def show_mission_score():
    global current_screen
    current_screen = "score"
    writer.clear()
    mission = missions[current_mission]
    write_text(0, 200, "mission complete!", "green", 26)
    write_text(0, 150, "+" + str(mission["xp"]) + " xp", "green", 20)
    write_text(0, 100, "your total: " + str(total_xp) + " xp", "white", 16)

    if current_mission == 6:
        draw_button(20, "see final score", "green")
    else:
        draw_button(20, "next mission", "green")
    screen.update()


# show the score at the end of the game
def show_final_score():
    global current_screen
    current_screen = "done"
    writer.clear()
    write_text(0, 180, "you finished all the missions!", "green", 23)
    write_text(0, 120, "your score: " + str(total_xp) + " / 140 xp", "white", 20)
    write_text(0, 70, "great job practicing your coding!", "white", 16)
    draw_button(0, "quit")
    screen.update()


# check if the code typed by the player is right
def check_code(answer):
    typed_code = "".join(answer.lower().split())
    right_code = "".join(missions[current_mission]["answer"].lower().split())
    return typed_code == right_code


# ask the player to type their code
def ask_for_code():
    global total_xp
    answer = screen.textinput("your coding challenge", "type your code here:")
    if answer is None:
        return

    if check_code(answer):
        total_xp = total_xp + missions[current_mission]["xp"]
        show_mission_score()
    else:
        show_challenge(True)


# go to the next mission
def next_mission():
    global current_mission
    current_mission = current_mission + 1
    if current_mission < len(missions):
        show_question()
    else:
        show_final_score()


# check what the player clicked
def click_action(x, y):
    if current_screen == "welcome":
        if button_hit(x, y, 30):
            show_question()
        elif button_hit(x, y, -30):
            screen.bye()

    elif current_screen == "question":
        for i in range(len(button_ys)):
            if button_hit(x, y, button_ys[i]):
                if missions[current_mission]["choices"][i][1]:
                    show_right_answer()
                else:
                    show_question(True)
                break

    elif current_screen == "right":
        if button_hit(x, y, 20):
            show_challenge()

    elif current_screen == "challenge":
        if button_hit(x, y, -215):
            ask_for_code()

    elif current_screen == "score":
        if button_hit(x, y, 20):
            next_mission()

    elif current_screen == "done":
        if button_hit(x, y, 0):
            screen.bye()


screen.onclick(click_action)
show_welcome()
turtle.done()
