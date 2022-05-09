from turtle import Screen, Turtle
import time
from Snake import Snake
from food import Food
from scoreboard import Score

sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("OG Snake game")
sc.tracer(0)
sc.listen()
new_snake = Snake()
food = Food()
score = Score()
sc.onkey(new_snake.up, "Up")
sc.onkey(new_snake.down, "Down")
sc.onkey(new_snake.left, "Left")
sc.onkey(new_snake.right, "Right")

game_on = True

while game_on:
    sc.update()
    time.sleep(0.1)
    new_snake.movement()
    # detecting if the snake head collided with the food
    if new_snake.segment[0].distance(food) < 15:
        food.refresh()
        new_snake.extend()
        score.inc_score()
    # detect collision with tail
    for seg in new_snake.segment:
        if seg == new_snake.segment[0]:
            pass
        elif new_snake.segment[0].distance(seg) < 10:
            game_on = False
            score.gameover()
    # detect collision with wall
    if new_snake.segment[0].xcor() > 280 or new_snake.segment[0].xcor() < -280 or new_snake.segment[0].ycor() > 280 or new_snake.segment[0].ycor() < -280:
         game_on = False
         score.gameover()

sc.exitonclick()
