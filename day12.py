import json
from typing import Any
from collections.abc import Callable

def part1(part: Any) -> int:
    if isinstance(part, list):
        return sum([part1(x) for x in part])
    elif isinstance(part, dict):
        return sum([part1(x) for x in part.values()])
    elif isinstance(part, int):
        return part
    else:
        return 0


def part2(part: Any) -> int:
    if isinstance(part, list):
        return sum([part2(x) for x in part])
    elif isinstance(part, dict):
        if "red" not in part.values():
            return sum([part2(x) for x in part.values()])
        return 0
    elif isinstance(part, int):
        return part
    else:
        return 0
        

input = ""
with open("input12.txt") as f:
    input = f.readline().strip()

json_doc = json.loads(input)
print(part1(json_doc))
print(part2(json_doc))
