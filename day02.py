import re

box = []
with open("input02.txt") as f:
    for line in f.readlines():
        box.append([int(x) for x in line.strip("\n").split("x")])

def calculate_required_paper(l: int, w: int, h: int) -> int:
    sides = [l*w, w*h, h*l]
    return sum(sides)*2 + min(sides)

def calculate_required_ribbon(l: int, w: int, h: int) -> int:
    a, b = tuple(sorted([l, w, h])[:2])
    return 2*a + 2*b + l*w*h

total = sum([calculate_required_paper(*box) for box in box])
# print(calculate_required_paper(2,3,4))
print(total)

total = sum([calculate_required_ribbon(*box) for box in box])
print(total)
