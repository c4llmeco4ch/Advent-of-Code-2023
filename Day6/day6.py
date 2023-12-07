from functools import reduce

with open('test.txt') as f:
    lines=f.readlines()

def calc_distance(held_time, max_time):
    speed = held_time
    return speed * (max_time - held_time)

def find_bound(curr_held, max_time, target, going_down):
    if curr_held == 0 or curr_held == max_time:
        return 0
    if calc_distance(curr_held, max_time) <= target:
        return curr_held + (1 if going_down else -1)
    if going_down is None:
        return (find_bound(curr_held - 1, max_time, target, True),
                find_bound(curr_held + 1, max_time, target, False))
    return find_bound(curr_held - (1 if going_down else -1), max_time, target, going_down)

# P1    

times = lines[0].split(':')[1].strip().split()
records = lines[1].split(':')[1].strip().split()

ways_to_win = []
for t, d in zip(times, records):
    mid = int(t) // 2
    down, up = find_bound(mid, int(t), int(d), None)
    ways_to_win.append(up - down + 1)
print(f'P1:{reduce(lambda x, y: x * y, ways_to_win)}')
