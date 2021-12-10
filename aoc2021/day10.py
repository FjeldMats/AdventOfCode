from collections import deque

lines = [line.strip() for line in  open("aoc2021/inputs/10.txt")] 

closing = [')', ']', '}', '>']
opening = ['(', '[', '{', '<']

def get_closing(c):
    return closing[opening.index(c)]        

def currupted(s):
    q = deque()
    q.append(s[0])
    for character in s[1:]:
        if character in closing:
            if get_closing(q[-1]) == character:
                q.pop()
            else:
                #print('expected', get_closing(q[-1]), 'but got ', character)
                return character
        elif character in opening:
            q.append(character)

incomplete = []
points = {')':3, ']': 57, '}':1197, '>':25137}
illegal = []
for line in lines:
    #print(line,isIncompleate(line))
    c = currupted(line)
    if c is not None:
        illegal.append(c)
    else:
        incomplete.append(line)
print(sum([points[c] for c in illegal]))

autocomplete_points = {')':1, ']': 2, '}':3, '>':4}

def autocomplete(s):
    q = deque()
    q.append(s[0])
    for character in s[1:]:
        if character in closing:
            if get_closing(q[-1]) == character:
                q.pop()
            else:
                #print('expected', get_closing(q[-1]), 'but got ', character)
                return character
        elif character in opening:
            q.append(character)
    else:
        score = 0
        for character in reversed(q):
            score *= 5
            score += autocomplete_points[get_closing(character)]
        return score


scores = []
for line in incomplete:
    scores.append(autocomplete(line))
scores = sorted(scores)
print(scores[len(scores)//2])
