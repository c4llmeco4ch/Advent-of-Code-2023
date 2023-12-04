import re
import string

# P1

SYMBOLS = re.compile(r'[' +'|\\'.join(string.punctuation.replace('.', '')) + ']')

part_num_sum = 0

def diff_row(sym_x, line):
    global part_num_sum
    updated = line
    groups = re.finditer(r'\d+', line)
    for group in groups:
        s, e = group.span()
        if s >= sym_x - 1 and s <= sym_x + 1\
            or e >= sym_x and e <= sym_x + 2\
            or s < sym_x - 1 and e > sym_x:
            updated = updated.replace(group[0], '.' * (e - s))
            part_num_sum += int(group[0])
    return updated

def same_row(sym_x, line):
    global part_num_sum
    updated = line
    groups = re.finditer(r'\d+', line)
    print(f'Found {" | ".join(val[0] for val in groups)}')
    for group in groups:
        s, e = group.span()
        if s == sym_x + 1 or e == sym_x:
            updated = updated.replace(group[0], '.' * (e - s))
            part_num_sum += int(group[0])
    return updated


with open('input.txt') as f:
    lines = f.readlines()


for row, line in enumerate(lines):
    for match in re.finditer(SYMBOLS, line):
        pos = match.start()
        if row != 0:
            lines[row - 1] = diff_row(pos, lines[row - 1])
        lines[row] = same_row(pos, line)
        if row != len(lines) - 1:
            lines[row + 1] = diff_row(pos, lines[row + 1])

with open('output.txt', 'w') as output:
    output.write('\n'.join(lines))

print(f'P1: {part_num_sum}')
