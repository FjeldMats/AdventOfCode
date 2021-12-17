all_input = [i.strip() for i in open('aoc2021/inputs/13.txt').readlines()]
x = all_input.index('')
instructions = all_input[x+1:]
points = [list(map(int, point.split(","))) for point in all_input[:x]]
points = set([(point[0], point[1]) for point in points])


def print_table(lst):
    print()
    for row in lst:
        for number in row:
            print(number, end='')
        print()


def draw_points(points):
    max_y = max(points, key=lambda item: item[1])[1]+1
    max_x = max(points, key=lambda item: item[0])[0]+1

    matrix = [['.' for _ in range(max_x)] for _ in range(max_y)]
    for x, y in points:
        matrix[y][x] = "#"

    print_table(matrix)


def hor_fold(points, y):
    top_points = set([point for point in points if point[1] < y])
    bottom_points = set([point for point in points if point[1] > y])
    assert len(top_points) + len(bottom_points) == len(points)

    for p_x, p_y in bottom_points:
        top_points.add((p_x, y-(p_y-y)))

    return top_points


def ver_fold(points, x):
    left = set([point for point in points if point[0] < x])
    right = set([point for point in points if point[0] > x])
    assert len(right) + len(left) == len(points)

    for p_x, p_y in right:
        left.add((x-(p_x-x), p_y))

    return left


instructions = [i.split(" ")[2] for i in instructions]

for instruction in instructions:
    instruction = instruction.split("=")
    print(instruction)
    num = int(instruction[1])
    if instruction[0] == 'y':
        points = hor_fold(points, num)
    if instruction[0] == 'x':
        points = ver_fold(points, num)
draw_points(points)
print(len(points))




