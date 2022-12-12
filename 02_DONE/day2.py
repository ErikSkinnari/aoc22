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
    return 'X'

def getLoosingSelection(opponentSelection):
    if opponentSelection == 'A':
            return 'Z'
    elif opponentSelection == 'B':
        return 'X'
    return 'Y'

def getDrawSelection(opponentSelection):
    if opponentSelection == 'A':
        return 'X'
    elif opponentSelection == 'B':
        return 'Y'
    return 'Z'
    
def readInput():
    return open("input.txt", "r")

def getRoundPoints(opponentSelection, playerSelection):
    if ((opponentSelection == 'A' and playerSelection == 'X') 
        or (opponentSelection == 'B' and playerSelection == 'Y') 
        or (opponentSelection == 'C' and playerSelection == 'Z')): # draw
        return 3
    
    if playerSelection == getWinningSelection(opponentSelection): # win
        return 6

    return 0 # loss

def getPlayerPoints(opponentSelection, playerInstruction):

    playerSelection = ''

    if playerInstruction == 'X': # loose
        playerSelection = getLoosingSelection(opponentSelection)
    elif playerInstruction == 'Y': # draw
        playerSelection = getDrawSelection(opponentSelection)
    else: # win
        playerSelection = getWinningSelection(opponentSelection)
    
    return getRoundPoints(opponentSelection, playerSelection) + getSelectionPoints(playerSelection)


input = readInput()

for round in input:

    print()
    opponentSelection = round[0]

    # Solution pt1
    # playerSelection = round[2]
    # print('Opponent: ' + opponentSelection + ' | Player: ' + playerSelection)
    # playerScoreCurrentRound = getRoundPoints(opponentSelection, playerSelection)
    # playerScoreCurrentRound += getSelectionPoints(playerSelection)

    # playerScore += playerScoreCurrentRound
    # print(playerScoreCurrentRound)

    # Solution pt2
    playerInstruction = round[2]
    playerScore += getPlayerPoints(opponentSelection, playerInstruction)

print(playerScore)
