import turtle
import random

def draw_multi_squares(t):
    for i in range(200):
        t.left(2)
        t.forward(i+3)
        t.left(90)
def draw_squares(t, hm):
    for i in hm:
        for e in range(4):
            t.forward(i)
            t.left(90)
        t.penup()
        t.forward(i)
        t.pendown()


def pretty_pattern(t, sz):
    for i in range(40):
        for e in range(4):
            t.forward(sz)
            t.left(90+i)
        t.penup()
        t.left(20)
        t.pendown()

def draw_poly(t, n, sz):
    for i in range(n):
        t.forward(sz)
        t.left(360/n)
    return None

wn = turtle.Screen() # Set up window and it's attributes
wn.bgcolor("#321768")

tess = turtle.Turtle()
tess.pensize(2)
tess.speed(0)
tess.hideturtle()
tess.color('#120F26')
draw_multi_squares(tess)
tess.penup()
tess.setpos(0, -350)
tess.setheading(0)
tess.pendown()
draw_squares(tess, [10, 20, 30, 40, 80, 100, 80, 40, 30, 20, 10])
tess.setpos(-420, -350)
draw_squares(tess, [10, 20, 30, 40, 80, 100, 80, 40, 30, 20, 10])
wn.mainloop()

