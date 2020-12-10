"""
https://adventofcode.com/2020/day/3

"""

def count_trees(filename, right, down):
    row = 0
    col = 0
    count = 0
    with open(filename, 'r') as f:
        lines =  f.readlines()
        length = len(lines[0].strip())
        while row < len(lines):
            line = lines[row].strip()
            if line[col] == '#':
                count += 1
            row += down
            col = (col + right) % length
    return count

a = count_trees('input.txt', 3, 1)
b = count_trees('input.txt', 1, 1)
c = count_trees('input.txt', 5, 1)
d = count_trees('input.txt', 7, 1)
e = count_trees('input.txt', 1, 2)

print(a)
print(a*b*c*d*e)
