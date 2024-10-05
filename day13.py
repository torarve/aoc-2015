from itertools import permutations
import itertools
import re


lines = [
    "Alice would gain 54 happiness units by sitting next to Bob.",
    "Alice would lose 79 happiness units by sitting next to Carol.",
    "Alice would lose 2 happiness units by sitting next to David.",
    "Bob would gain 83 happiness units by sitting next to Alice.",
    "Bob would lose 7 happiness units by sitting next to Carol.",
    "Bob would lose 63 happiness units by sitting next to David.",
    "Carol would lose 62 happiness units by sitting next to Alice.",
    "Carol would gain 60 happiness units by sitting next to Bob.",
    "Carol would gain 55 happiness units by sitting next to David.",
    "David would gain 46 happiness units by sitting next to Alice.",
    "David would lose 7 happiness units by sitting next to Bob.",
    "David would gain 41 happiness units by sitting next to Carol."
]

with open("input13.txt") as f:
    lines = [x.strip() for x in f.readlines()]

nodes = set()
weights: dict[tuple[str,str], int] = {}

for line in lines:
    m = re.match(r"(\w+) would (gain|lose) (\d+) happiness units by sitting next to (\w+)", line)
    who, what, units, whom = m.groups()
    weigth = int(units) if what == 'gain' else -int(units)
    nodes.add(who)
    nodes.add(whom)
    weights[(who, whom)] = weigth

def calculate_happiness(nodes: set, weights: dict[tuple[str,str],int]):
    results: list[tuple[int,list[str]]] = []
    for permutation in permutations(nodes):
        total_gain = 0
        order = list(permutation)
        for a, b in itertools.pairwise(order + [order[0]]):
            total_gain += weights.get((a, b), 0)
            total_gain += weights.get((b, a), 0)
        results.append((total_gain, order))

    return list(sorted(results, key=lambda x: x[0]))

results = calculate_happiness(nodes, weights)
print(results[-1][0])

nodes.add("Me")
results = calculate_happiness(nodes, weights)
print(results[-1][0])
