
def read_input(file_path):
    grid = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            grid.append(list(line.strip()))
    return grid

TARGET_WORD = "XMAS"
def get_total_xmas(grid):
    n = len(grid)
    m = len(grid[0])

    total = 0
    for i in range(n):
        for j in range(m):
            total += get_from_single_point(i, j, grid)
    return total


def get_from_single_point(i, j, grid):
    total = 0
    n = len(grid)
    m = len(grid[0])
    cardinal_offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diagonal_offsets = [(-1, -1), (1, 1), (-1, 1), (1, -1)]

    offsets = cardinal_offsets + diagonal_offsets
    for dx, dy in offsets:
        is_match = True
        new_i = i
        new_j = j
        for k in range(len(TARGET_WORD)):
            if (new_i < 0) or (new_i >= n) or (new_j < 0) or (new_j >= m):
                is_match = False
                break

            if (grid[new_i][new_j] != TARGET_WORD[k]):
                is_match = False
                break
                
            new_i += dx
            new_j += dy
        
        if is_match:
            total += 1
    
    return total

def main():
    grid = read_input("input/day_4.txt")
    total_xmas = get_total_xmas(grid)

    
    return total_xmas

if __name__ == "__main__":
    print(main())
