import sys


def get_char(row, col, x, y):
    if x == 1 or y == 1:
        return "B"

    if row == 0 and (col == 0 or col == x - 1):
        return "A"

    if row == y - 1 and (col == 0 or col == x - 1):
        return "C"

    if row == 0 or row == y - 1 or col == 0 or col == x - 1:
        return "B"

    return " "


def rush(x, y):
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return

    for row in range(y):
        line = ""
        for col in range(x):
            line += get_char(row, col, x, y)
        print(line)