from turtle import Turtle
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        sammy = Turtle("square")
        sammy.color("white")
        sammy.penup()
        sammy.setposition(position)
        self.snake_body.append(sammy)

    def extend_segment(self):
        self.add_segment(self.snake_body[-1].position())

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def move(self):
        for seg in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[seg-1].xcor()
            new_y = self.snake_body[seg-1].ycor()
            self.snake_body[seg].goto(new_x, new_y)

        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
