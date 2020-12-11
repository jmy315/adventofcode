"""
https://adventofcode.com/2020/day/6
"""

def count_yes(filename):
    yes_list = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            temp_set = set()
            while line.strip():
                for i in line.strip():
                    temp_set.add(i)
                line = f.readline()
            yes_list.append(temp_set)
            line = f.readline()
    count = 0
    for i in yes_list:
        count += len(i)
    return count

print(count_yes('input.txt'))

def count_yes2(filename):
    yes_list = []
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            temp_set = set(line.strip())
            while line.strip():
                temp_set = temp_set.intersection(set(line.strip()))
                line = f.readline()
            yes_list.append(temp_set)
            line = f.readline()
    count = 0
    for i in yes_list:
        count += len(i)
    return count

print(count_yes2('input.txt'))



