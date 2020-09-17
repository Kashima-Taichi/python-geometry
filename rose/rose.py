import turtle

# maximize speed
turtle.speed(10)

# rose geometry

for i in range(200):
    turtle.fd(i)
    turtle.left(360 / 4 + 10)

turtle.done()
