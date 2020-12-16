"""
https://adventofcode.com/2020/day/8
"""

def kill_loop(filename):
    instructions = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            words = line.split()
            op = words[0]
            jump = int(words[1])
            instructions.append((op,jump))
    i = 0
    while i < len(instructions):
        if instructions[i][0] == 'nop':
            loop, re = is_loop(instructions[:i] + [('jmp', instructions[i][1])] + instructions[i+1:])
            if not loop:
                return re
        elif instructions[i][0] == 'jmp':
            loop, re = is_loop(instructions[:i] + [('nop', instructions[i][1])] + instructions[i+1:])
            if not loop:
                return re
        i += 1
    return


def is_loop(ins):
    re = 0
    visited = set()
    i = 0
    while True:
        if i >= len(ins):
            return False, re
        if i not in visited:
            visited.add(i)
        else:
            return True, 0
        if ins[i][0] == 'nop':
            i += 1
        elif ins[i][0] == 'acc':
            re += ins[i][1]
            i += 1
        else:
            i += ins[i][1]

print(kill_loop('input.txt'))


def find_loop(filename):
    instructions = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            words = line.split()
            op = words[0]
            jump = int(words[1])
            instructions.append((op,jump))
    re = 0
    visited = set()
    i = 0
    while True:
        if i in visited:
            return re
        else:
            visited.add(i)
        if instructions[i][0] == 'nop':
            i += 1
        elif instructions[i][0] == 'acc':
            re += instructions[i][1]
            i += 1
        else:
            i += instructions[i][1]



print(find_loop('input.txt'))
