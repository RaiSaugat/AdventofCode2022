
file = open("input.txt", "r")
line_list = file.readlines();

ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSOR = 'SCISSOR'

ROCK_1 = 'A'
PAPER_1= 'B'
SCISSOR_1 = 'C'

ROCK_VALUE = 1
PAPER_VALUE = 2
SCISSOR_VALUE = 3

ROCK_2 = 'X'
PAPER_2 = 'Y'
SCISSOR_2 = 'Z'

handMap = {
    'A': ROCK,
    'B': PAPER,
    'C': SCISSOR,
    'X': ROCK,
    'Y': PAPER,
    'Z': SCISSOR,
}

value = {
    ROCK: 1,
    PAPER: 2,
    SCISSOR: 3,
}

rules = {
    'lose': {
        ROCK: value[SCISSOR],
        PAPER: value[ROCK],
        SCISSOR: value[PAPER],
    },
    'draw': {
        ROCK: value[ROCK] + 3,
        PAPER: value[PAPER] + 3,
        SCISSOR: value[SCISSOR] + 3,
    },
    'win': {
        ROCK: value[PAPER] + 6,
        PAPER: value[SCISSOR] + 6,
        SCISSOR: value[ROCK] + 6,
    }
}

def drawValue(hand):
    return rules['draw'][handMap[hand]]

def loseValue(hand):
    return rules['lose'][handMap[hand]]

def winValue(hand):
    return rules['win'][handMap[hand]]


def solutionA():
    myScoreA = 0
    for x in line_list:
        if handMap[x[0]] == handMap[x[2]]:
            myScoreA += rules['draw'][handMap[x[0]]]
        else:
            if x[0] == 'A':
                if x[2] == SCISSOR_2:
                    myScoreA += SCISSOR_VALUE
                if x[2] == PAPER_2:
                    myScoreA += PAPER_VALUE + 6

            if x[0] == 'B':
                if x[2] == ROCK_2:
                    myScoreA += ROCK_VALUE
                if x[2] ==  SCISSOR_2:
                    myScoreA += SCISSOR_VALUE + 6

            if x[0] == 'C':
                if x[2] == ROCK_2:
                    myScoreA += ROCK_VALUE + 6
                if x[2] == PAPER_2:
                    myScoreA += PAPER_VALUE
    print(myScoreA)

def solutionB():
    myScore = 0
    for x in line_list:
        if x[2] == 'X':
            myScore += loseValue(x[0])

        if x[2] == 'Y':
           myScore += drawValue(x[0])

        if x[2] == 'Z':
           myScore += winValue(x[0])
    print(myScore)


solutionA()
solutionB()

# 12794
# 14979
