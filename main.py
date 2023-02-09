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
    for index in range(3):
        for jindex in range(3):
            if current_state[index][jindex] == '*':
                return index, jindex


def switchStates(current_state, initial_index, new_index):
    current_state[initial_index[0]][initial_index[1]] = current_state[new_index[0]][new_index[1]]
    current_state[new_index[0]][new_index[1]] = '*'
    return current_state


def moveUp(current_state):
    starIndex = findStar(current_state)
    if starIndex[0] != 0:
        print("Move Up")
        newStarIndex = [starIndex[0] - 1, starIndex[1]]
        return switchStates(current_state, starIndex, newStarIndex)


def moveRight(current_state):
    starIndex = findStar(current_state)
    if starIndex[1] != 2:
        print("Move Right")
        newStarIndex = [starIndex[0], starIndex[1] + 1]
        return switchStates(current_state, starIndex, newStarIndex)


def moveDown(current_state):
    starIndex = findStar(current_state)
    if starIndex[0] != 2:
        print("Move Down")
        newStarIndex = [starIndex[0] + 1, starIndex[1]]
        return switchStates(current_state, starIndex, newStarIndex)


def moveLeft(current_state):
    starIndex = findStar(current_state)
    if starIndex[1] != 0:
        print("Move Left")
        newStarIndex = [starIndex[0], starIndex[1] - 1]
        return switchStates(current_state, starIndex, newStarIndex)


def expand(current_state):
    nextStates = [moveUp(current_state), moveRight(current_state), moveDown(current_state), moveLeft(current_state)]
    return nextStates


def DFS(current_state, limit, iteration=0):
    if current_state == goalState or iteration == limit:
        return
    else:
        DFS(moveUp(current_state), limit, iteration + 1)
        DFS(moveRight(current_state), limit, iteration + 1)
        DFS(moveDown(current_state), limit, iteration + 1)
        DFS(moveLeft(current_state), limit, iteration + 1)


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
for i in expand(initialState):
    line()
    printState(i)
# DFS(initialState, 10)
