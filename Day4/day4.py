with open('input.txt') as f:
    lines = f.readlines()

# P1

total = 0

for line in lines:
    games = line[line.find(':') + 2:]
    win, pick = games.split('|')
    win_set = set(win.strip().split())
    card_val = len([1 for p in pick.strip().split() if p in win_set])
    total += int(2 ** (card_val - 1))

print(f'P1: {total}')



# P2

copies = [1] * len(lines)

for card_num, line in enumerate(lines):
    games = line[line.find(':') + 2:]
    win, pick = games.split('|')
    win_set = set(win.strip().split())
    card_val = len([1 for p in pick.strip().split() if p in win_set])
    for pos in range(card_val):
        copies[(card_num + 1) + pos] += copies[card_num]
    
print(f'P2: {sum(copies)}')