import turtle as t
from turtle import Screen
import random

colors = [(235, 252, 243), (198, 13, 32), (248, 236, 25), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62)]
t.colormode(255)
tim = t.Turtle()
tim.pensize(20)
tim.speed("fastest")
tim.hideturtle()

tim_x_pos = -225.00
tim_y_pos = -225.00

for _ in range(10):
    tim.teleport(tim_x_pos, tim_y_pos)
    for _ in range(10):
        tim.dot(20,random.choice(colors))
        tim.penup()
        tim.forward(50)
    tim_y_pos += 50



screen = Screen()
screen.exitonclick()