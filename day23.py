from dataclasses import dataclass
import re


with open("input23.txt") as f:
    input = [x.strip() for x in f.readlines()]


def parse_instruction(line: str) -> tuple[str,str,int]:
    m = re.match(r"(hlf|tpl|inc|jmp|jie|jio) (a|b|(?:(?:-|\+)\d+))(?:, ((?:-|\+)\d+))?", line)
    return m.groups()

instructions = [parse_instruction(l) for l in input]
def run_program(program, a, b):
    registers = { "a": a, "b": b }
    ip = 0
    while ip < len(input):
        i, r1, r2 = program[ip]
        if i == "hlf":
            registers[r1] = registers[r1] // 2
        elif i == "tpl":
            registers[r1] = 3*registers[r1]
        elif i == "inc":
            registers[r1] = registers[r1] + 1
        elif i == "jmp":
            ip += int(r1)
            continue
        elif i == "jie" and registers[r1]%2==0:
            ip += int(r2)
            continue
        elif i == "jio" and registers[r1]==1:
            ip += int(r2)
            continue
        ip += 1
    return registers


print(run_program(instructions, 0, 0)["b"])

print(run_program(instructions, 1, 0)["b"])
