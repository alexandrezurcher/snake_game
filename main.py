from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect colision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.score_point()

    #Detect colision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    #Detec colision with tail
    # for segment in snake.segments:
    #     if segment == snake.head:
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()

    #Detect colision with slicing --> less verbose
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

    #if the head colides with any segment on the tail:
        #triggers game_over


screen.exitonclick()