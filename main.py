"""
import colorgram
colors = colorgram.extract('image.jpg', 121)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
"""
import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
turtle.speed(0)

color_list = [(235, 235, 241), (230, 222, 200), (235, 221, 229), (135, 162, 193), (66, 93, 121), (154, 79, 56), (211, 167, 109), (135, 184, 145), (76, 104, 85), (214, 83, 65), (225, 209, 110), (201, 150, 177), (215, 228, 216), (226, 165, 189), (31, 58, 74), (224, 79, 93), (69, 56, 46), (39, 63, 59), (141, 136, 109), (118, 125, 162), (78, 63, 45), (98, 141, 152), (56, 62, 78), (118, 160, 94), (173, 190, 215), (49, 71, 73), (227, 174, 166), (51, 70, 66), (176, 202, 182), (85, 57, 43), (173, 200, 208)]
turtle.penup()
turtle.hideturtle()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)
n = 101

for dots in range(1, n):
    turtle.dot(15, random.choice(color_list))
    turtle.forward(50)
    if dots % 10 == 0:
        turtle.setheading(90)
        turtle.forward(50)
        turtle.setheading(180)
        turtle.forward(500)
        turtle.setheading(0)


screen = t.Screen()
screen.exitonclick()