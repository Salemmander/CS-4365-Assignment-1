import copy
import sys

goalState = [
    ['7', '8', '1'],
    ['6', '*', '2'],
    ['5', '4', '3']
]

path_states = 0
states_enqueued = 0


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
    newState = copy.deepcopy(current_state)
    starIndex = findStar(newState)
    if starIndex[0] != 0:
        newStarIndex = [starIndex[0] - 1, starIndex[1]]
        return switchStates(newState, starIndex, newStarIndex)


def moveRight(current_state):
    newState = copy.deepcopy(current_state)
    starIndex = findStar(newState)
    if starIndex[1] != 2:
        newStarIndex = [starIndex[0], starIndex[1] + 1]
        return switchStates(newState, starIndex, newStarIndex)


def moveDown(current_state):
    newState = copy.deepcopy(current_state)
    starIndex = findStar(newState)
    if starIndex[0] != 2:
        newStarIndex = [starIndex[0] + 1, starIndex[1]]
        return switchStates(newState, starIndex, newStarIndex)


def moveLeft(current_state):
    newState = copy.deepcopy(current_state)
    starIndex = findStar(newState)
    if starIndex[1] != 0:
        newStarIndex = [starIndex[0], starIndex[1] - 1]
        return switchStates(newState, starIndex, newStarIndex)


def expand(current_state):
    return [moveUp(current_state), moveRight(current_state), moveDown(current_state),
            moveLeft(current_state)]


def DFS(current_state, path=None, level=0, limit=10):
    global states_enqueued
    global path_states
    if path is None:
        path = []
    if current_state in path:
        return False
    if current_state is not None:
        states_enqueued += 1
        path_states += 1
        path.append(current_state)
    else:
        return False
    if current_state == goalState:
        return path
    if level == limit:
        path.pop()
        path_states -= 1
        return False
    for child in expand(current_state):
        if DFS(child, path, level + 1):
            return path
    path.pop()
    path_states -= 1
    return False


def IDS(initial_state):
    for i in range(10):
        path = DFS(initial_state)
        if path:
            return path
        else:
            return False


def astar(current_state, heuristic, path=None, level=0, limit=10):
    global path_states, states_enqueued
    if path is None:
        path = []
    if current_state is not None:
        path_states += 1
        path.append(current_state)
    else:
        return False
    costs = []
    children = expand(current_state)
    if current_state == goalState:
        return path
    if level == limit:
        path.pop()
        path_states -= 1
        return False
    for child in children:
        if child not in path:
            states_enqueued += 1
            costs.append(heuristic(child))
    minCost = costs.index(min(costs))
    path.append(children[minCost])
    if astar(children[minCost], heuristic, path, level + 1):
        return path
    path.pop()
    path_states -= 1
    return False


def h1(current_state):
    global goalState
    wrongTiles = 0
    if current_state is not None:
        for index in range(3):
            for jindex in range(3):
                if current_state[index][jindex] != goalState[index][jindex]:
                    wrongTiles += 1
    return wrongTiles


def h2(current_state):
    global goalState
    wrongTilesDifference = 0
    if current_state is not None:
        for index in range(3):
            for jindex in range(3):
                if current_state[index][jindex] != goalState[index][jindex] and current_state[index][jindex] != '*' and \
                        goalState[index][jindex] != '*':
                    wrongTilesDifference += int(current_state[index][jindex]) - int(goalState[index][jindex])
    return wrongTilesDifference


def printState(current_state):
    if isinstance(current_state, str):
        print(current_state)
    else:
        for row in current_state:
            print(row)
        line()


def printPath(current_state):
    if isinstance(current_state, bool):
        print("Can't find goal state")
    else:
        for row in current_state:
            for col in row:
                print(col)
            line()
        print("Moves: ", path_states - 1)
        print("States Enqueued: ", states_enqueued)


def line():
    print('-' * 15)


algorithm = sys.argv[1]
filePath = sys.argv[2]

file = open(filePath, 'r')
text = file.readline().split()

initialState = [text[i:i + 3] for i in range(0, len(text), 3)]

if algorithm == "dfs":
    print("Depth First Search:")
    printPath(DFS(initialState))
elif algorithm == "ids":
    print("Iterative Deepening Search")
    printPath(IDS(initialState))
elif algorithm == "astar1":
    print("A* with first heuristic")
    printPath(astar(initialState, h1))
elif algorithm == "astar2":
    print("A* with second heuristic")
    printPath(astar(initialState, h2))
else:
    print("valid algorithm options are 'dfs', 'ids', 'astar1', and 'astar2'")
