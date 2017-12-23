import turtle

def draw_bar(t, height):
    """ Get turtle t to draw one bar, of height. """
    t.begin_fill()
    t.left(90)
    t.forward(height) # Draw up the left side
    t.right(90)
    t.write('  ' + str(height)) 
    t.forward(40) # Width of bar, along the top
    t.right(90)
    t.forward(height) # and down again!
    t.left(90) # Put turtle facing the way we found it.
    t.end_fill() 
    t.penup()
    t.forward(10) # leave smal gap after each bar
    t.pendown()

xs = [48, 117, 200, 240, 260, 220]

wn = turtle.Screen()
tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)

for v in xs:
    draw_bar(tess, v)
wn.mainloop()
