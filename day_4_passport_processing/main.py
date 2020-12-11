"""
https://adventofcode.com/2020/day/4
"""

def count_passports2(filename):
    passports = []
    count = 0
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            temp = ''
            while line.strip():
                temp += line
                line = f.readline()
            line = f.readline()
            passports.append(temp)
    for p in passports:
        fields = set()
        words = p.split()
        valid = True
        for word in words:
            fv = word.split(':')
            fields.add(fv[0])
            if fv[0] == 'byr' and (len(fv[1]) != 4 or int(fv[1]) < 1920 or int(fv[1]) > 2002):
                valid = False
            elif fv[0] == 'iyr' and (len(fv[1]) != 4 or int(fv[1]) < 2010 or int(fv[1]) > 2020):
                valid = False
            elif fv[0] == 'eyr' and (len(fv[1]) != 4 or int(fv[1]) < 2020 or int(fv[1]) > 2030): 
                valid = False
            elif fv[0] == 'hgt':
                if fv[1][-2:] == 'cm':
                    if int(fv[1][:-2]) < 150 or int(fv[1][:-2]) > 193:
                        valid = False
                elif fv[1][-2:] == 'in':
                    if int(fv[1][:-2]) < 59 or int(fv[1][:-2]) > 76:
                        valid = False
                else:
                    valid = False
            elif fv[0] == 'hcl':
                if fv[1][0] == '#':
                    for i in fv[1][1:]:
                        if not i.isdigit() and not i.isalpha():
                            valid = False
                    if len(fv[1]) != 7:
                        valid = False
                else:
                    valid = False
            elif fv[0] == 'ecl':
                if fv[1] not in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
                    valid = False
            elif fv[0] == 'pid' and (len(fv[1]) != 9 or not fv[1].isdigit()):
                valid = False
        if required_fields.issubset(fields) and valid:
            count += 1
    return count

print(count_passports2('input.txt'))


def count_passports(filename):
    passports = []
    count = 0
    required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            temp = ''
            while line.strip():
                temp += line
                line = f.readline()
            line = f.readline()
            passports.append(temp)
    for p in passports:
        fields = set()
        words = p.split()
        for word in words:
            fv = word.split(':')
            fields.add(fv[0])
        if required_fields.issubset(fields):
            count += 1
    return count

print(count_passports('input.txt'))
