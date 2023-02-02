from treelib import Node, Tree

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

tree = Tree()
tree.create_node(initialState, tree.size())
tree.create_node(1, tree.size(), parent=tree.size() - 1)
tree.show()


