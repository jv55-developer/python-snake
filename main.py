from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
# Create snake screen
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake_1 = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake_1.up, "Up")
screen.onkey(snake_1.down, "Down")
screen.onkey(snake_1.left, "Left")
screen.onkey(snake_1.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake_1.move()

    # Detect collision
    if snake_1.head.distance(food) < 15:
        food.relocate()
        scoreboard.increase_score()
        snake_1.extend_segment()

    # Detect collision with wall
    if snake_1.head.xcor() > 280 or snake_1.head.xcor() < -280 or snake_1.head.ycor() > 280 or snake_1.head.ycor() < \
            -280:
        scoreboard.reset()
        snake_1.reset()

    # Detect collision with tail
    for segment in snake_1.snake_body[1:]:
        if snake_1.head.distance(segment) < 10:
            scoreboard.reset()
            snake_1.reset()


screen.exitonclick()
