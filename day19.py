import re


lines = [
    "e => H",
    "e => O",
    "H => HO",
    "H => OH",
    "O => HH",
    "",
    "HOH"
]

with open("input19.txt") as f:
    lines = [x.strip() for x in f.readlines()]

rules: dict[str, list[str]] = {}
reversed_rules: dict[str,str] = {}
for line in lines:
    if line == "": break
    m = re.match(r"(\w+) => (\w+)", line)
    a, b = m.groups()
    current_rules = rules.get(a, [])
    current_rules.append(b)
    rules[a] = current_rules
    reversed_rules[b] = a

molecule = lines[-1]

def calculate_next(input: str, rules: dict[str,list[str]]):
    parts = re.findall(r"([A-Z][a-z]?|e)", input)
    for pos, part in enumerate(parts):
        for rule in rules.get(part, []):
            yield "".join(parts[0:pos] + [rule] + parts[pos+1:])


results = [x for x in calculate_next(molecule, rules)]
distinct_molecules = set(results)
print(f"The number of distinct molecules that can be created from {molecule} are {len(distinct_molecules)}.")


reverse_molecule = molecule[::-1]
reversed_rules = dict([
    (value[::-1], key[::-1]) 
    for key,values in rules.items()
    for value in values])

expr = re.compile("|".join([x for x in reversed_rules.keys()]))
count = 0
while reverse_molecule != "e":
    reverse_molecule = expr.sub(lambda m: reversed_rules[m.group()], reverse_molecule, 1)
    count += 1

print(f"The number of steps to produce {molecule} is {count}.")
