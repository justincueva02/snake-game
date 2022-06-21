from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

tim = Turtle()


def init_turtle(arg):
    new_turtle = Turtle()
    new_turtle.color('#fff')
    new_turtle.shape('square')
    new_turtle.setpos(arg * 20, 0)


number_of_turtles = 3
for x in range(number_of_turtles):
    init_turtle(x)


screen.exitonclick()
