import collections

f = open('aoc2021/inputs/5.txt')


def parseline(line):
    return [list(map(int, point.split(","))) for point in line.split(" -> ")]


def draw_lines(lines, diagonal=False):
    points = collections.defaultdict(int)
    for line in lines:
        x1, y1 = line[0]
        x2, y2 = line[1]

        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                points[(x1, y)] += 1
        elif y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                points[(x, y1)] += 1

        else:
            xs = []
            ys = []

            for x in range(min(x1, x2), max(x1, x2)+1):
                xs.append(x)
            for y in range(min(y1, y2), max(y1, y2)+1):
                ys.append(y)

            if x1 == max(x1, x2):
                xs = list(reversed(xs))
            if y1 == max(y1, y2):
                ys = list(reversed(ys))

            if diagonal:
                for x, y in zip(xs, ys):
                    points[(x, y)] += 1

    return points


lines = [parseline(line.strip()) for line in f.readlines()]

print(len([x for x in draw_lines(lines).values() if x >= 2]))
print(len([x for x in draw_lines(lines, diagonal=True).values() if x >= 2]))
