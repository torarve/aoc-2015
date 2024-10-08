from dataclasses import dataclass
import itertools
import math
from pprint import pprint
import re


@dataclass
class Item:
    type: str
    name: str
    cost: int
    damage: int
    armor: int


@dataclass
class Stats:
    hitpoints: int
    damage: int
    armor: int


weapons = [
    Item("weapon", "Dagger", 8, 4, 0),
    Item("weapon", "Shortsword", 10, 5, 0),
    Item("weapon", "Warhammer", 25, 6, 0),
    Item("weapon", "Longsword", 40, 7, 0),
    Item("weapon", "Greataxe", 74, 8, 0)
]

armor = [
    None,
    Item("armor", "Leather", 13, 0, 1),
    Item("armor", "Chainmail", 31, 0, 2),
    Item("armor", "Splintmail", 53, 0, 3),
    Item("armor", "Bandedmail", 75, 0, 4),
    Item("armor", "Platemail", 102, 0, 5),
]

rings = [
    None,
    Item("ring", "Damage +1", 25, 1, 0),
    Item("ring", "Damage +2", 50, 2, 0),
    Item("ring", "Damage +3", 100, 3, 0),
    Item("ring", "Defense +1", 20, 0, 1),
    Item("ring", "Defense +2", 40, 0, 2),
    Item("ring", "Defense +3", 80, 0, 3),
]

def reduce(items: tuple[Item]) -> tuple[int, Stats]:
    cost = sum([x.cost for x in items if x is not None])
    damage = sum([x.damage for x in items if x is not None])
    armor = sum([x.armor for x in items if x is not None])
    return (cost, Stats(100, damage, armor))

def will_play_win(player: Stats, boss: Stats) -> bool:
    damage_inflicted_by_player = max(1, player.damage-boss.armor)
    damage_inflicted_by_boss = max(1, boss.damage-player.armor)
    player_kills_boss_after = boss.hitpoints//damage_inflicted_by_player
    if boss.hitpoints%damage_inflicted_by_player > 0:
        player_kills_boss_after += 1
    boss_kills_player_after = player.hitpoints//damage_inflicted_by_boss
    if player.hitpoints%damage_inflicted_by_boss > 0: 
        boss_kills_player_after += 1
    return player_kills_boss_after<=boss_kills_player_after

boss = Stats(0,0,0)
with open("input21.txt") as f:
    for line in f.readlines():
        m = re.match(r"(.+): (\d+)", line)
        name, value = m.groups()
        if name == "Hit Points":
            boss.hitpoints = int(value)
        elif name == "Damage":
            boss.damage = int(value)
        elif name == "Armor":
            boss.armor = int(value)

possibilities = [reduce(x) for x in itertools.product(weapons, armor, rings, rings) if x[-1] is None or x[-2] is None or x[-1]!=x[-2]]

winning_possibilities = [x for x,y in possibilities if will_play_win(y, boss)]
print(min(winning_possibilities))

loosing_possibilities = [x for x,y in possibilities if will_play_win(y, boss) == False]
print(max(loosing_possibilities))

