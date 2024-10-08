with open("input20.txt") as f:
    wanted_number_of_presents = int(f.read())

def part1():
    upper_limit = wanted_number_of_presents//40
    presents_at_house = [0] * upper_limit
    elf = 1
    while elf < len(presents_at_house):
        pos = elf - 1
        while pos < len(presents_at_house):
            presents_at_house[pos] = presents_at_house[pos] + elf*10
            if presents_at_house[pos]>wanted_number_of_presents: break
            pos += elf
        elf += 1

    for i in range(0, len(presents_at_house)):
        if presents_at_house[i]>= wanted_number_of_presents:
            return i+1

print(part1())

def part2():
    upper_limit = wanted_number_of_presents//40
    presents_at_house = [0] * upper_limit
    elf = 1
    while elf < len(presents_at_house):
        pos = elf - 1
        while pos < len(presents_at_house) and pos<50*elf:
            presents_at_house[pos] = presents_at_house[pos] + elf*11
            if presents_at_house[pos]>wanted_number_of_presents: break
            pos += elf
        elf += 1

    for i in range(0, len(presents_at_house)):
        if presents_at_house[i]>= wanted_number_of_presents:
            return i+1

print(part2())