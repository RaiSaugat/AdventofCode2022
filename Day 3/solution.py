import math;

lowerCase = 1
upperCase = 27
lowerCaseAscii = 97
upperCaseAscii = 65
lines = []

with open('input.txt') as f:
    for line in f:
        lines.append(line.strip())

def findValue(letter):
    if ord(letter) > 65 and ord(letter) < 97:
        return (ord(letter) - upperCaseAscii) + upperCase
    else:
        return (ord(letter) - lowerCaseAscii) + lowerCase

def solutionA():
    sum = 0
    for x in lines:
        half = math.floor(len(x)/2);
        partOne = x[:half]
        partTwo = x[half: len(x)]
        a = list(set(partOne)&set(partTwo))
        value = findValue(a[0])
        sum += value

    print(sum)

def solutionB():
    sum = 0
    i=0
    for x in range(math.ceil(len(lines) / 3)):
        a = list(set(lines[i])&set(lines[i+1])&set(lines[i+2]))
        i += 3
        value = findValue(a[0])
        sum += value
    print(sum)


solutionA()
solutionB()
