from statistics import median, mean
position = [int(num)
            for num in open('aoc2021/inputs/7.txt').readline().split(",")]


def calc_fuel(lst, num):
    return sum([abs(i-num) for i in lst])


m = int(median(position))
print(m)
print(calc_fuel(position, m))


def triangle_num(n):
    return int(n*(n+1)/2)


def calc_fuel2(lst, num):
    return sum([triangle_num(abs(i-num)) for i in lst])


lowest = calc_fuel2(position, 0)
idx = 0
for i in range(1, max(position)):
    s = calc_fuel2(position, i)
    if s < lowest:
        lowest = s
        idx = i

print(idx)
print(calc_fuel2(position, idx))
