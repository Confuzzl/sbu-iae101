# Vincent Yang
# XXXXXXXXX
# viyyang
#
# IAE 101
# Fall, 2024
# Project 2 - Sierpinski Triangle

import turtle

# Color names as strings to be passed to turtle
colors = ['black', 'red', 'green', 'blue', 'white']

# Each of these constants is the index to the corresponding pygame Color object
# in the list, colors, defined above.
BLACK = 0
RED = 1
GREEN = 2
BLUE = 3
WHITE = -1

# This function draws a triangle.
# p1 - is the coordinates of the first vertex of the triangle
# p2 - is the coordinates of the second vertex of the triangle
# p3 - is the coordinates of the third vertex of the triangle
# All coordinates are given as a list of two floats, [x, y] that specify a
# position on the turtle's screen.
# color - is an integer constant used to index into the colors list to select a
# string name for a color.
# line_width - is an integer that determines the thickness of the lines used to
# draw the triangle. The larger the integer the thicker the line.
# If line-width is set to 0, then this function will fill the triangle in with
# the chosen color.
# myTurtle - This variables stores a reference to the Turtle object that draws
# on the screen.
# This function has no return value.


def draw_triangle(p1, p2, p3, color, line_width, myTurtle: turtle.Turtle):
    if line_width == 0:
        myTurtle.color(colors[color])
    else:
        myTurtle.fillcolor(colors[WHITE])
        myTurtle.pensize(line_width)
        myTurtle.pencolor(colors[color])
    myTurtle.up()
    myTurtle.goto(p1[0], p1[1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(p2[0], p2[1])
    myTurtle.goto(p3[0], p3[1])
    myTurtle.goto(p1[0], p1[1])
    myTurtle.end_fill()

# THIS FUNCTION MUST BE COMPLETED BY THE STUDENT.
# This function returns a point that lies at the midpoint between the input
# points.
# p1 - the coordinates of the first point
# p2 - the coordinates of the second point
# Each point is a list of two floats, [x, y]
# The function should return coordinates--a list of two floats--that locate the
# point that is midway between p1 and p2.


def find_midpoint(p1, p2):
    return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]

# THIS FUNCTION MUST BE COMPLETED BY THE STUDENT
# This function draws a tringle, and then recursively calls itself to ensure
# that three smaller triangles are drawn within the new triangle, as described
# by the Sierpinski Triangle algorithm.
# degree - This describes the depth of recursion remaining--how many more levels
# of triangles are going to be drawn in this image.
# p1 - the coordinates of the first vertex of the new triangle
# p2 - the coordinates of the second vertex of the new triangle
# p3 - the coordinates of the third vertex of the new triangle
# color - the color of the new triangle
# line_width - The width of the line used to draw the triangle.
# screen - The pygame surface upon which the Sierpinski triangle will be drawn


def sierpinski(degree, p1, p2, p3, color, line_width, myTurtle):
    draw_triangle(p1, p2, p3, color, line_width, myTurtle)
    if degree <= 1:
        return
    a = find_midpoint(p1, p2)
    b = find_midpoint(p2, p3)
    c = find_midpoint(p1, p3)
    sierpinski(degree-1, p1, a, c, color, line_width, myTurtle)
    sierpinski(degree-1, a, p2, b, color, line_width, myTurtle)
    sierpinski(degree-1, c, b, p3, color, line_width, myTurtle)


def main():
    # Creates a Turtle object that will do the drawing
    myTurtle = turtle.Turtle()
    myTurtle.speed(0)

    # The size of the drawing surface in the horizontal dimension (y)
    width = 640
    # The size of the drawing surface in the vertical dimension (x)
    height = 640

    # These coordinates identify the vertices of the first, outermost triangle.
    # They are set to center the triangle in the drawing surface, and set 5
    # pixels from the borders on each side.
    p1 = [5, height - 5]
    p2 = [(width - 10) / 2, 5]
    p3 = [width - 5, height - 5]
    initial_color = BLACK  # The initial color assigned to the triangle.
    initial_line_width = 1  # The initial line_width assigned to the triangle.
    # Set to 1 to tell the Turtle to draw the triangle
    # with the thinnest possible line and leave the
    # triangle unfilled.

    degree = 5  # The degree of the Sierpinski triangle. This indicates how many
    # levels of recursion to go down while drawing the triangle.

    # Creates the drawing surface of the specified size. A reference to that
    # surface is stored in the variable screen
    screen = turtle.Screen()
    screen.setup(width, height, 20, 20)
    screen.setworldcoordinates(0, height, width, 0)

    # Colors the background of the drawing surface white.
    screen.bgcolor(colors[WHITE])

    # Initial call to the recursive function. This will draw the first,
    # outermost triangle (the degree 0 triangle).
    sierpinski(degree, p1, p2, p3, initial_color, initial_line_width, myTurtle)

    # DON'T CHANGE THE CODE HERE

    screen.exitonclick()
    # DON'T CHANGE THE CODE HERE


# DON'T CHANGE THIS EITHER
if __name__ == "__main__":
    main()
