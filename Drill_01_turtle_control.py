import turtle


def forward_control():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()


def back_control():
    turtle.setheading(-90)
    turtle.forward(50)
    turtle.stamp()

def right_control():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def left_control():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()
    turtle.stamp()


turtle.shape('turtle')
turtle.stamp()

turtle.onkey(forward_control, 'w')
turtle.onkey(back_control, 's')
turtle.onkey(right_control, 'd')
turtle.onkey(left_control, 'a')
turtle.onkey(restart, 'Escape')
turtle.listen()
