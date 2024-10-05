from collections.abc import Iterable
from dataclasses import dataclass
import re


lines = [
    "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
    "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
]
time_limit = 1000

with open("input14.txt") as f:
    lines = [x.strip() for x in f.readlines()]
time_limit = 2503


@dataclass
class Reindeer:
    name: str
    speed: int
    flight_time: int
    rest_time: int

    def distance_after(self, seconds: int) -> int:
        block_size = self.flight_time + self.rest_time
        blocks = seconds // block_size
        remaining = seconds % block_size
        flying_time = blocks*self.flight_time + min(remaining, self.flight_time)

        return flying_time * self.speed


reindeer: list[Reindeer] = []
for line in lines:
    m = re.match(r"(\w+) can fly (\d+) km/s for (\d+) seconds, but then must rest for (\d+) seconds.", line)
    who, speed, flight_time, rest_time = m.groups()
    reindeer.append(Reindeer(who, int(speed), int(flight_time), int(rest_time)))

def leaders_after(seconds: int) -> Iterable[tuple[str,int]]:
    results = sorted([(x.name, x.distance_after(seconds)) for x in reindeer], key=lambda t: t[1], reverse=True)
    max_distance = results[0][1]
    current = 0
    while current < len(results) and results[current][1] == max_distance:
        yield results[current]
        current += 1
    
name, distance = next(leaders_after(time_limit))
print(f"Winner is {name} at {distance} km.")

points: dict[str,int] = dict([(x.name, 0) for x in reindeer])
for current_time in range(1, time_limit+1):
    leaders = leaders_after(current_time)
    for leader, _ in leaders:
        points[leader] = points[leader] + 1

name, score = sorted(points.items(), key=lambda x: x[1], reverse=True)[0]
print(f"Winner is {name} with {score} points.")