from functools import lru_cache
import sys
sys.setrecursionlimit(2300)

def part1(walls: dict[tuple[int], int]) -> None:
    for key in walls.keys():
        neighbours = [(key[0], key[1], key[2]-1), (key[0], key[1], key[2]+1), (key[0], key[1]-1, key[2]), (key[0], key[1]+1, key[2]), (key[0]-1, key[1], key[2]), (key[0]+1, key[1], key[2])]
        for neighbour in neighbours:
            if neighbour in walls:
                walls[neighbour] -= 1
    return sum(walls.values())
    

@lru_cache(maxsize=None)
def check_if_inside(key: tuple[int], cubes: tuple[tuple[int]], maxX: int, maxY: int, maxZ: int):
    if key[0] > maxX or key[1] > maxY or key[2] > maxZ:
        return False
    if min(key) < 0:
        return False
    global visited
    neighbours = [(key[0], key[1], key[2]-1), (key[0], key[1], key[2]+1), (key[0], key[1]-1, key[2]), (key[0], key[1]+1, key[2]), (key[0]-1, key[1], key[2]), (key[0]+1, key[1], key[2])]
    for neighbour in neighbours:
        if neighbour not in cubes and neighbour not in visited:
            visited = visited + (neighbour,)
            if not check_if_inside(neighbour, cubes + (neighbour,), maxX, maxY, maxZ):
                return False
    return True


def part2(walls: dict[tuple[int], int], maxX: int, maxY: int, maxZ: int, amount: int) -> None:
    global visited,i
    cubes = tuple(walls.keys())
    inside = ()
    not_cube = ()
    for x in range(maxX):
        for y in range(maxY):
            for z in range(maxZ):
                if (x,y,z) not in cubes:
                    not_cube += ((x,y,z),)
    for cube in not_cube:
        if cube not in cubes:
            visited = (cube,)
            if check_if_inside(cube, cubes, maxX, maxY, maxZ):
                inside += visited
                cubes += visited
    for key in inside:
        neighbours = [(key[0], key[1], key[2]-1), (key[0], key[1], key[2]+1), (key[0], key[1]-1, key[2]), (key[0], key[1]+1, key[2]), (key[0]-1, key[1], key[2]), (key[0]+1, key[1], key[2])]
        for neighbour in neighbours:
            if neighbour in walls:
                amount -= 1
    print(amount)



with open("input.txt", "r") as file:
    lines = list(map(str.strip, file.readlines()))
    walls = {}
    maxX = 0
    maxY = 0
    maxZ = 0
    for line in lines:
        cube = tuple(map(int, line.split(",")))
        walls[cube] = 6
        maxX = max(cube[0], maxX)
        maxY = max(cube[1], maxY)
        maxZ = max(cube[2], maxZ)
    amount = part1(walls)
    print(amount)
    part2(walls, maxX, maxY, maxZ, amount)
