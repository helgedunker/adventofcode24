def read_input(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines()]

def solve(data, patterns, target_words):
    count = 0

    for y in range(len(data)):
        for x in range(len(data[0])):
            for pattern in patterns:
                try:
                    word = ''.join([data[y + dy][x + dx] for dx, dy in pattern])
                    if word in target_words:
                        count += 1
                except IndexError:
                    continue

    return count

# Define patterns for different slices
slices_part1 = [
    ((0, 0), (1, 0), (2, 0), (3, 0)), # horizontal
    ((0, 0), (0, 1), (0, 2), (0, 3)), # vertical
    ((0, 0), (1, 1), (2, 2), (3, 3)), # diagonal
    ((0, 3), (1, 2), (2, 1), (3, 0)), # other diagonal
]

slices_part2 = [
    ((0, 0), (1, 1), (2, 2), (0, 2), (2, 0)), # x-shape
]

# Read input data
input_data = read_input("input.txt")

# Solve for part 1 and part 2
part1_result = solve(input_data, slices_part1, {'XMAS', 'SAMX'})
part2_result = solve(input_data, slices_part2, {'MASMS', 'SAMSM', 'MASSM', 'SAMMS'})

# Print results
print(part1_result, part2_result)