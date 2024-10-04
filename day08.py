
from itertools import accumulate


strings = [
    '""',
    '"abc"',
    '"aaa\\"aaa"',
    '"\\x27"'
]

def is_hex(string: str) -> bool:
    def _hex_char(c: str) -> bool:
        return c in '0123456789abcdefABCDEF'
    
    return any([_hex_char(x) for x in string])


def decode(string: str) -> tuple[int,int]:
    if string[0]!='"':
        raise f"Invalid string {string}"
    
    mem_size = 0
    i = 1
    while i<len(string) and string[i]!='"':
        if string[i] != '\\':
            mem_size += 1
            i += 1
        elif string[i+1] != 'x':
            mem_size += 1
            i += 2
        elif i<len(string)-4 and is_hex(string[i+2:i+4]):
            mem_size += 1
            i += 4
        else:
            mem_size += 1
            i += 2

    return len(string), mem_size


def encode(string: str) -> tuple[int, int]:
    e = [2 if x == '"' or x == '\\' else 1 for x in string]
    return sum(e) + 2, len(string)


with open("input08.txt") as f:
    strings = [x.strip() for x in f.readlines()]

tmp = [decode(x) for x in strings]
a = sum([a for (a,b) in tmp])
b = sum([b for (a,b) in tmp])
print(a-b)

tmp = [encode(x) for x in strings]
a = sum([a for (a,b) in tmp])
b = sum([b for (a,b) in tmp])
print(a-b)
