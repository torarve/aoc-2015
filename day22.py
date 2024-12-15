
from dataclasses import dataclass
import re


@dataclass
class GameState:
    hitpoints: int
    mana: int
    shield: int
    poison: int
    recharge: int
    boss: int
    turn: int

    def __hash__(self):
        return hash(f"{self.hitpoints}-{self.mana}-{self.shield}-{self.poison}-{self.recharge}-{self.boss}-{self.turn}")
    
    def has_won(self):
        return self.boss <= 0
    
    def clone(self):
        return GameState(self.hitpoints, self.mana, self.shield, self.poison, self.recharge, self.boss, self.turn)
    
    def active_effects(self) -> list[str]:
        result = []
        if self.shield > 0: result.append("Shield")
        if self.poison > 0: result.append("Poison")
        if self.recharge > 0: result.append("Recharge")
        return result

    def apply_effects(self) -> int:
        shield = 0
        if self.shield>0:
            shield = 7
            self.shield -= 1
   
        if self.poison>0:
            self.boss -= 3
            self.poison -= 1

        if self.recharge>0:
            self.mana += 101
            self.recharge -= 1

        return shield
   

with open("input22.txt") as f:
    for line in f.readlines():
        m = re.match(r"(.+): (\d+)", line)
        name, value = m.groups()
        if name == "Hit Points":
            boss_hitpoints = int(value)
        elif name == "Damage":
            boss_damage = int(value)


spell_costs = {
    "Magic Missile": 53,
    "Drain": 73,
    "Shield": 113,
    "Poison": 173,
    "Recharge": 229,
}

cache: dict[int, int] = {}

def search_for_min_mana(state: GameState, damage: int, part2: bool = False):
    if hash(state) in cache.keys():
        return cache.get(hash(state))

    temp = state.clone()
    if part2 and state.turn == 0:
        temp.hitpoints -= 1
        if temp.hitpoints<=0:
            return None
            
    shield = temp.apply_effects()
    if temp.has_won():
        # No mana used
        cache[hash(state)] = 0
        return 0
    
    if state.turn == 0:
        active_effects = temp.active_effects()
        possible_spells = [spell for spell, cost in spell_costs.items() if cost<=temp.mana and spell not in active_effects]
        if len(possible_spells) == 0:
            cache[hash(state)] = None
            return None
        
        min_used_mana = None
        for spell in possible_spells:
            next_state = temp.clone()
            next_state.mana -= spell_costs[spell]
            if spell == "Magic Missile":
                next_state.boss -= 4
            elif spell == "Drain":
                next_state.hitpoints += 2
                next_state.boss -= 2
            elif spell == "Shield":
                next_state.shield = 6
            elif spell == "Poison":
                next_state.poison = 6
            elif spell == "Recharge":
                next_state.recharge = 5

            if next_state.boss > 0:
                next_state.turn = 1
                search_result = search_for_min_mana(next_state, damage, part2)
                if search_result is None:
                    used_mana = None
                else:
                    used_mana = search_result + spell_costs[spell]
            else:
                used_mana = spell_costs[spell]
            if used_mana is not None:
                if min_used_mana is None or used_mana < min_used_mana:
                    min_used_mana = used_mana
        
        cache[hash(state)] = min_used_mana
        return min_used_mana
    else:
        # Boss
        temp.hitpoints -= (damage-shield)
        temp.turn = 0
        if temp.hitpoints<=0:
            cache[hash(state)] = None
            return None
        result = search_for_min_mana(temp, damage, part2)
        cache[hash(state)] = result
        return result


initial_state = GameState(50, 500, 0, 0, 0, boss_hitpoints, turn=0)

result = search_for_min_mana(initial_state, boss_damage)
print(result)

cache.clear()
initial_state = GameState(50, 500, 0, 0, 0, boss_hitpoints, turn=0)
result = search_for_min_mana(initial_state, boss_damage, True)
print(result)
