import re

with open("input.txt") as f:
    lines = f.readlines()

# Part 1

combo = []
for line in lines:
    digits = [val for val in line if val.isdigit()]
    ans = int(digits[0] + digits[-1])
    combo.append(ans)

print(f'P1: {sum(combo)}')

# Part 2

nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
combo2 = []

def find_digit(match):
    word = match.group(0)
    try:
        index = nums.index(word)
        return str(index + 1) + word[-1]
    except ValueError:
        return word

pattern = re.compile(r'|'.join(nums))
for line in lines:
    swapped = line
    while not (new_swap := pattern.sub(find_digit, swapped)) == swapped:
        swapped = new_swap
    digits = [val for val in swapped if val.isdigit()]
    ans = int(digits[0] + digits[-1])
    combo2.append(ans)

print(f'P2: {sum(combo2)}')
