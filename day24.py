import functools
import itertools
from operator import mul


with open("input24.txt") as f:
    package_weights = [int(x.strip()) for x in f.readlines()]

# package_sizes = [1, 2, 3, 4, 5, 7, 8, 9, 10, 11]
# print(package_sizes)

package_weights.sort()
accumulated = [x for x in itertools.accumulate(package_weights)]

def qe(x: int) -> int:
    res = 1
    for i in range(len(package_weights)):
        if x & (1<<i) != 0:
            res *= package_weights[i]
    return res

def find_possible_groups(count):
    total_size = sum(package_weights)
    compartment_size = total_size//count
    possible_groups = []
    working_set = []
    for i in range(len(package_weights), 0, -1):
        c = package_weights[i-1]
        tmp = []
        if accumulated[i-1]>compartment_size:
            tmp.append((1<<i-1, c))
        for p, v in working_set:
            if v+c == compartment_size:
                possible_groups.append(p | 1<<i-1)
            elif v+c < compartment_size:
                tmp.append((p | 1 << i-1, v+c))

            if v+accumulated[i-1]>=compartment_size:
                tmp.append((p,v))
        working_set = tmp


    possible_groups.sort(key=lambda a: (a.bit_count(), -a))
    return possible_groups

def find_solution_for(number_of_compartments):
    possible_groups = find_possible_groups(number_of_compartments)

    for z in itertools.combinations(possible_groups, number_of_compartments-1):
        if all([a&b==0 for a,b in itertools.combinations(z,2)]):
            return qe(z[0])

print(find_solution_for(3))
print(find_solution_for(4))