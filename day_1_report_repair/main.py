"""
https://adventofcode.com/2020/day/1
ideas:
    1) use a set to store individual seen number
    2) whenever see a new num, check if can find sum - num inside the set
    3) if so, print out the product, if not, add it to the set

complexity:
    O(n) where n is number of integers given
"""

import sys

def two_sum(filename):
    knowns = set()
    with open(filename, 'r') as f:
        for line in f.readlines():
            num = int(line.strip())
            if (2020 - num) in knowns:
                return num * (2020 - num)
            else:
                knowns.add(num)

print(two_sum(sys.argv[1]))


def three_sum(filename):
    numbers = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            numbers.append(int(line.strip()))
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                if 2020 == numbers[i] + numbers[j] + numbers[k]:
                    return numbers[i] * numbers[j] * numbers[k]

print(three_sum(sys.argv[1]))


