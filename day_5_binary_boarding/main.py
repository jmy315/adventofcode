"""
https://adventofcode.com/2020/day/5
"""

def highest(filename):
    max = 0
    pool = []
    with open(filename, 'r') as f:
        for line in f:
            result = 0
            ticket = line.strip()
            first = ticket[:7]
            second = ticket[7:]
            base = 512
            for i in range(10):
                if ticket[i] == 'B':
                    result += base
                if ticket[i] == 'R':
                    result += base
                base /= 2
            pool.append(result)
            if result > max:
                max = result
    sorted_pool = sorted(pool)
    temp = sorted_pool[0]
    my_ticket = 0
    for i in sorted_pool:
        if i > temp + 1:
            my_ticket = i - 1
            break
        temp = i
    return (max, my_ticket)
                
print(highest('input.txt'))
