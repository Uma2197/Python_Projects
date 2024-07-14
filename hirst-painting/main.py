import random
import turtle
from turtle import Turtle, Screen
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(249, 228, 18), (212, 13, 9), (197, 12, 35), (231, 228, 5), (197, 69, 20), (32, 90, 188), (43, 212, 70), (234, 149, 40), (33, 31, 152), (16, 22, 55), (66, 9, 48), (240, 245, 251), (244, 39, 149), (65, 203, 229), (14, 205, 222), (63, 21, 10), (223, 20, 110), (229, 164, 9), (15, 154, 23), (245, 57, 16), (98, 75, 9), (248, 11, 9), (223, 139, 203), (67, 241, 160), (10, 97, 61), (5, 38, 33), (67, 219, 155)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = Screen()
screen.exitonclick()