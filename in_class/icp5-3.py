# Iris Canavan, Section 3

ANGLE = 90
LENGTH = 200
MAX = 0
MIN = -100

inputPercent = 1
modifiedLength = 0

import turtle
turtle.showturtle()
turtle.pencolor("red")

for x in range(1,5):
	turtle.forward(LENGTH)
	turtle.right(ANGLE)

while inputPercent != 0:
	inputPercent = float(input("Enter negative percentage to decrease the rectangle (0 to stop) = "))
	if inputPercent <= MAX or inputPercent >= MIN:
		modifiedLength = (100 + inputPercent) / 100 * LENGTH

	for x in range(1,5):
		turtle.pencolor("black")
		if inputPercent == 0:
			turtle.penup()
		else:
			turtle.forward(modifiedLength)
			turtle.right(ANGLE)
print("----Loop exited, just ckick in turtle window to exit----")

turtle.hideturtle()
turtle.exitonclick()
