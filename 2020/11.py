# Problem: https://adventofcode.com/2020/day/11
def getInput():
    '''Returns input as a 2D array'''
    state = open('input/11.txt', 'r')
    state = [list(line.strip()) for line in state]
    return state

def writeOutput(state):
    output = open("output/11.txt", "w")
    for row in state:
        rowString = ''.join(row)
        output.write(rowString)
        output.write("\n")
    output.close()

# Helper Functions
def nextState(state, rule, lowerLimit):
    newState = [row[:] for row in state]
    for row in range(len(state)): 
        for col in range(len(state[0])): 
            if state[row][col] == 'L' and rule(state, row, col) == 0: 
                newState[row][col] = '#'
            elif state[row][col] == '#' and rule(state, row, col) >= lowerLimit:
                newState[row][col] = 'L'     
    return newState

def numAdjacentSeats(state, row, col):
    count = 0 
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2): 
            if withinBounds(state, i, j) and not (row == i and col == j) and state[i][j] == '#': 
                count += 1
    return count 

def numAdjacentVisibleSeats(state, row, col):
    count, rowLen, colLen = 0, len(state), len(state[0])
    for rightSeat in state[row][col + 1:colLen]:
        if rightSeat != '.':
            if rightSeat == '#':
                count += 1
            break

    for leftSeat in reversed(state[row][0:col]):
        if leftSeat != '.':
            if leftSeat == '#':
                count += 1
            break

    for downRow in state[row + 1:rowLen]: 
        if downRow[col] != '.':
            if downRow[col] == '#':
                count += 1
            break
    
    for upRow in reversed(state[0:row]): 
        if upRow[col] != '.':
            if upRow[col] == '#':
                count += 1
            break 

    # upper right
    i, j = row - 1, col + 1
    while withinBounds(state, i, j):
        if state[i][j] != '.':
            if state[i][j] == '#':
                count += 1
            break
        i, j = i - 1, j + 1
    
    # upper left 
    i, j = row - 1, col - 1
    while withinBounds(state, i, j):
        if state[i][j] != '.':
            if state[i][j] == '#':
                count += 1
            break
        i, j = i - 1, j - 1

    # lower left 
    i, j = row + 1, col - 1
    while withinBounds(state, i, j):
        if state[i][j] != '.':
            if state[i][j] == '#':
                count += 1
            break
        i, j = i + 1, j - 1

    # lower right
    i, j = row + 1, col + 1
    while withinBounds(state, i, j):
        if state[i][j] != '.':
            if state[i][j] == '#':
                count += 1
            break
        i, j = i + 1, j + 1
    
    return count 

def withinBounds(state, i, j): 
    return i >= 0 and j >= 0 and i < len(state) and j < len(state[0])

def numOccupiedSeats(state):
    count = 0
    for row in state:
        for val in row: 
            if val == '#':
                count += 1
    return count

# Solving 
def solve(rule, limit):
    state = getInput()
    newState = nextState(state, rule, limit)
    while state != newState:
        state = [row[:] for row in newState]
        newState = nextState(state, rule, limit)
    numOccupied = numOccupiedSeats(state)
    writeOutput(state)
    return numOccupied

print("Problem 1:", solve(numAdjacentSeats, 4))
print("Problem 2:", solve(numAdjacentVisibleSeats, 5))