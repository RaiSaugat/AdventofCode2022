import math;

lines = []

with open('input.txt') as f:
    for line in f:
        lines.append(line.strip())

def _splitHyphen(array):
    return array.split("-")

def solutionA():
    occurrence = 0
    for x in range(math.ceil(len(lines))):
        parts = lines[x].split(",")
        left = int(_splitHyphen(parts[0]))
        right = int(_splitHyphen(parts[1]))

        if (left[0] <= right[0] and right[1] <= left[1]) or (right[0] <= left[0] and left[1] <= right[1]):
            occurrence += 1

    print(occurrence)

def solutionB():
    overLap = 0
    for x in range(math.ceil(len(lines))):
        parts = lines[x].split(",")
        left = int(_splitHyphen(parts[0]))
        right = int(_splitHyphen(parts[1]))
        range1 = range(left[0], left[1] + 1)
        range2 = range(right[0], right[1] + 1)

        for y in range1:
            if y in range2:
                overLap +=1;
                break;

    print(overLap)

solutionA()
solutionB()