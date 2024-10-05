from dataclasses import dataclass
import re


lines = [
    "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
    "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"
]

with open("input15.txt") as f:
    lines = [x.strip() for x in f.readlines()]

@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def __hash__(self):
        return self.name.__hash__()


class Recipe:
    def __init__(self, available_ingredients: list[Ingredient]):
        self.ingredients: dict[Ingredient, int] = dict([(x, 0) for x in available_ingredients])
    
    def set_amount_for(self, ingredient: Ingredient, amount: int):
        self.ingredients[ingredient] = amount

    def __str__(self):
        lines = [f"{amount} teaspoones of {ingredient.name}" for ingredient, amount in self.ingredients.items()]
        return f"Recipe({"\n".join(lines)})"

    @property
    def total_score(self):
        capacity = max(0, sum(ingredient.capacity*amount for ingredient, amount in self.ingredients.items()))
        durability = max(0, sum(ingredient.durability*amount for ingredient, amount in self.ingredients.items()))
        flavor = max(0, sum(ingredient.flavor*amount for ingredient, amount in self.ingredients.items()))
        texture = max(0, sum(ingredient.texture*amount for ingredient, amount in self.ingredients.items()))

        return capacity*durability*flavor*texture
    
    @property
    def calories(self):
        return max(0, sum(ingredient.calories*amount for ingredient, amount in self.ingredients.items()))


def best_total_score(ingredients: list[Ingredient], amount: int, recipe: Recipe, calories: int|None = None):
    if amount == 0:
        return 0
    if len(ingredients)==1:
        recipe.set_amount_for(ingredients[0], amount)
        if calories is None or calories==recipe.calories:
            return recipe.total_score
        return 0
        
    best_score = 0
    for i in range(1, amount+1):
        recipe.set_amount_for(ingredients[0], i)
        best_score = max(best_score, best_total_score(ingredients[1:], amount-i, recipe, calories))

    return best_score


ingredients: list[Ingredient] = []

for line in lines:
    m = re.match(r"(\w+): capacity (-?\w+), durability (-?\w+), flavor (-?\w+), texture (-?\w+), calories (-?\w+)", line)
    name, capacity, durability, flavor, texture, calories = m.groups()
    ingredients.append(Ingredient(name, int(capacity), int(durability), int(flavor), int(texture), int(calories)))


part1 = best_total_score(ingredients, 100, Recipe(ingredients))
print(part1)

part2 = best_total_score(ingredients, 100, Recipe(ingredients), 500)
print(part2)