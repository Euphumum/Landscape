import turtle

joey = turtle.Turtle()
rico = turtle.Turtle()
ethan = turtle.Turtle()


joey.speed(15)
rico.speed(15)
ethan.speed(15)


joey.color("forest green")

joey.penup()
joey.begin_fill()
joey.penup()
joey.goto(0, -200)
joey.pendown()
joey.left(180)
joey.forward(321)
joey.left(90)
joey.forward(175)
joey.left(90)
joey.forward(630)
joey.left(90)
joey.forward(175)
joey.left(90)
joey.forward(321)
joey.end_fill()
joey.pendown()

turtle.bgcolor("Sky blue")


rico.color("red")
rico.begin_fill()
rico.goto(-100, -100)
rico.right(90)
rico.forward(100)
rico.left(90)
rico.forward(200)
rico.left(90)
rico.forward(100)
rico.goto(0, 0)
rico.goto(-100, -100)
rico.goto(100, -100)
rico.end_fill()


ethan.color("black")
ethan.begin_fill()
ethan.goto(-100, -100)
ethan.goto(100, -100)
ethan.goto(0, 0)
ethan.end_fill()
ethan.penup()
ethan.goto(-80, -140)
ethan.pendown()

ethan.begin_fill()
ethan.color("brown")


def square(sidelength):
    for i in range(4):
        ethan.forward(sidelength)
        ethan.right(90)


for i in range(1):
    square(20)
ethan.end_fill()

turtle.exitonclick()