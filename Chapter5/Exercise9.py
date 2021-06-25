import turtle

def draw_bar(t, height):
    if height >= 200:
        t.color("blue", "red")
    elif height >= 100 and height < 200:
        t.color("blue", "yellow")
    elif height < 100:
        t.color("blue", "green")
    t.begin_fill()
    t.left(90)
    t.forward(height)
    if height > 0:
        t.write(" "+ str(height))
    elif height < 0:
        t.penup()
        t.forward(-14)
        t.write(" "+ str(height))
        t.forward(14)
        t.pendown()
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.forward(10)
    t.pendown()

wn = turtle.Screen()
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("blue", "red")
tess.pensize(3)

xs = [-48,117,200,240,160,260,220]

for length in xs:
    draw_bar(tess, length)
wn.mainloop()
turtle.done()