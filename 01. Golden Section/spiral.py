import turtle


def square(size: int) -> None:
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)


if __name__ == '__main__':
    square(300)
    turtle.done()
