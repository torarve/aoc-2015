
from typing import Iterable


def read_file() -> str:
    with open("input03.txt") as f:
        return f.readline()

def visit(directions: str) -> int:
    x, y = 0, 0
    visited = set([(x,y)])
    for d in directions:
        match d:
            case "<": x -= 1
            case ">": x += 1
            case "^": y += 1
            case "v": y -= 1
        visited.add((x, y))

    return len(visited)

def visit2(directions: Iterable) -> set[int]:
    x, y = 0, 0
    visited = set([(x,y)])
    for d in directions:
        match d:
            case "<": x -= 1
            case ">": x += 1
            case "^": y += 1
            case "v": y -= 1
        visited.add((x, y))

    return visited


directions = read_file()
print(visit(directions))
print(len(visit2(directions[0::2]).union(visit2(directions[1::2]))))