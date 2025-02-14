
def read_input(file_path):
    with open(file_path, 'r') as file:
        a_nums = []
        b_nums = []
        for line in file.readlines():
            a, b = line.split()
            a_nums.append(int(a))
            b_nums.append(int(b))
    return (a_nums, b_nums)


def main():
    a_nums, b_nums = read_input("input/day_1.txt")
    a_nums.sort()
    b_nums.sort()

    n = len(a_nums)
    diff = 0
    for i in range(n):
        diff += abs(a_nums[i] - b_nums[i])
    return diff

if __name__ == "__main__":
    print(main())
