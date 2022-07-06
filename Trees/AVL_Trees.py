# AVL Trees

# Generic tree node class
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

# Searching - is the same as binary search tree

# Inserting
"""
Following are two basic operations that can be performed to re-balance 
a BST without violating the BST property (keys(left) < key(root) < keys(right)). 

Left Rotation 
Right Rotation

T1, T2 and T3 are subtrees of the tree 
           
     y                               x
    / \     Right Rotation          /  \
   x   T3   - - - - - - - >        T1   y 
  / \       < - - - - - - -            / \
 T1  T2     Left Rotation            T2  T3

Keys in both of the above trees follow the 
same order 
 keys(T1) < key(x) < keys(T2) < key(y) < keys(T3)

"""
"""
Steps to follow for insertion 

Let the newly inserted node be w 

Perform standard BST insert for w. 
Travel up and find the first unbalanced node. 
Then take action based on case
"""

# Left Left Case
"""
T1, T2, T3 and T4 are subtrees.
         z                                      y 
        / \                                   /   \
       y   T4      Right Rotate (z)          x      z
      / \          - - - - - - - - ->      /  \    /  \ 
     x   T3                               T1  T2  T3  T4
    / \
  T1   T2
"""

# Left Right Case
"""
     z                               z                           x
    / \                            /   \                        /  \ 
   y   T4  Left Rotate (y)        x    T4  Right Rotate(z)    y      z
  / \      - - - - - - - - ->    /  \      - - - - - - - ->  / \    / \
T1   x                          y    T3                    T1  T2 T3  T4
    / \                        / \
  T2   T3                    T1   T2
"""

# Right Right Case
"""
  z                                y
 /  \                            /   \ 
T1   y     Left Rotate(z)       z      x
    /  \   - - - - - - - ->    / \    / \
   T2   x                     T1  T2 T3  T4
       / \
     T3  T4
"""

# Right Left Case
"""
   z                            z                            x
  / \                          / \                          /  \ 
T1   y   Right Rotate (y)    T1   x      Left Rotate(z)   z      y
    / \  - - - - - - - - ->     /  \   - - - - - - - ->  / \    / \
   x   T4                      T2   y                  T1  T2  T3  T4
  / \                              /  \
T2   T3                           T3   T4
"""

# Python code to insert a node in AVL tree

# Generic tree node class
class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		self.height = 1

# AVL tree class which supports the
# Insert operation
class AVL_Tree(object):

	# Recursive function to insert key in
	# subtree rooted with node and returns
	# new root of subtree.
	def insert(self, root, key):
	
		# Step 1 - Perform normal BST
		if not root:
			return TreeNode(key)
		elif key < root.val:
			root.left = self.insert(root.left, key)
		else:
			root.right = self.insert(root.right, key)

		# Step 2 - Update the height of the
		# ancestor node
		root.height = 1 + max(self.getHeight(root.left),
						self.getHeight(root.right))

		# Step 3 - Get the balance factor
		balance = self.getBalance(root)

		# Step 4 - If the node is unbalanced,
		# then try out the 4 cases
		# Case 1 - Left Left
		if balance > 1 and key < root.left.val:
			return self.rightRotate(root)

		# Case 2 - Right Right
		if balance < -1 and key > root.right.val:
			return self.leftRotate(root)

		# Case 3 - Left Right
		if balance > 1 and key > root.left.val:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)

		# Case 4 - Right Left
		if balance < -1 and key < root.right.val:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def leftRotate(self, z):

		y = z.right
		T2 = y.left

		# Perform rotation
		y.left = z
		z.right = T2

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def rightRotate(self, z):

		y = z.left
		T3 = y.right

		# Perform rotation
		y.right = z
		z.left = T3

		# Update heights
		z.height = 1 + max(self.getHeight(z.left),
						self.getHeight(z.right))
		y.height = 1 + max(self.getHeight(y.left),
						self.getHeight(y.right))

		# Return the new root
		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.height

	def getBalance(self, root):
		if not root:
			return 0

		return self.getHeight(root.left) - self.getHeight(root.right)


# Deleting
"""
Similar to inserting
1) Perform a standard BST deletion
2) Travel up to the first unbalanced node
3) Rebalance accordingly
"""

def delete(self, root, key):

    # Step 1 - Perform standard BST delete
    if not root:
        return root

    elif key < root.val:
        root.left = self.delete(root.left, key)

    elif key > root.val:
        root.right = self.delete(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = self.getMinValueNode(root.right)
        root.val = temp.val
        root.right = self.delete(root.right,
                                    temp.val)

    # If the tree has only one node,
    # simply return it
    if root is None:
        return root

    # Step 2 - Update the height of the
    # ancestor node
    root.height = 1 + max(self.getHeight(root.left),
                        self.getHeight(root.right))

    # Step 3 - Get the balance factor
    balance = self.getBalance(root)

    # Step 4 - If the node is unbalanced,
    # then try out the 4 cases
    # Case 1 - Left Left
    if balance > 1 and self.getBalance(root.left) >= 0:
        return self.rightRotate(root)

    # Case 2 - Right Right
    if balance < -1 and self.getBalance(root.right) <= 0:
        return self.leftRotate(root)

    # Case 3 - Left Right
    if balance > 1 and self.getBalance(root.left) < 0:
        root.left = self.leftRotate(root.left)
        return self.rightRotate(root)

    # Case 4 - Right Left
    if balance < -1 and self.getBalance(root.right) > 0:
        root.right = self.rightRotate(root.right)
        return self.leftRotate(root)

    return root




