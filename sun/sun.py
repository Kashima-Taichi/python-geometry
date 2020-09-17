import turtle

# maximize speed
turtle.speed(10)

# sun geometry

turtle.color('green', 'yellow')

turtle.begin_fill()

for i in range(90):
    turtle.fd(300)
    turtle.left(170)

turtle.end_fill()

turtle.done()
