from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

segments = []
def set_turtle_attributes(segment, position):
    segment.penup()
    segment.shape("square")
    segment.color("white")
    segment.setposition(position)

x=0
for s in range(3):
    segment = Turtle()
    set_turtle_attributes(segment, (x, 0))
    x -= 20
    segments.append(segment)



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    for num_seg in range(len(segments)-1, 0, -1):
        new_x = segments[num_seg - 1].xcor()
        new_y = segments[num_seg - 1].ycor()
        segments[num_seg].goto(new_x, new_y)
    segments[0].forward(2)











screen.exitonclick()