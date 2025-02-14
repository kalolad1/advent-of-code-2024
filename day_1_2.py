from collections import Counter

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
    b_count = Counter(b_nums)
    sim_score = 0

    for a in a_nums:
        if a in b_count:
            sim_score += a * b_count[a]
    return sim_score

if __name__ == "__main__":
    print(main())
