from turtle import Turtle, Screen
import time

START_POS = [(0, 0), (-20, 0), (-40, 0)]
SC = Screen()
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment = []
        self.create_snake()

    def create_snake(self):
        for pos in START_POS:
            self.add_seg(pos)

    def movement(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(DISTANCE)

    def up(self):
        if self.segment[0].heading() != DOWN:
            self.segment[0].setheading(UP)

    def down(self):
        if self.segment[0].heading() != UP:
            self.segment[0].setheading(DOWN)

    def left(self):
        if self.segment[0].heading() != RIGHT:
            self.segment[0].setheading(LEFT)

    def right(self):
        if self.segment[0].heading() != LEFT:
            self.segment[0].setheading(RIGHT)

    def add_seg(self, position):
        new_seg = Turtle("square")
        new_seg.color("White")
        new_seg.penup()
        new_seg.goto(position)
        self.segment.append(new_seg)

    def extend(self):
        self.add_seg(self.segment[-1].position())