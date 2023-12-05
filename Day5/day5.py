with open('input.txt') as f:
    lines = f.readlines()

def fill_ranges(nums):
    ranges = []
    for line in nums:
        end, val, size = line.strip().split()
        ranges.append((int(val), int(val) + (int(size) - 1), int(end) - int(val))) # if the value is in the range, receive the difference between the base value and base end-point
    return ranges

def slide(start, plots):
    for plot in plots:
        if start >= plot[0] and start <= plot[1]:
            end = start + plot[2]
            break
    else:
        end = start
    return end



# P1

seeds = lines[0].split(':')[1].strip().split()

remaining = lines[3:] # skipping the text line
end = remaining.index('\n')
soil_map = fill_ranges(remaining[:end])

remaining = remaining[end + 2:]
end = remaining.index('\n')
fert_map = fill_ranges(remaining[:end])

remaining = remaining[end + 2:]
end = remaining.index('\n')
water_map = fill_ranges(remaining[:end])

remaining = remaining[end + 2:]
end = remaining.index('\n')
light_map = fill_ranges(remaining[:end])

remaining = remaining[end + 2:]
end = remaining.index('\n')
temp_map = fill_ranges(remaining[:end])

remaining = remaining[end + 2:]
end = remaining.index('\n')
humid_map = fill_ranges(remaining[:end])

remaining = remaining[end + 2:]
loc_map = fill_ranges(remaining)


height = []
for seed in seeds:
    seed_num = int(seed)
    soil = slide(seed_num, soil_map)
    fert = slide(soil, fert_map)
    water = slide(fert, water_map)
    light = slide(water, light_map)
    temp = slide(light, temp_map)
    humid = slide(temp, humid_map)
    loc = slide(humid, loc_map)
    height.append(loc)

print(height)
print(f'P1: {min(height)}')
