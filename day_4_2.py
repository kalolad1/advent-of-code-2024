
def read_input(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            grid.append(list(line.strip()))
    return grid

def get_total_xmas(grid):
    n = len(grid)
    m = len(grid[0])

    total = 0
    for i in range(n):
        for j in range(m):
            if is_cross(i, j, grid):
                total += 1
    return total


def is_cross(i, j, grid):
    if grid[i][j] != "A":
        return False

    n = len(grid)
    m = len(grid[0])
    l_to_r_offsets = [(-1, -1), (1, 1)]
    r_to_l_offsets = [(-1, 1), (1, -1)]

    target_set = {"S", "M"}
    l_to_r_chars = set()
    for dx, dy in l_to_r_offsets:
        new_i = i + dx
        new_j = j + dy

        if (new_i < 0) or (new_i >= n) or (new_j < 0) or (new_j >= m):
            return False

        l_to_r_chars.add(grid[new_i][new_j])

    r_to_l_chars = set()
    for dx, dy in r_to_l_offsets:
        new_i = i + dx
        new_j = j + dy

        if (new_i < 0) or (new_i >= n) or (new_j < 0) or (new_j >= m):
            return False

        r_to_l_chars.add(grid[new_i][new_j])

    return l_to_r_chars == target_set and r_to_l_chars == target_set

def main():
    grid = read_input("input/day_4.txt")
    total_xmas = get_total_xmas(grid)

    
    return total_xmas

if __name__ == "__main__":
    print(main())
