import re

def read_input(file_path):
    with open(file_path, 'r') as file:
        input = "".join(file.readlines())
    return input

def parse_input(input):
    parsed_input = []

    stop_indexes = set([m.start() for m in re.finditer(r"don't\(\)", input)])
    start_indexes = set([m.start() for m in re.finditer(r"do\(\)", input)])

    enabled = True
    for i in range(len(input)):
        if enabled:
            parsed_input.append(input[i])
        
        if i in stop_indexes:
            enabled = False
        
        if i in start_indexes:
            enabled = True
    
    return "".join(parsed_input)


def main():
    # Read input
    input = parse_input(read_input("input/day_3.txt"))

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
