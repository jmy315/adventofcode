"""
https://adventofcode.com/2020/day/7
"""

def find_colors(filename):
    bag_dict = dict()
    with open(filename, 'r') as f:
        for line in f.readlines():
            temp = line.strip().split(' contain ')
            first = ' '.join(temp[0].split(' ')[:-1])
            raw_bags = temp[1].split(', ')
            bags = []
            for i, bag in enumerate(raw_bags):
                if bag == 'no other bags.':
                    continue
                temp = ' '.join(bag.split(' ')[1:-1])
                bags.append(temp)
            if first not in bag_dict:
                bag_dict[first] = []
            bag_dict[first] += bags
    total = find_shiny_gold(bag_dict, {'shiny gold'}, set(), 0)
    return total

def find_shiny_gold(bags, wanted, known, total):
    if not wanted:
        return total
    temp = set()
    for key,value in bags.items():
        for v in value:
            for color in wanted:
                if v == color and key not in known:
                    total += 1
                    known.add(key)
                    temp.add(key)
    return find_shiny_gold(bags, temp, known, total)

print(find_colors('input.txt'))


def find_colors2(filename):
    bag_dict = dict()
    with open(filename, 'r') as f:
        for line in f.readlines():
            temp = line.strip().split(' contain ')
            first = ' '.join(temp[0].split(' ')[:-1])
            raw_bags = temp[1].split(', ')
            bags = dict()
            for i, bag in enumerate(raw_bags):
                if bag == 'no other bags.':
                    continue
                num = int(bag.split(' ')[0])
                temp = ' '.join(bag.split(' ')[1:-1])
                bags[temp] = num
            bag_dict[first] = bags
    total = find_shiny_gold2(bag_dict, {'shiny gold': 1})
    return total - 1

def find_shiny_gold2(bags, wanted):
    total = 0
    for key, value in wanted.items():
        total += value + value * find_shiny_gold2(bags, bags[key])
    return total

print(find_colors2('input.txt'))
