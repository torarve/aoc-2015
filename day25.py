import math
import re


with open("input25.txt") as f:
    t = f.read()
    tr, tc = re.match("To continue, please consult the code grid in the manual.  Enter the code at row (\d+), column (\d+).", t).groups()
    r, c = int(tr), int(tc)

def next_code(code: int) -> int:
    return (code * 252533)%33554393

code = 20151125
idx = math.comb(c+1+r-1,2)-r+1

final_code = code
for i in range(idx-1):
    final_code = next_code(final_code)

print(final_code)
