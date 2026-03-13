import sys
from functools import reduce


def power_of_four(x):
    return x ** 4


def sum_negatives_and_zero(numbers):
    filtered = list(filter(lambda y: y <= 0, numbers))
    return reduce(lambda acc, y: acc + power_of_four(y), filtered, 0)


def process_case(lines, index):
    x = int(lines[index])
    nums_line = lines[index + 1].split()
    if len(nums_line) != x:
        return -1, index + 2
    numbers = list(map(int, nums_line))
    result = sum_negatives_and_zero(numbers)
    return result, index + 2


def process_all(lines, n, index, results):
    if n == 0:
        return results
    result, next_index = process_case(lines, index)
    return process_all(lines, n - 1, next_index, results + [result])


def main():
    data = sys.stdin.read().split('\n')
    lines = list(filter(lambda l: l.strip() != '', data))
    n = int(lines[0])
    results = process_all(lines, n, 1, [])
    print('\n'.join(map(str, results)))


if __name__ == "__main__":
    main()