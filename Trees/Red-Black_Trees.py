# Red Black Trees

"""
Rules That Every Red-Black Tree Follows: 

1) Every node has a color either red or black.
2) The root of the tree is always black.
3) There are no two adjacent red nodes (A red node cannot have a red parent or red child).
4) Every path from a node (including root) to any of its descendants NULL nodes has the same number of black nodes.
5) All leaf nodes are black nodes.
"""
"""
Red-Black Trees are similar to AVL Trees but they perform less rotations.
If insertion and deletion is performed more often => Red-Black Trees
If Search is performed more often => AVL Trees

Every Red Black Tree with n nodes has height <= 2Log2(n+1) 

In the Red-Black tree, 2 tools are used to do the balancing. 
1) Recoloring
2) Rotation

Recoloring changes node color from red to black and vice versa. But NULL node will always be black.

"""

# Inserting
"""
Set the colour of the new-node to red and insert like a normal BST insert.
Then perform Red-Black Tree fix.

Algorithm to maintain red-black property after insertion
This algorithm is used for maintaining the property of a red-black tree if the insertion of a newNode violates this property.



Recolouring is the change in colour of the node i.e. if it is red then change it to black and vice versa. 

It must be noted that the colour of the NULL node is always black. Moreover, we always try recolouring first, 
if recolouring doesn’t work, then we go for rotation. 

The algorithms have mainly two cases depending upon the colour of the uncle. If the uncle is red, we do recolour. 
If the uncle is black, we do rotations and/or recolouring.

     gp     
    / \     
   p   u   
  / \       
 n   s  

 gp = grandparent
 p  = parent
 u  = uncle
 s  = sibling
 n  = newnode


Let x be the newly inserted node.

Perform standard BST insertion and make the colour of newly inserted nodes as RED.

If x is the root, change the colour of x as BLACK (Black height of complete tree increases by 1).

Do the following if the color of x’s parent is not BLACK and x is not the root. 

a) If x’s uncle is RED (Grandparent must have been black from property 4) 
(i) Change the colour of parent and uncle as BLACK. 
(ii) Colour of a grandparent as RED. 
(iii) Change x = x’s grandparent, repeat steps 2 and 3 for new x. 

b) If x’s uncle is BLACK, then there can be four configurations for x, x’s parent (p) and x’s grandparent (g) (This is similar to AVL Tree) 
(i) Left Left Case (p is left child of g and x is left child of p) 
(ii) Left Right Case (p is left child of g and x is the right child of p) 
(iii) Right Right Case (Mirror of case i) 
(iv) Right Left Case (Mirror of case ii)
"""

# Deleting
"""
Deletion of a node in Red Black Tree:


1) Perform standard Binary Search Tree delete. 
(When we perform standard delete operation in BST, we always end up deleting a node which is either leaf or has only one child 
Because (For an internal node, we copy the successor and then recursively call delete for successor, successor is always a leaf node or a node with one child). 
So we only need to handle cases where a node is leaf or has one child. Let v be the node to be deleted and u be the child that replaces v 
(Note that u is NULL when v is a leaf and color of NULL is considered as Black).


2) Simple Case: If either u or v is red, we mark the replaced child as black (No change in black height). 
Note that both u and v cannot be red as v is parent of u and two consecutive reds are not allowed in red-black tree.


3) If Both u and v are Black.

3.1) Color u as double black. Now our task reduces to convert this double black to single black. 
Note that If v is leaf, then u is NULL and color of NULL is considered as black. 
So the deletion of a black leaf also causes a double black.

3.2) Do following while the current node u is double black and it is not root. Let sibling of node be s.
(a): If sibling s is black and at least one of sibling’s children is red, perform rotation(s). 
Let the red child of s be r. This case can be divided in four subcases depending upon positions of s and r.

(i) Left Left Case (s is left child of its parent and r is left child of s or both children of s are red). 
This is mirror of right right case shown in below diagram.

(ii) Left Right Case (s is left child of its parent and r is right child). 
This is mirror of right left case shown in below diagram.

(iii) Right Right Case (s is right child of its parent and r is right child of s or both children of s are red)

(iv) Right Left Case (s is right child of its parent and r is left child of s)

(b): If sibling is black and its both children are black, perform recoloring, and recur for the parent if parent is black.

(c): If sibling is red, perform a rotation to move old sibling up, recolor the old sibling and parent. 
The new sibling is always black (See the below diagram). 
This mainly converts the tree to black sibling case (by rotation) and leads to case (a) or (b). 
This case can be divided in two subcases.

(i) Left Case (s is left child of its parent). This is mirror of right right case shown in below diagram. 
We right rotate the parent p.

(ii) Right Case (s is right child of its parent). We left rotate the parent p.

3.3) If u is root, make it single black and return (Black height of complete tree reduces by 1).
"""

# Implementing Red-Black Tree in Python


import sys


# Node creation
class Node():
    def __init__(self, item):
        self.item = item
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RedBlackTree():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    # Preorder
    def pre_order_helper(self, node):
        if node != TNULL:
            sys.stdout.write(node.item + " ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    # Inorder
    def in_order_helper(self, node):
        if node != TNULL:
            self.in_order_helper(node.left)
            sys.stdout.write(node.item + " ")
            self.in_order_helper(node.right)

    # Postorder
    def post_order_helper(self, node):
        if node != TNULL:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            sys.stdout.write(node.item + " ")

    # Search the tree
    def search_tree_helper(self, node, key):
        if node == TNULL or key == node.item:
            return node

        if key < node.item:
            return self.search_tree_helper(node.left, key)
        return self.search_tree_helper(node.right, key)

    # Balancing the tree after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    # Node deletion
    def delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.item == key:
                z = node

            if node.item <= key:
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            print("Cannot find key in the tree")
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    # Balance the tree after insertion
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    # Printing the tree
    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.item) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def preorder(self):
        self.pre_order_helper(self.root)

    def inorder(self):
        self.in_order_helper(self.root)

    def postorder(self):
        self.post_order_helper(self.root)

    def searchTree(self, k):
        return self.search_tree_helper(self.root, k)

    def minimum(self, node):
        while node.left != self.TNULL:
            node = node.left
        return node

    def maximum(self, node):
        while node.right != self.TNULL:
            node = node.right
        return node

    def successor(self, x):
        if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self,  x):
        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        node = Node(key)
        node.parent = None
        node.item = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.item < x.item:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.item < y.item:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root

    def delete_node(self, item):
        self.delete_node_helper(self.root, item)

    def print_tree(self):
        self.__print_helper(self.root, "", True)


if __name__ == "__main__":
    bst = RedBlackTree()

    bst.insert(55)
    bst.insert(40)
    bst.insert(65)
    bst.insert(60)
    bst.insert(75)
    bst.insert(57)

    bst.print_tree()

    print("\nAfter deleting an element")
    bst.delete_node(40)
    bst.print_tree()
