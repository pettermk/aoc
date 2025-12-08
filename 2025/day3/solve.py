from os import read


def read_input() -> list[str]:
    with open('input.txt') as f:
    # with open('test_input.txt') as f:
        lines = f.readlines()
    return lines


def part1():
    data = read_input()
    digits = []
    for line in data:
        print(line)
        digits.append([(int(x[1]), x[0]) for x in enumerate(line.rstrip())])
    print(digits)
    count = 0
    for dig in digits:
        m = max(dig, key=lambda x: x[0])
        if m[1] == len(dig) - 1:
            dig.pop()
            n = max(dig, key=lambda x: x[0])
            count = count + n[0] * 10 + m[0]
            print(f'Key is {n[0]}{m[0]}')
        else:
            n = max(dig[m[1] + 1:], key=lambda x: x[0])
            count = count + m[0] * 10 + n[0]
            print(f'Key is {m[0]}{n[0]}')
    print(count)


def process_line(line: str) -> int:
    n = len(line)
    digits = [int(x) for x in line]
    count = 0
    current_index = 0
    for end_index in range(11, -1, -1):
        max_value = max(digits[current_index:n - end_index])
        position = digits.index(max_value, current_index)
        current_index = position + 1
        count = count + max_value * pow(10, end_index)
    return count

def part2():
    data = read_input()
    count = 0
    for line in data:
        count = count + process_line(line.rstrip())
    print(count)

def solve_part2(lines):
    total = 0
    for line in lines:
        digits = sorted(line.strip(), reverse=True)
        # Take the twelve largest digits
        joltage = int(''.join(digits[:12]))
        total += joltage
    return total

def max_joltage_greedy(line, num_batteries):
    """
    Greedy: At each output position, choose the largest available digit
    that still leaves enough digits for the remaining positions.
    """
    n = len(line)
    result = []
    start = 0
    
    for i in range(num_batteries):
        # How many more digits do we need after this one?
        remaining_after = num_batteries - i - 1
        # Latest position we can choose from
        latest_pos = n - remaining_after - 1
        
        # Find the maximum digit in range [start, latest_pos]
        best_digit = line[start]
        best_pos = start
        for j in range(start, latest_pos + 1):
            if line[j] > best_digit:
                best_digit = line[j]
                best_pos = j
        
        result.append(best_digit)
        start = best_pos + 1
    
    return int(''.join(result))

if __name__ == '__main__':
    part2()
    print(solve_part2(read_input()))
    total2 = 0
    lines = read_input()
    for line in lines:
        joltage = max_joltage_greedy(line, 12)
        print(f"{line}: {joltage}")
        total2 += joltage
    print(f"Total: {total2}")

