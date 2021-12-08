
file = 'aoc2021/inputs/8.txt'
digits = [[segment.split(" ") for segment in digit.strip().split(" | ")]
          for digit in open(file).readlines()]

unique = [2, 3, 4, 7]

count = 0
for digit in digits:
    for segment in digit[1]:
        if len(segment) in unique:
            count += 1

print(count)


def overlaps(str1, str2):
    o = 0
    for s in str1:
        if s in str2:
            o += 1
    return o


def contains(str1, str2):
    for s in str1:
        if s not in str2:
            return False
    else:
        return True


def compare(s1, s2):
    return sorted(s1) == sorted(s2)


def decode(numbers):
    one = ''
    four = ''
    for num in numbers:
        if num[1] == 2:
            num[2] = 1
            one = num[0]
        elif num[1] == 3:
            num[2] = 7
        elif num[1] == 4:
            num[2] = 4
            four = num[0]
        elif num[1] == 7:
            num[2] = 8

    for num in numbers:
        # find 3, only 5 segment that contains both segments in 'one'
        if num[1] == 5 and contains(one, num[0]):
            num[2] = 3
        # find  2, only with an overlap of 2 with four
        elif num[1] == 5 and overlaps(num[0], four) == 2:
            num[2] = 2
        # find 5, only with an overlap of 3 with four
        elif num[1] == 5 and overlaps(num[0], four) == 3:
            num[2] = 5

        # 6, only with 1 overlap with one
        elif num[1] == 6 and overlaps(num[0], one) == 1:
            num[2] = 6

        # 9 or 0, both 9 and 0 have 2 overlap with one
        elif num[1] == 6 and overlaps(num[0], one) == 2:
            if overlaps(num[0], four) == 4:
                num[2] = 9
            if overlaps(num[0], four) == 3:
                num[2] = 0


total = 0
for row in digits:
    lengths = []
    for number in row[0]:
        l = len(number)
        lengths.append([number, l, None])
    decode(lengths)
    s = ''
    for number in row[1]:
        for length in lengths:
            if compare(number, length[0]):
                s += str(length[2])
    total += int(s)

print(total)
