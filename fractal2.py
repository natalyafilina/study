import turtle as tl

sc = tl.Screen()
tl.speed(0)
tl.hideturtle()
tl.pensize(2)


def triangle(length):
    for _ in range(3):
        tl.forward(length)
        tl.left(120)


def fract(length, red, green, blue):
    if length < 10:
        ...
    else:
        tl.begin_fill()
        tl.fillcolor(red, green, blue)
        triangle(length)
        tl.end_fill()
        tl.left(10)
        if red <= 3:
            red = 255
        if green == 255:
            green = 237
        if blue == 72:
            blue = 0
        fract(length - 5, red - 14, green + 1, blue + 4)

tl.delay(1)
tl.pencolor("red")
tl.colormode(255)
fract(900, 255, 237, 0)
tl.tracer(0, 0)
tl.done()

