import itertools

container_sizes = [20, 15, 10, 5, 5]
target_amount = 25

with open("input17.txt") as f:
    container_sizes = [int(x.strip()) for x in f.readlines()]

target_amount = 150

container_combinations = [
    x
    for i in range(1, len(container_sizes)) 
    for x in itertools.combinations(container_sizes, i)
    if sum(x)==target_amount]

print(len(container_combinations))

minimum_number_of_containers = min(len(x) for x in container_combinations)
print(len([x for x in container_combinations if len(x) == minimum_number_of_containers]))