all_input = [i.strip() for i in open('aoc2021/inputs/ex14.txt').readlines()]
start = all_input[0]

insertions = [i.split(" -> ") for i in all_input[2:]]
insertions = [(i[0], i[1]) for i in insertions]


def insert_letter(string, letter, index):
    return string[:index] + letter + string[index:]


def preform_step(string, insertions):

    edits = []
    for substring, letter in insertions:
        if substring in string:
            indices = [
                i+1 for i in range(len(string)) if string.startswith(substring, i)]
            for index in indices:
                edits.append((index, letter))

    edits.sort(key=lambda x: x[0])
    for index, letter in reversed(edits):
        string = insert_letter(string, letter, index)

    return string


steps = 40
string = start

for i in range(steps):
    string = preform_step(string, insertions)
    print(i+1, len(string))


def most_frequent(List):
    return max(set(List), key=List.count)


def least_frequent(List):
    return min(set(List), key=List.count)


print()
most = most_frequent(string)
least = least_frequent(string)
print(most, string.count(most))
print(least, string.count(least))
print(string.count(most) - string.count(least))
