import random
from turtle import Turtle, Screen

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_input = my_screen.textinput(title="Make your bet",
                                 prompt="Which turtle will win the race?\n Choose a color: red, orange, "
                                        "yellow, green, blue, purple")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

x_pos = -230
y_pos = -180
i = 0
turtles = []
for _ in range(6):
    turtlex = Turtle(shape="turtle")
    turtlex.color(colors[i])
    turtles.append(turtlex)
    i += 1
    turtlex.penup()
    turtlex.goto(x_pos, y_pos)
    y_pos += 73

continue_race = True
while continue_race:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            continue_race = False
            winner = turtle.fillcolor()
            if user_input == winner:
                print(f"You win, The {winner} turtle is the winner!")
            else:
                print(f"You lose, the {winner} turtle is the winner!")
        else:
            turtle.forward(random.randint(0, 10))

my_screen = Screen()
my_screen.exitonclick()
