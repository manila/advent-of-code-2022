elves = [0]
num = 0

with open('input.txt') as fp:
    for line in fp:
        if line == '\n':
            num += 1
            elves.append(0)
        else:
            print(line)
            elves[num] = elves[num] + int(line)

print(sorted(elves))
