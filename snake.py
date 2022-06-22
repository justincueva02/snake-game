from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.starting_positions = STARTING_POSITIONS
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in self.starting_positions:
            self.create_segment(position)

    def create_segment(self, coordinates):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape('square')
        new_turtle.color('#fff')
        new_turtle.goto(coordinates)
        self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segments[0].setheading(90)
        print('up')

    def down(self):
        self.segments[0].setheading(270)
        print('down')

    def left(self):
        self.segments[0].setheading(180)
        print('left')

    def right(self):
        self.segments[0].setheading(0)
        print('right')
