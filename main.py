from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
segments = []


def init_turtle(coordinates):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape('square')
    new_turtle.color('#fff')
    new_turtle.goto(coordinates)
    segments.append(new_turtle)


for position in starting_positions:
    init_turtle(position)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    # for x in range(6):
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
screen.exitonclick()
