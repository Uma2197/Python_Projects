import random
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue",
           "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for n_sides in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(n_sides)

screen = Screen()
screen.exitonclick()
