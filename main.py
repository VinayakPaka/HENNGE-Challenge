import sys
from functools import reduce


def power_of_four(x):
    return x ** 4


def sum_negatives_and_zero(numbers):
    filtered = list(filter(lambda y: y <= 0, numbers))
    return reduce(lambda acc, y: acc + power_of_four(y), filtered, 0)


def read_line():
    line = sys.stdin.readline()
    if not line:
        return ""
    stripped = line.strip()
    if not stripped:
        return read_line()
    return stripped

def process_case():
    x_line = read_line()
    if not x_line:
        return None
    x = int(x_line)
    nums_line = read_line()
    nums_str = nums_line.split()
    if len(nums_str) != x:
        return -1
    numbers = list(map(int, nums_str))
    return sum_negatives_and_zero(numbers)

def process_all(n, results):
    if n == 0:
        return results
    res = process_case()
    if res is None:
        return results
    return process_all(n - 1, results + [res])

def main():
    n_line = read_line()
    if not n_line:
        return
    n = int(n_line)
    results = process_all(n, [])
    print('\n'.join(map(str, results)))


if __name__ == "__main__":
    main()