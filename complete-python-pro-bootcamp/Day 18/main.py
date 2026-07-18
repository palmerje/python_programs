import turtle
from turtle import Turtle, Screen
import random
turtle.colormode(255)
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

# TODO Get Timmy to draw a square
# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)



# TODO Aliasing modules
# import turtle as t
# tim = t.Turtle()

# TODO Import from non standard library
# import heroes
# print(heroes.gen())

# TODO Draw a dashed line
# for _ in range (15):
#     timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)

# TODO Draw different shapes
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.left(angle)
#
# for shape_side_n in range(3, 11):
#     timmy_the_turtle.color(random.choice(colors))
#     draw_shape(shape_side_n)

# TODO method to generate a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# TODO Random walk with random colors
# direction = [0, 90, 180, 270]
# def random_walk():
#     timmy_the_turtle.setheading(random.choice(direction))
#     timmy_the_turtle.forward(30)
#
# timmy_the_turtle.speed(0)
# timmy_the_turtle.pensize(10)
# for _ in range(1000):
#     timmy_the_turtle.color(random_color())
#     random_walk()

# TODO Draw a spirograph with turtle
timmy_the_turtle.speed(0)
for _ in range(120):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(3)



screen = Screen()
screen.exitonclick()
