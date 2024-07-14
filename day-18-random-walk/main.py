import random
import turtle
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.speed("fastest")
        tim.circle(100)
        tim.color(random_color())
        tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
# "wheat", "SlateGray", "SeaGreen"]
# directions = [0, 90, 180, 270]

# for _ in range(200):
#     #tim.forward(30)
#     tim.color(random_color())
#     #tim.color(random.choice(colours))
#     #tim.setheading(random.choice(directions))
#     #tim.width(15)
#     tim.speed("fastest")


screen = Screen()
screen.exitonclick()
