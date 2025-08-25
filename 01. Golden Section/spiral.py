import turtle
from math import sqrt


PHI: float = 2 / (sqrt(5) - 1)


def square(size: int) -> None:
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)


def golden_spiral(n: int) -> None:
    size: float = 10
    for _ in range(n):
        turtle.pencolor('blue')
        square(int(size))
        turtle.pencolor('red')
        turtle.circle(size, 90)
        size *= PHI


if __name__ == '__main__':
    # square(300)
    # turtle.circle(100, 45)
    turtle.hideturtle()
    turtle.pensize(3)
    turtle.speed('fastest')
    golden_spiral(9)
    turtle.done()
    print(PHI)
