from dataclasses import dataclass


def path_points(path):
    allpos = dict()
    pos = (0, 0)
    steps = 0
    for move in path.split(','):
        direction, length = move[0], int(move[1:])
        # could be a hash map instead
        if direction == 'R':
            axis, increment = 0, 1
        elif direction == 'L':
            axis, increment = 0, -1
        elif direction == 'U':
            axis, increment = 1, 1
        elif direction == 'D':
            axis, increment = 1, -1
        else:
            raise ValueError(direction)

        for j in range(1, length+1):
            steps += 1
            pos = list(pos)
            pos[axis] += increment
            pos = tuple(pos)
            if pos in allpos:
                continue

            allpos[pos] = steps

    return allpos


def min_dist(path1, path2):
    common = set(path_points(p1).keys()) & set(path_points(p2).keys())
    return min(abs(pos[0]) + abs(pos[1]) for pos in common)


p1 = 'R8,U5,L5,D3'
p2 = 'U7,R6,D4,L4'
assert min_dist(p1, p2) == 6

p1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
p2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
assert min_dist(p1, p2) == 159

p1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
p2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
assert min_dist(p1, p2) == 135

# TASK 1

with open('day3_data.txt') as f:
    p1, p2 = next(f), next(f)

print(min_dist(p1, p2))

# TASK 2


def min_cost(path1, path2):
    pp1 = path_points(path1)
    pp2 = path_points(path2)
    common = set(pp1.keys()) & set(pp2.keys())
    return min(pp1[key] + pp2[key] for key in common)


p1 = 'R8,U5,L5,D3'
p2 = 'U7,R6,D4,L4'
assert min_cost(p1, p2) == 30

p1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
p2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
assert min_cost(p1, p2) == 610

p1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
p2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
assert min_cost(p1, p2) == 410

with open('day3_data.txt') as f:
    p1, p2 = next(f), next(f)

print(min_cost(p1, p2))
