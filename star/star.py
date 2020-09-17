import turtle

turtle.speed(10)

# star

turtle.color('red', 'yellow')

turtle.begin_fill()
for i in range(5 * 6):
    turtle.forward(100 + i * 10)
    turtle.right(360 / 5 * 2)
turtle.end_fill()

turtle.done()
