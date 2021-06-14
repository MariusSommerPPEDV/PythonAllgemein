import turtle, time

i = 0

variable1 = turtle.Turtle()

while i < 300:
    variable1.tilt(i)
    variable1.forward(i)
    variable1.left(i)
    variable1.forward(i)
    variable1.right(i)
    variable1.back(i)
    variable1.circle(i)
    variable1.forward(i)
    i += 1

time.sleep(5)
asd = 21312
