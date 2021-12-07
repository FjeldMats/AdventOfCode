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


m = int(mean(position)) # this works input data 
n = round(mean(position)) # this works for only test? 

if calc_fuel2(position, m) > calc_fuel2(position, n):
    print(n, calc_fuel2(position, n))
else:
    print(m, calc_fuel2(position, m))


