import turtle, time

i = 0

variable1 = turtle.Turtle()

while i < 1000:
    i /= 2
    variable1.tilt(i)
    variable1.forward(i + 10)
    variable1.left(i + 5)
    variable1.forward(i + 10)
    variable1.right(i + 20)
    variable1.back(i + 50)
    variable1.circle(i + 2)
    variable1.forward(i + 10)
    i += 10

time.sleep(5)
asd = 21312

