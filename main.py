from Node import *

goalState = [
    ['7', '8', '1'],
    ['6', '*', '2'],
    ['5', '4', '3']
]

initialState = [
    ['6', '7', '1'],
    ['8', '2', '*'],
    ['5', '4', '3']
]


def DFS(initial_state, goal_state, limit):
    initialNode = Node(initialState, 0)
    stack = [initialNode]
    result = "failure"
    numGenerated = 0

    while len(stack) is not 0:
        node = stack.pop()
        if node.state == goalState:
            pass
        if node.cost >= limit:
            result = "cutoff"
