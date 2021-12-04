
nums = list(map(int, open("aoc2019/inputs/2.txt").read().split(",")))


def evalOptcode(lst, row):
    if lst[row] == 1:
        return lst[lst[row+1]] + lst[lst[row+2]]
    else:
        return lst[lst[row+1]] * lst[lst[row+2]]


def checkHealt(lst, row):
    return lst[row] == 99


def run_computer(nums, noun=None, verb=None):
    if noun != None:
        nums[1] = noun
    if verb != None:
        nums[2] = verb

    row = 0
    while(checkHealt(nums, row) == False):
        newNum = evalOptcode(nums, row)
        new_idx = nums[row+3]
        if new_idx > len(nums):
            return -1  # invalid access
        nums[new_idx] = newNum
        row += 4
    return nums[0]


def search_for_output(nums, output, search_space):
    for noun in range(search_space):
        for verb in range(search_space):
            program = nums.copy()
            x = run_computer(program, noun, verb)
            if x == output:
                return noun, verb
    return -1, -1

# part 1


value = run_computer(nums.copy(), 12, 2)
print(value)

# part 2
noun, verb = search_for_output(nums.copy(), 19690720, len(nums))
print(noun, verb)
print(100 * noun + verb)
