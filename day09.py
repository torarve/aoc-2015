from itertools import permutations
import itertools
import re

lines = [
    "London to Dublin = 464",
    "London to Belfast = 518",
    "Dublin to Belfast = 141",
]

with open("input09.txt") as f:
    lines = [x.strip() for x in f.readlines()]

nodes = set()
distance = {}

for line in lines:
    m = re.match(r"(\w+)\s+to\s+(\w+) = (\d+)", line)
    f, t, d = m.groups()
    nodes.add(f)
    nodes.add(t)
    distance[f"{f}-{t}"] = int(d)
    distance[f"{t}-{f}"] = int(d)

all_distances = []
for p in [x for x in permutations(nodes)]:
    total_distance = sum([distance[f"{a}-{b}"] for (a,b) in itertools.pairwise(p)])
    all_distances.append((p, total_distance))

results = [x for x in sorted(all_distances, key=lambda x: x[1])]
result = results[0]

print(result[1])

result = results[-1]
print(result[1])
