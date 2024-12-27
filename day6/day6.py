with open("input.txt", "r") as f:
    data = f.readlines()
    data = [line.strip() for line in data]

#data is a grid there are objects # and the guard ^
#the guard moves forward (upward in this case) until it hits an object # 
#then it turns right and moves forward until it hits an object #
#continue this until the guard leaves the map, count the distinct positions 
directions = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0)
}

def turn_right(direction):
    if direction == "up":
        return "right"
    if direction == "right":
        return "down"
    if direction == "down":
        return "left"
    if direction == "left":
        return "up"
#create grid from data 
data = [list(line) for line in data]
#default direction
direction = "up"

#find the starting position of the guard
for y,line in enumerate(data):
    for x, char in enumerate(line):
        if char == "^":
            start = (x, y)
            break

#count every valid position of the guard 
valid_pos = set()
valid_pos.add(start)
#if the guard would hit an object # turn 90 degress right 

while True:
    x, y = start
    dx, dy = directions[direction]
    x += dx
    y += dy
    if x < 0 or x >= len(data[0]) or y < 0 or y >= len(data):
        break
    if data[y][x] == "#":
        direction = turn_right(direction)
        continue
    valid_pos.add((x, y))
    start = (x, y)

print(len(valid_pos))


# part 2
# based on the grid find points on which an obstacle can be placed so that the guard is stuck in a loop
# the guard is stuck in a loop if it always moves the same way
# find all possible loops 
# example input, guard ^, obstacle # 
# ....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...

def find_loops(data):

    def check_loop(grid):
        pos = None
        facing = None
        for ry in range(len(grid)):
            for rx in range(len(grid[0])):
                if grid[ry][rx] == "^":
                    pos = (rx, ry)
                    facing = "up"
                    break
            if pos:
                break
        
        visited = set()
        while True:
            state = (pos, facing)
            if state in visited:
                return True
            visited.add(state)
            dx, dy = directions[facing]
            nx, ny = pos[0] + dx, pos[1] + dy
            if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
                return False
            if grid[ny][nx] == "#":
                facing = turn_right(facing)
            else:
                pos = (nx, ny)

    loops = []
    for ry in range(len(data)):
        for rx in range(len(data[0])):
            if data[ry][rx] == ".":
                data[ry][rx] = "#"
                if check_loop(data):
                    loops.append((rx, ry))
                data[ry][rx] = "."
    return loops

print(len(find_loops(data)))