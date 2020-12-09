"""
https://adventofcode.com/2020/day/2
ideas:
    1) read each line and check for number of times range and the character
    2) check if the password meets the requirement by counting appearances of that char

complexity:
    O(N) where N is number of passwords
"""

import sys

def valid_password(filename):
    valid_counts = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            words = line.split()
            numbers = words[0].split('-')
            low = int(numbers[0])
            high = int(numbers[1])
            character = words[1][0]
            password = words[2]
            count = 0
            for c in password:
                if c == character:
                    count += 1
            if count <= high and count >= low:
                valid_counts += 1
    return valid_counts

print(valid_password(sys.argv[1]))


def valid_password2(filename):
    valid_counts = 0
    with open(filename, 'r') as f:
        for line in f.readlines():
            words = line.split()
            numbers = words[0].split('-')
            low = int(numbers[0]) - 1
            high = int(numbers[1]) - 1
            character = words[1][0]
            password = words[2]
            if password[low] == character and password[high] != character:
                valid_counts += 1
            if password[low] != character and password[high] == character:
                valid_counts += 1

    return valid_counts


print(valid_password2(sys.argv[1]))
