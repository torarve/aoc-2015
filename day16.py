import operator
import re
from typing import Any

def parse_pair(s: str) -> tuple[str, int]:
    a, b = s.split(": ")
    return (a, int(b))


def matches(record: dict[str,int], filters: dict[str,int], comparators: dict[str,Any] = {}):
    return all([
        comparators.get(name, operator.eq)(value, filters[name])
        for name, value in record.items()])

filters = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

with open("input16.txt") as f:
    lines = [x.strip() for x in f.readlines()]

sues = {}
for line in lines:
    m = re.match(r"(Sue \d+):\s(.+)", line)
    id, tmp = m.groups()
    values = [parse_pair(x) for x in re.split(r",\s", tmp)]
    sues[id] = dict(values)

part1 = [sue for sue, record in sues.items() if matches(record, filters)][0]
print(part1)

comparators = {
    "cats": operator.gt,
    "trees": operator.gt,
    "pomeranians": operator.lt,
    "goldfish": operator.lt
}

part2 = [sue for sue, record in sues.items() if matches(record, filters, comparators)][0]
print(part2)
