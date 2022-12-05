elves = [0]
num = 0

with open('input.txt') as fp:
    for line in fp:
        if line == '\n':
            num += 1
            elves.append(0)
        else:
            elves[num] = elves[num] + int(line)

elves = sorted(elves)
print(sum(elves[-3:]))
