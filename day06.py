
import re


def lines():
    with open("input06.txt") as f:
        for line in f:
            yield line

grid = [False] * 1000 * 1000

e = r"(toggle|turn (?:on|off)) (\d+),(\d+) through (\d+),(\d+)"
regexp = re.compile(e)
for line in lines():
    cmd, x1, y1, x2, y2 = regexp.match(line).groups()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    match cmd:
        case "toggle":
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y*1000+x] = not grid[y*1000+x]
        case "turn on":
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y*1000+x] = True
        case "turn off":
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y*1000+x] = False

print(len([x for x in grid if x]))

grid = [0] * 1000 * 1000

e = r"(toggle|turn (?:on|off)) (\d+),(\d+) through (\d+),(\d+)"
regexp = re.compile(e)
for line in lines():
    cmd, x1, y1, x2, y2 = regexp.match(line).groups()
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    match cmd:
        case "toggle":
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y*1000+x] += 2
        case "turn on":
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y*1000+x] += 1
        case "turn off":
            for y in range(y1, y2+1):
                for x in range(x1, x2+1):
                    grid[y*1000+x] = max(0, grid[y*1000+x]-1)

print(sum(grid))