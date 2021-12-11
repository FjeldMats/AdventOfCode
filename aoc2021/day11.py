numbers = [[int(num) for num in line.strip()]
           for line in open('aoc2021/inputs/11.txt')]


def print_table(lst):
    print()
    for row in lst:
        for number in row:
            print(number, end='')
        print()


def get_neighbors(x, y, lst):
    neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1),
                 (-1, -1), (1, 1), (-1, 1), (1, -1)]
    vals = []
    for offset_x, offset_y in neighbors:
        new_x, new_y = x+offset_x, y+offset_y
        if 0 <= new_x < len(lst[0]) and 0 <= new_y < len(lst):
            vals.append((new_x, new_y))
    return vals


def blink(x, y, numbers, blinked):
    blinked.add((x, y))

    for nx, ny in get_neighbors(x, y, numbers):
        numbers[ny][nx] += 1
        if numbers[ny][nx] > 9 and (nx, ny) not in blinked:
            blinked.add((nx, ny))
            blink(nx, ny, numbers, blinked)


def take_step(numbers):
    # 1. increase all numbers by 1
    for y, row in enumerate(numbers):
        for x, number in enumerate(row):
            numbers[y][x] += 1

    # 2. check for blinks, and increase andjacent by +1
    blinked = set()
    for y, row in enumerate(numbers):
        for x, number in enumerate(row):
            if number > 9 and not (x, y) in blinked:
                blink(x, y, numbers, blinked)

    # 3. set all flashes back to 0
    for x, y in blinked:
        numbers[y][x] = 0

    return len(blinked)


total = 0
for i in range(100):
    blinks = take_step(numbers)
    total += blinks
print(total)


numbers = [[int(num) for num in line.strip()]
           for line in open('aoc2021/inputs/11.txt')]
for i in range(1000):
    blinks = take_step(numbers)
    if blinks == len(numbers)*len(numbers[0]):
        print(i+1)
        break
