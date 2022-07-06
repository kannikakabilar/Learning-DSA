# General Trees / N-ary Trees

class TreeNode:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children

# Searching
# - Given a value of a node, check if it's equivalent to the root node value
#   if root node value not equivalent to given value, then check node value for each child
# if a leaf is reached return False/Null/-1
def search(given, root):
    if root is None:
        return False
    if root.val == given:
        return True
    else:
        for child in root.children:
            search(given, child)

# Inserting
# - Given a tree node and a node-to-be-inserted, append it to the list of children to the tree node
def insert(node, tree_node):
    if tree_node.children is None:
        tree_node.children = [node]
    else:
        tree_node.children.append(node)

# Deleting - Given a node value to delete, search through the tree to find its node and delete the node
# The children of the deleted node must be handled accordingly





