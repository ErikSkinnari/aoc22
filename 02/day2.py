
# Rock      A   X
# Paper     B   Y
# Scissors  C   Z

playerScore = 0


def getSelectionPoints(selection):
    if selection == 'A' or selection == 'X':
        return 1
    elif selection == 'B' or selection == 'Y':
        return 2
    elif selection == 'C' or selection == 'Z':
        return 3

def getWinningSelection(opponentsSelection):
    if opponentsSelection == 'A':
        return 'Y'
    elif opponentsSelection == 'B':
        return 'Z'
    elif opponentsSelection == 'C':
        return 'X'
    return ''

def readInput():
    return open("input.txt", "r")

def getRoundPoints(opponentSelection, playerSelection):
    if ((opponentSelection == 'A' and playerSelection == 'X') 
        or (opponentSelection == 'B' and playerSelection == 'Y') 
        or (opponentSelection == 'C' and playerSelection == 'Z')):
        print('draw')
        return 3
    
    if playerSelection == getWinningSelection(opponentSelection):
        print('player win')
        return 6

    print('player lose')
    return 0


input = readInput()

for round in input:

    print()
    opponentSelection = round[0]
    playerSelection = round[2]

    print('Opponent: ' + opponentSelection + ' | Player: ' + playerSelection)
    playerScoreCurrentRound = getRoundPoints(opponentSelection, playerSelection)
    playerScoreCurrentRound += getSelectionPoints(playerSelection)

    playerScore += playerScoreCurrentRound
    print(playerScoreCurrentRound)

print(playerScore)

