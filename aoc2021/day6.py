def reset_timers(timers):
    for idx, timer in enumerate(timers):
        if timer == 0:
            timers[idx] = 6
            timers.append(9)
        else:
            timers[idx] -= 1


def calc_children(current_day, max_day):
    return (max_day-current_day)//7


def first_count(current_day, max_day):
    return 1 + count(current_day, max_day)


def count(current_day, max_day):
    if current_day > max_day:
        return 0
    n_children = calc_children(current_day, max_day)
    children = [count(current_day+(9*(i+1)), max_day) for i in range(0, n_children)]
    print(children)
    return 1 + n_children + sum(children)


def go_to_next_day(count_fish): 
    new_fish_count = [0]*9

    new_fish = count_fish[0]

    for i in range(1,len(count_fish)): 
        new_fish_count[i-1] = count_fish[i]
    
    new_fish_count[8] = new_fish
    new_fish_count[6] += new_fish
    return new_fish_count


def calc2(inital_timers,max_day):

    # number of fish at day 0, number of fish at day 1 ...
    count_fish = [0]*9

    for i in range(len(inital_timers)): 
        count_fish[inital_timers[i]] += 1

    for _ in range(max_day): 
        count_fish = go_to_next_day(count_fish)
    return sum(count_fish)



timers = [int(time)
          for time in open('aoc2021/inputs/6.txt').readline().split(",")]
days = range(0, 80)
for day in days:
    reset_timers(timers)
print(len(timers))


timers = [int(time) for time in open('aoc2021/inputs/6.txt').readline().split(",")]
print(calc2(timers,256))