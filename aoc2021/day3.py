data = [line.strip() for line in open("aoc2021/inputs/3.txt")]

def count_bits(data):
    zeros = [0] * len(data[0])
    ones = [0] * len(data[0])

    for bit_str in data:
        for idx, bit in enumerate(bit_str):
            if bit == '1':
                ones[idx] += 1
            if bit == '0':
                zeros[idx] += 1
    return ones, zeros

# part 1 -  power consumption

ones, zeros = count_bits(data)
epsilon = [0]*len(data[0])
gamma = [0]*len(data[0])

for i in range(len(data[0])):
    if zeros[i] < ones[i]:
        epsilon[i] = 0
        gamma[i] = 1
    else:
        epsilon[i] = 1
        gamma[i] = 0

e = int(''.join([str(i) for i in epsilon]),2)
g = int(''.join([str(i) for i in gamma]),2)

print("part 1:")
print(f"epsilon rate: {e} \ngamma rate {g} \npower consumption = {e*g}\n\n")


# part 2 - life support rating

def equal_or_greater(num1,num2):
    return num1 >= num2

def strictly_less(num1,num2):
    return num1 < num2

def filter(ones, zeros, lst, comp_op):
    for idx in range(len(ones)):
        if comp_op(ones[idx], zeros[idx]):
            lst = [lst[i] for i in range(len(lst)) if lst[i][idx] == '1']
        else:
            lst = [lst[i] for i in range(len(lst)) if lst[i][idx] == '0']
        ones, zeros = count_bits(lst)
        if(len(lst) == 1):
            return int(''.join([str(i) for i in lst[0]]), 2)

oxygen_gen = filter(ones, zeros, data, equal_or_greater)
co2_scrub = filter(ones, zeros, data, strictly_less)

print("part 2:")
print(f"oxygen_gen: {oxygen_gen} \nco2_scrub {co2_scrub} \nsupport rating = {oxygen_gen*co2_scrub}")