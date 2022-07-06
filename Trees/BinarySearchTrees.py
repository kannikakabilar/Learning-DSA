# Binary Search Trees

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search(given, root):
    if root is None:
        return False
    else:
        if root.val == given:
            return True
        else:
            if given < root.val:
                search(given, root.left)
            else:
                search(given, root.right)

def insert(node, root):
    if root is None:
        return False
    else:
        if root.val > node.val:
            if root.left is None:
                root.left = node
            else:
                insert(node, root.left)

        else:
            if root.right is None:
                root.right = node
            else:
                insert(node, root.right)
def get_leftmost(root):
    tmp = root
    while not(tmp.left is None):
        tmp = tmp.left
    return tmp
def deleteNode(root, key):
 
    # Base Case
    if root is None:
        return root
 
    # If the key to be deleted
    # is smaller than the root's
    # key then it lies in  left subtree
    if key < root.key:
        root.left = deleteNode(root.left, key)
 
    # If the kye to be delete
    # is greater than the root's key
    # then it lies in right subtree
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
 
    # If key is same as root's key, then this is the node
    # to be deleted
    else:
 
        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        # Node with two children:
        # Get the inorder successor
        # (smallest in the right subtree)
        temp = get_leftmost(root.right)
 
        # Copy the inorder successor's
        # content to this node
        root.key = temp.key
 
        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.key)
 
    return root