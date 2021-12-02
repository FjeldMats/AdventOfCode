
nums = list(map(int, open("aoc2019/2.txt").read().split(",")))

# restore the computer to "1202 program alarm"
nums[1] = 12
nums[2] = 2

# optcode always at index 0
# - can be three values: 
#      - optcode 1: add numbers
#      - optcode 2: multiply numbers 
#      - optcode 3: program halt 

def evalOptcode(lst, row):
    # if first index 1 add,  otherwise mult
    if lst[row] == 1:
        return lst[lst[row+1]] + lst[lst[row+2]]
    else: 

        return lst[lst[row+1]] * lst[lst[row+2]]


def checkHealt(lst, row):
    return lst[row] == 99

row = 0
while(checkHealt(nums, row) == False):
    newNum = evalOptcode(nums, row)
    nums[row+3] = newNum
    print(nums[row:row+4])
    row += 4


print(nums[row-4:row])