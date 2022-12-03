ROCK_1 = 'A'
PAPER_1= 'B'
SCISSORS_1 = 'C'
ROCK_VALUE = 1
PAPER_VALUE = 2
SCISSORS_VALUE = 3

ROCK_2 = 'X'
PAPER_2 = 'Y'
SCISSORS_2 = 'Z'


file = open("input.txt", "r")
line_list = file.readlines();
myScoreA = 0
myScoreB = 0

for x in line_list:
    if x[0] == ROCK_1:
        if x[2] == ROCK_2:
            myScoreA += ROCK_VALUE + 3
        if x[2] == PAPER_2:
            myScoreA += PAPER_VALUE + 6
        if x[2] == SCISSORS_2:
            myScoreA += SCISSORS_VALUE

    if x[0] == PAPER_1:
        if x[2] == ROCK_2:
            myScoreA += ROCK_VALUE
        if x[2] == PAPER_2:
            myScoreA += PAPER_VALUE + 3
        if x[2] ==  SCISSORS_2:
            myScoreA += SCISSORS_VALUE + 6

    if x[0] == SCISSORS_1:
        if x[2] == ROCK_2:
            myScoreA += ROCK_VALUE + 6
        if x[2] == PAPER_2:
            myScoreA += PAPER_VALUE
        if x[2] == SCISSORS_2:
            myScoreA += SCISSORS_VALUE + 3

for x in line_list:
    if x[0] == ROCK_1:
        if x[2] == ROCK_2:
            myScoreB += SCISSORS_VALUE
        if x[2] == PAPER_2:
            myScoreB += ROCK_VALUE + 3
        if x[2] == SCISSORS_2:
            myScoreB += PAPER_VALUE + 6

    if x[0] == PAPER_1:
        if x[2] == ROCK_2:
            myScoreB += ROCK_VALUE
        if x[2] == PAPER_2:
            myScoreB += PAPER_VALUE + 3
        if x[2] ==  SCISSORS_2:
            myScoreB += SCISSORS_VALUE + 6

    if x[0] == SCISSORS_1:
        if x[2] == ROCK_2:
            myScoreB += PAPER_VALUE
        if x[2] == PAPER_2:
            myScoreB += SCISSORS_VALUE + 3
        if x[2] == SCISSORS_2:
            myScoreB += ROCK_VALUE + 6

print(myScoreA)
print(myScoreB)