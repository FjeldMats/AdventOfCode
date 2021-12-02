f = open("aoc2021/inputs/2.txt")
movements = []
for line in f:
    movements.append(line.strip())


movements_ex = ["forward 5", "down 5","forward 8","up 3","down 8","forward 2"]

pos = {'forward': 0, 'down': 0, 'up': 0}

# part 1 
for move in movements:
    action, value = move.split(" ")
    pos[action] += int(value)

depth = pos['down'] - pos['up']
hor_pos = pos['forward']

print(pos)

print(depth, hor_pos)
print(depth * hor_pos)
print("\npart 2\n")

# part 2 

pos = {'forward':0, 'aim': 0,'depth': 0}

for move in movements:
    action, value = move.split(" ")
    value = int(value)
    if action == 'down':
        pos['aim'] += value
    elif action == 'up':
        pos['aim'] -= value
    elif action == 'forward':
        pos['forward'] += value
        pos['depth'] += pos['aim'] * value

depth = pos['depth']
hor_pos = pos['forward']

print(pos)

print(depth, hor_pos)
print(depth * hor_pos)