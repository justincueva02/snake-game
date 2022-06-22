from turtle import Turtle


class Snake:
    def __init__(self):
        self.starting_positions = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0)]
        self.segments = []

        for position in self.starting_positions:
            self.init_turtle(position)

    def init_turtle(self, coordinates):
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
        self.segments[0].forward(20)