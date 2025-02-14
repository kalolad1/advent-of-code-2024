import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        input = "".join(file.readlines())
    return input

def main():
    # Read input
    input = read_input("input/day_3.txt")

    # Use regex to parse out all mul(X,Y)
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, input)

    # Multiple each other and store in counter
    total = 0
    for a, b in matches:
        total += int(a) * int(b)
    
    return total

if __name__ == "__main__":
    print(main())
