data = [int(line.strip()) for line in open("aoc2021/inputs/1.txt")]

#part 1 
prev = data[0]
inc = 0
for measurement in data: 
    if measurement > prev: 
        inc += 1
    prev = measurement
print(inc)


#part 2
window = sum(data[0:3])
prev_window = window
inc = 0
for idx in range(len(data)): 
    if window > prev_window:
        inc += 1
    prev_window = window
    window = sum(data[0+idx:3+idx])
print(inc)