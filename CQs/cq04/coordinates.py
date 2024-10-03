"""Challenge question 04: coordinates"""

__author__ = "730462791"


def get_coords(xs: str, ys: str) -> None:
    x: int = 0
    while x < len(xs):
        y: int = 0
        while y < len(ys):
            print(xs[x], ys[y])
            y += 1
        x += 1


get_coords("12", "34")
