
class Grid:
    def __init__(self, size: int = 6):
        self.size = size
        self._data: list[bool] = [False]*(size*size)

    def __getitem__(self, pos: tuple[int,int]) -> bool:
        x, y = pos
        return self._data[y*self.size + x]
    
    def __setitem__(self, pos: tuple[int,int], value: bool) -> bool:
        x, y = pos
        self._data[y*self.size + x] = value
        return value
    
    def __str__(self):
        result = []
        for y in range(0, self.size):
            line = "".join(["#" if x else "." for x in self._data[y*self.size:(y+1)*self.size]])
            result.append(line)
        return "\n".join(result)
    
    def neighbours(self, x: int, y: int) -> list[bool]:
        result = []
        if x>0: result.append(self[x-1, y])
        if x<self.size-1: result.append(self[x+1,y])

        min_x = max(0, x-1)
        max_x = min(self.size-1, x+1)
        if y>0: result.extend(self._data[(y-1)*self.size+min_x:(y-1)*self.size+max_x+1])
        if y<self.size-1: result.extend(self._data[(y+1)*self.size+min_x:(y+1)*self.size+max_x+1])

        return result
    
    def step(self) -> "Grid":
        result = Grid(self.size)
        for y in range(0, self.size):
            for x in range(0, self.size):
                ligths_on = len([x for x in self.neighbours(x,y) if x])
                if self[x,y]:
                    result[x,y] = True if ligths_on == 3 or ligths_on == 2 else False
                else:
                    result[x,y] = True if ligths_on == 3 else False
        return result
    
    def turn_corners_on(self):
        self[0,0] = True
        self[0, self.size-1] = True
        self[self.size-1, 0] = True
        self[self.size-1, self.size-1] = True

    def step2(self) -> "Grid":
        result = self.step()
        result.turn_corners_on()
        return result


with open("input18.txt") as f:
    lines = [x.strip() for x in f.readlines()]

def read_grid(lines: list[str]) -> Grid:
    grid = Grid(len(lines[0]))

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[x,y] = True if c == "#" else False
    return grid

grid = read_grid(lines)
for i in range(0,100):
    grid = grid.step()
print(f"For part 1 {len([x for x in grid._data if x])} lights are on.")

grid = read_grid(lines)
grid.turn_corners_on()
for i in range(0, 100):
    grid = grid.step2()
print(f"For part 2 {len([x for x in grid._data if x])} lights are on.")
