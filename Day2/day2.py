with open("input.txt") as f:
    lines = f.readlines()

# P1

bag = {'red': 12, 'green': 13, 'blue':14}
possible_ids = []
for line in lines:
    game_id, rounds = line.split(':')
    valid = True
    for result in rounds.split(';'):
        pulls = result.split(',')
        for p in pulls:
            num, color = p.split()
            if int(num) > bag[color]:
                valid = False
                break
    if valid:
        possible_ids.append(int(game_id.split()[-1]))

print(f'P1: {sum(possible_ids)}')

# P2
from functools import reduce

bags = []
for line in lines:
    rounds = line.split(':')[-1].lstrip()
    bag = {'red': 0, 'green': 0, 'blue': 0}
    for game in rounds.split(';'):
        pulls = game.split(',')
        for pull in pulls:
            num, color = pull.split()
            bag[color] = max(int(num), bag[color])
    bags.append(reduce((lambda x, y: x * y), bag.values()))

print(f'P2: {sum(bags)}')
