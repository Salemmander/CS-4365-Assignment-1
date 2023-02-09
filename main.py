goalState = [
    ['7', '8', '1'],
    ['6', '*', '2'],
    ['5', '4', '3']
]

initialState = [
    ['6', '7', '1'],
    ['8', '*', '2'],
    ['5', '4', '3']
]


def findStar(current_state):
    row = 0
    col = 0
    for i in range(3):
        for j in range(3):
            if current_state[i][j] == '*':
                return i, j


def switchStates(current_state, initial_index, new_index):
    current_state[initial_index[0]][initial_index[1]] = current_state[new_index[0]][new_index[1]]
    current_state[new_index[0]][new_index[1]] = '*'
    return current_state


def moveUp(current_state):
    starIndex = findStar(current_state)
    if starIndex[0] == 0:
        return "Cannot move up from this position"
    else:
        print("Move Up")
        newStarIndex = [starIndex[0] - 1, starIndex[1]]
        return switchStates(current_state, starIndex, newStarIndex)


def moveRight(current_state):
    starIndex = findStar(current_state)
    if starIndex[1] == 2:
        return "Cannot move right from this position"
    else:
        print("Move Right")
        newStarIndex = [starIndex[0], starIndex[1] + 1]
        return switchStates(current_state, starIndex, newStarIndex)


def moveDown(current_state):
    starIndex = findStar(current_state)
    if starIndex[0] == 2:
        return "Cannot move down from this position"
    else:
        print("Move Down")
        newStarIndex = [starIndex[0] + 1, starIndex[1]]
        return switchStates(current_state, starIndex, newStarIndex)


def moveLeft(current_state):
    starIndex = findStar(current_state)
    if starIndex[1] == 0:
        return "Cannot move left from this position"
    else:
        print("Move Left")
        newStarIndex = [starIndex[0], starIndex[1] - 1]
        return switchStates(current_state, starIndex, newStarIndex)


def DFS(current_state, limit):
    pass


def IDS(initial_state, limit):
    pass


def astar(initial_state):
    pass


def printState(current_state):
    if isinstance(current_state, str):
        print(current_state)
    else:
        for row in current_state:
            print(row)


def line():
    print('-' * 15)


print("Initial State")
printState(initialState)
line()
printState(moveUp(initialState))
line()
printState(moveDown(initialState))
line()
printState(moveRight(initialState))
line()
printState(moveLeft(initialState))
