
fname = "aoc2021/inputs/4.txt"
f = open(fname)

numbers = list(map(int, f.readline().strip().split(",")))


def read_board(f):
    f.readline()  # blank sapce
    board = []
    for _ in range(5):
        board.append(
            list(map(int, filter(lambda str: str != '', f.readline().strip().split(" ")))))
    return board


def create_empty():
    return [[0 for _ in range(5)] for _ in range(5)]


def print_board(b):
    for i in range(5):
        for j in range(5):
            print(b[i][j], end=" ")
        else:
            print()
    else:
        print()


def print_boards(bs):
    [(print_board(b)) for b in bs]


def mark_board(boards, marks, nums):
    for board, marked in zip(boards, marks):
        for num in nums:
            for i in range(5):
                for j in range(5):
                    if board[i][j] == num:
                        marked[i][j] = 1
    return boards, marks


def check_rows(board, marked):
    for i in range(5):
        s = 0
        for j in range(5):
            s += marked[i][j]
        if s == 5:
            return sum(board[i])
    else:
        return 0


def check_cols(board, marked):
    for i in range(5):
        s = 0
        for j in range(5):
            s += marked[j][i]

        if s == 5:
            return sum([board[j][idx] for idx in range(5)])
    else:
        return 0


def check_wins(boards, marks):
    winning_boards = []
    for i, (board, marked) in enumerate(zip(boards, marks)):
        r = check_rows(board, marked)
        c = check_cols(board, marked)
        if r != 0 or c != 0:
            winning_boards.append(i)
    return list(set(winning_boards))


# board is 5+1 lines (+1 bc of space between)
count_boards = (len(open(fname).readlines())-1)//6
boards = []
marks = []

for i in range(count_boards):
    boards.append(read_board(f))
    marks.append(create_empty())


idx = 1
winning_boards = []
while True:
    boards, marks = mark_board(boards, marks, numbers[0:idx])
    winning_boards = check_wins(boards, marks)
    if len(winning_boards) != 0:
        break
    idx += 1

winning_board = winning_boards[0]


def calc_score(boards, marks, board_idx):
    sum_of_unmarked = 0
    for i in range(5):
        for j in range(5):
            if(marks[board_idx][i][j] == 0):
                sum_of_unmarked += boards[board_idx][i][j]
    return sum_of_unmarked


sum_of_unmarked = calc_score(boards, marks, winning_board)

last_num = numbers[idx-1]
print(f"{sum_of_unmarked} sum of unmarked")
print(f"last drawn {last_num}")
print(sum_of_unmarked*last_num)


# part 2
for i in range(count_boards):
    marks.append(create_empty())


idx = 1
winning_boards = []
won = []
while idx < len(numbers):
    boards, marks = mark_board(boards, marks, numbers[0:idx])
    winning_boards = check_wins(boards, marks)
    if len(winning_boards) == count_boards:
        break

    for win in winning_boards:
        won.append(win)
    won = list(set(won))  # remove dups

    idx += 1

last_board = (list(set(winning_boards) - set(won))
              )[0]  # difference, last added board

sum_of_unmarked = calc_score(boards, marks, last_board)
last_num = numbers[idx-1]
print("\npart 2:")
print(f"{sum_of_unmarked} sum of unmarked")
print(f"last drawn {last_num}")
print(sum_of_unmarked*last_num)
