from operator import and_, lshift, or_, rshift
from pprint import pprint


lines = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i""".split("\n")


def parse(line: str):
    value, name = line.split(" -> ")
    if value.isdigit():
        return name, int(value)
    elif value.startswith("NOT "):
        return name, (value[len("NOT "):],)
    elif " " in value:
        l, o, r = value.split(" ")
        match o:
            case "AND":
                return name, (l, and_, r)
            case "OR":
                return name, (l, or_, r)
            case "LSHIFT":
                return name, (l, lshift, int(r))
            case "RSHIFT":
                return name, (l, rshift, int(r))
    else:
        return name, value

    raise "Unable to parse"


def cache(m):
    m.cache = {}
    def wrapper(name, *args):
        if name not in m.cache:
            m.cache[name] = m(name, *args)
        return m.cache[name]
    
    def reset():
        m.cache = {}

    wrapper.reset = reset
    return wrapper

@cache
def calculate_value_for(name: str|int, wires: dict[tuple]) -> int:
    if type(name) == int:
        return name
    if name.isdigit():
        return int(name)
    value = wires[name]
    if type(value) == str:
        return calculate_value_for(value, wires)
    elif type(value) == int:
        return value
    elif len(value)==1:
        return ~calculate_value_for(value[0], wires) & 0xffff
    else:
        return value[1](calculate_value_for(value[0], wires), calculate_value_for(value[2], wires)) & 0xffff


wires = dict([parse(line) for line in lines])
wires = dict([parse(line.strip()) for line in open("input07.txt") if line !=""])

val = calculate_value_for("a", wires)
print(val)

wires["b"] = val
calculate_value_for.reset()
print(calculate_value_for("a", wires))