f = open('aoc2021/inputs/5.txt')


def parseline(line):
    return [list(map(int, point.split(","))) for point in line.split(" -> ")]


def make_board(size):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append('.')
    return board


def print_board(board):
    size = len(board)
    for i in range(size):
        for j in range(size):
            print(board[i][j], end="")
        print()


def size_of_board(lines):
    max_value = -1
    for line in lines:
        for point in line:
            max_value = max(max(point[0], point[1]), max_value)
    return max_value


def draw_point(board, x, y):
    if board[x][y] == '.':
        return 1
    else:
        return board[x][y] + 1


def draw_line(board, line, diagonal=False):
    x1 = line[0][0]
    x2 = line[1][0]
    y1 = line[0][1]
    y2 = line[1][1]

    # vertial line
    if x1 == x2:
        for y in range(min(y1, y2), max(y1, y2)+1):
            board[y][x1] = draw_point(board, y, x1)

    # horizontal
    elif y1 == y2:
        for x in range(min(x1, x2), max(x1, x2)+1):
            board[y1][x] = draw_point(board, y1, x)

    elif x1 != x2 and y1 != y2 and diagonal:
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

        for x, y in zip(xs, ys):
            board[y][x] = draw_point(board, y, x)


def count_overlaps(board, num):
    count = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != '.' and board[i][j] >= num:
                count += 1
    return count


lines = [parseline(line.strip()) for line in f.readlines()]
max_value = size_of_board(lines)

board = make_board(max_value+1)
for line in lines:
    draw_line(board, line)

print(count_overlaps(board, 2))

# part 2
board = make_board(max_value+1)
for line in lines:
    draw_line(board, line, diagonal=True)
print(count_overlaps(board, 2))
