input = "111221"

with open("input10.txt") as f:
    input = f.readline().strip()

def round(input) -> str:
    result = ""
    current = input[0]
    count = 1
    i = 1
    while i<len(input):
        if current != input[i]:
            result += str(count)
            result += current
            count = 1
            current = input[i]
        else:
            count += 1

        i += 1

    result += str(count)
    result += current

    return result

result = input
for i in range(40):
    result = round(result)

print(len(result))

result = input
for i in range(50):
    result = round(result)

print(len(result))
