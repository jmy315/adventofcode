"""
https://adventofcode.com/2020/day/10
"""

def count_jolts(adapters, start):
    new_starts = list()
    total = 0
    for i in adapters:
        if i - start <= 0:
            continue
        elif (i - start) <= 3:
            new_starts.append(i)

    if len(new_starts) == 0:
        return 1
    else:
        for j in new_starts:
            total += count_jolts(adapters, j)
    return total


def find_jolts2(filename):
    numbers = [0]
    with open(filename, 'r') as f:
        for line in f.readlines():
            numbers.append(int(line.strip()))
    numbers = sorted(numbers)
    groups = []
    temp = 0
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] == 3:
            groups.append(numbers[temp:i+1])
            temp = i+1
    groups.append(numbers[temp:])

    product = 1
    for group in groups:
        product *= count_jolts(group, group[0])
    return product

print(find_jolts2('test.txt'))
print(find_jolts2('sest.txt'))
print(find_jolts2('input.txt'))



def find_jolts(filename):
    numbers = set()
    with open(filename, 'r') as f:
        for line in f.readlines():
            numbers.add(int(line.strip()))
    c1 = 0
    c3 = 0
    for i in numbers:
        if i == 1:
            c1 += 1
        if i + 1 in numbers:
            c1 += 1
        elif i + 3 in numbers or i == max(numbers):
            c3 += 1
    return(c1*c3)

print(find_jolts('input.txt'))
