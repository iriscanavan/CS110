# Iris Canavan, Section 3

import turtle
turtle.showturtle()

radius = 50
decrement = 10

#move
turtle.penup()
turtle.goto(0, radius)
turtle.pendown()

#draw dot
turtle.dot()

#move
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

#draw circle
turtle.circle(radius)

#move
turtle.penup()
turtle.goto(radius * 2 - decrement, 0)
turtle.pendown()

#draw circle
turtle.circle(radius)

#move
turtle.penup()
turtle.goto(-radius * 2 + decrement, 0)
turtle.pendown()

#draw circle
turtle.circle(radius)

turtle.done()
