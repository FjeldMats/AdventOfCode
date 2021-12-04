nums = [int(num.strip()) for num in open('aoc2019/inputs/1.txt').readlines()]


def calc_fuel(mass):
    return (mass//3)-2


def rec_fuel(mass):
    fuel = calc_fuel(mass)
    if fuel < 0:
        return 0
    else:
        return fuel + rec_fuel(fuel)


total_fuel = sum([calc_fuel(mass) for mass in nums])
print(total_fuel)

total_rec_fuel = sum([rec_fuel(mass) for mass in nums])
print(total_rec_fuel)
