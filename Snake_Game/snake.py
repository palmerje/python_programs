from turtle import Turtle

starting_positions = [(0,0),(-20,0),(-40,0)]

segments = []

def Snake():
    global starting_positions
    for position in starting_positions:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        segments.append(new_segment)