# Problem: https://adventofcode.com/2020/day/11

# Helper Functions
def getInput():
    '''Returns input as a 2D array'''
    state = open('input/11.txt', 'r')
    state = [list(line.strip()) for line in state]
    return state

def nextState(state):
    newState = [row[:] for row in state]
    for row in range(len(state)): 
        for col in range(len(state[0])): 
            if state[row][col] == 'L' and numAdjacentSeats(state, row, col) == 0: 
                newState[row][col] = '#'
            elif state[row][col] == '#' and numAdjacentSeats(state, row, col) >= 4:
                newState[row][col] = 'L'     
    return newState

def numAdjacentSeats(state, row, col):
    count = 0 
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2): 
            if withinBounds(state, i, j) and not (row == i and col == j) and state[i][j] == '#': 
                count += 1
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
def solve():
    state = getInput()
    newState = nextState(state)
    while state != newState: 
        state = [row[:] for row in newState]
        newState = nextState(state)
    numOccupied = numOccupiedSeats(state)
    return numOccupied

print(solve())