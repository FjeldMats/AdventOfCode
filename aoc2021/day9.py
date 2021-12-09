file = 'aoc2021/inputs/9.txt'
nums = [[int(num) for num in line.strip()] for line in open(file).readlines()]


def get_neighbors(x, y, lst):
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    vals = []
    for offset_x, offset_y in neighbors:
        new_x, new_y = x+offset_x, y+offset_y
        # if within bounds of lst add
        if 0 <= new_x < len(lst[0]) and 0 <= new_y < len(lst):
            vals.append((new_x, new_y))
    return vals


hight = len(nums)
length = len(nums[0])
lows = []
part_1_sum = 0
for y in range(hight):
    for x in range(length):
        point = nums[y][x]
        if all(nums[neighbor_y][neighbor_x] > point for neighbor_x, neighbor_y in get_neighbors(x, y, nums)):
            lows.append((x, y))
            part_1_sum += nums[y][x]+1

print(part_1_sum)

# part 2


def besin_size(x, y, lst, visited):
    visited.add((x, y))
    size = 0
    for neighbor_x, neighbor_y in get_neighbors(x, y, lst):
        if lst[y][x] < lst[neighbor_y][neighbor_x] and  \
            (neighbor_x, neighbor_y) not in visited and \
                lst[neighbor_y][neighbor_x] != 9:
            visited.add((neighbor_x, neighbor_y))
            size += besin_size(neighbor_x, neighbor_y, lst, visited) + 1
    else:
        return size


besins = []
visited = set()
for low_x, low_y in lows:
    size = besin_size(low_x, low_y, nums, visited)
    #print(low_x,low_y, size)
    besins.append(size+1)

biggest = reversed(sorted(besins))
part_2_product = 1
for i in range(3):
    b = next(biggest)
    part_2_product *= b
print(part_2_product)
