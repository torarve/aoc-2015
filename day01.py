
line = ")())())"
with open("input01.txt") as f:
    line = f.readline()

print(line)

ups = len([x for x in line if x == "("])
downs = len([x for x in line if x == ")"])
print(ups-downs)

i, pos = 0, 0
while pos != -1:
    pos += 1 if line[i]=="(" else -1
    i += 1

print(i)
