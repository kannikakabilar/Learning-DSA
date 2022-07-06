# B Trees

"""
B-tree is a special type of self-balancing search tree in which 
each node can contain more than one key and can have more than two children.

When given 'n' as the order of the tree
Each node except root can have at most n children and at least n/2 children.
All leaves have the same depth (i.e. height-h of the tree).
"""

# Inserting a node into a B-Tree 
"""
To insert value X into a B-tree, there are 3 steps:

1) using the SEARCH procedure for M-way trees (described above) find the leaf node to which X should be added.

2) add X to this node in the appropriate place among the values already there. Being a leaf node there are no subtrees to worry about.

3) if there are M-1 or fewer values in the node after adding X, then we are finished.
If there are M nodes after adding X, we say the node has overflowed. To repair this, we split the node into three parts:

Left:
the first (M-1)/2 values
Middle:
the middle value (position 1+((M-1)/2)
Right:
the last (M-1)/2 values

Rules
A node can have a maximum of m children. (i.e. 3)
A node can contain a maximum of m - 1 keys. (i.e. 2)
A node should have a minimum of ⌈m/2⌉ children. (i.e. 2)
A node (except root node) should contain a minimum of ⌈m/2⌉ - 1 keys. (i.e. 1)
For Examples look at the images

"""

# Deleting
"""
For deletion in b tree we wish to remove from a leaf. There are three possible case for deletion in b tree.
Let k be the key to be deleted, x the node containing the key.

Case1
If the key is in a leafnode, and removing it doesn’t cause that leaf node to have too few keys, 
then simply remove the key to be deleted.

(Look at corresponding images for the following cases)

Case2
If key k is in node x and x is an internal node, there are three cases to consider:

Case2a
If the child y that precedes k in node x has at least t keys (more than the minimum), 
then find the predecessor key k' in the subtree rooted at y. Recursively delete k' and replace k with k' in x

Case2b
Symmetrically, if the child z that follows k in node x has at least t keys, 
find the successor k' and delete and replace as before. Note that finding k' and deleting 
it can be performed in a single downward pass.

Case2c
Otherwise, if both y and z have only t−1 (minimum number) keys, 
merge k and all of z into y, so that both k and the pointer to z are removed from x. 
y now contains 2t − 1 keys, and subsequently k is deleted.

Case3
If key k is not present in an internal node x, determine the root of the appropriate subtree that must contain k. 
If the root has only t − 1 keys, execute either of the following two cases to ensure 
that we descend to a node containing at least t keys. Finally, recurse to the appropriate child of x.

Case3a
If the root has only t−1 keys but has a sibling with t keys, 
give the root an extra key by moving a key from x to the root, 
moving a key from the roots immediate left or right sibling up into x, 
and moving the appropriate child from the sibling to x.

Case3b
If the root and all of its siblings have t−1 keys, merge the root with one sibling. 
This involves moving a key down from x into the new merged node to become the median key for that node.
"""

# Searching a key on a B-tree in Python

# Create a node
class BTreeNode:
  def __init__(self, leaf=False):
    self.leaf = leaf
    self.keys = []
    self.child = []


# Tree
class BTree:
  def __init__(self, t):
    self.root = BTreeNode(True)
    self.t = t

    # Insert node
  def insert(self, k):
    root = self.root
    if len(root.keys) == (2 * self.t) - 1:
      temp = BTreeNode()
      self.root = temp
      temp.child.insert(0, root)
      self.split_child(temp, 0)
      self.insert_non_full(temp, k)
    else:
      self.insert_non_full(root, k)

    # Insert nonfull
  def insert_non_full(self, x, k):
    i = len(x.keys) - 1
    if x.leaf:
      x.keys.append((None, None))
      while i >= 0 and k[0] < x.keys[i][0]:
        x.keys[i + 1] = x.keys[i]
        i -= 1
      x.keys[i + 1] = k
    else:
      while i >= 0 and k[0] < x.keys[i][0]:
        i -= 1
      i += 1
      if len(x.child[i].keys) == (2 * self.t) - 1:
        self.split_child(x, i)
        if k[0] > x.keys[i][0]:
          i += 1
      self.insert_non_full(x.child[i], k)

    # Split the child
  def split_child(self, x, i):
    t = self.t
    y = x.child[i]
    z = BTreeNode(y.leaf)
    x.child.insert(i + 1, z)
    x.keys.insert(i, y.keys[t - 1])
    z.keys = y.keys[t: (2 * t) - 1]
    y.keys = y.keys[0: t - 1]
    if not y.leaf:
      z.child = y.child[t: 2 * t]
      y.child = y.child[0: t - 1]

  # Print the tree
  def print_tree(self, x, l=0):
    print("Level ", l, " ", len(x.keys), end=":")
    for i in x.keys:
      print(i, end=" ")
    print()
    l += 1
    if len(x.child) > 0:
      for i in x.child:
        self.print_tree(i, l)

  # Search key in the tree
  def search_key(self, k, x=None):
    if x is not None:
      i = 0
      while i < len(x.keys) and k > x.keys[i][0]:
        i += 1
      if i < len(x.keys) and k == x.keys[i][0]:
        return (x, i)
      elif x.leaf:
        return None
      else:
        return self.search_key(k, x.child[i])
      
    else:
      return self.search_key(k, self.root)

# Delete a node
    def delete(self, x, k):
        t = self.t
        i = 0
        while i < len(x.keys) and k[0] > x.keys[i][0]:
            i += 1
        if x.leaf:
            if i < len(x.keys) and x.keys[i][0] == k[0]:
                x.keys.pop(i)
                return
            return

        if i < len(x.keys) and x.keys[i][0] == k[0]:
            return self.delete_internal_node(x, k, i)
        elif len(x.child[i].keys) >= t:
            self.delete(x.child[i], k)
        else:
            if i != 0 and i + 2 < len(x.child):
                if len(x.child[i - 1].keys) >= t:
                    self.delete_sibling(x, i, i - 1)
                elif len(x.child[i + 1].keys) >= t:
                    self.delete_sibling(x, i, i + 1)
                else:
                    self.delete_merge(x, i, i + 1)
            elif i == 0:
                if len(x.child[i + 1].keys) >= t:
                    self.delete_sibling(x, i, i + 1)
                else:
                    self.delete_merge(x, i, i + 1)
            elif i + 1 == len(x.child):
                if len(x.child[i - 1].keys) >= t:
                    self.delete_sibling(x, i, i - 1)
                else:
                    self.delete_merge(x, i, i - 1)
            self.delete(x.child[i], k)

    # Delete internal node
    def delete_internal_node(self, x, k, i):
        t = self.t
        if x.leaf:
            if x.keys[i][0] == k[0]:
                x.keys.pop(i)
                return
            return

        if len(x.child[i].keys) >= t:
            x.keys[i] = self.delete_predecessor(x.child[i])
            return
        elif len(x.child[i + 1].keys) >= t:
            x.keys[i] = self.delete_successor(x.child[i + 1])
            return
        else:
            self.delete_merge(x, i, i + 1)
            self.delete_internal_node(x.child[i], k, self.t - 1)

    # Delete the predecessor
    def delete_predecessor(self, x):
        if x.leaf:
            return x.pop()
        n = len(x.keys) - 1
        if len(x.child[n].keys) >= self.t:
            self.delete_sibling(x, n + 1, n)
        else:
            self.delete_merge(x, n, n + 1)
        self.delete_predecessor(x.child[n])

    # Delete the successor
    def delete_successor(self, x):
        if x.leaf:
            return x.keys.pop(0)
        if len(x.child[1].keys) >= self.t:
            self.delete_sibling(x, 0, 1)
        else:
            self.delete_merge(x, 0, 1)
        self.delete_successor(x.child[0])

    # Delete resolution
    def delete_merge(self, x, i, j):
        cnode = x.child[i]

        if j > i:
            rsnode = x.child[j]
            cnode.keys.append(x.keys[i])
            for k in range(len(rsnode.keys)):
                cnode.keys.append(rsnode.keys[k])
                if len(rsnode.child) > 0:
                    cnode.child.append(rsnode.child[k])
            if len(rsnode.child) > 0:
                cnode.child.append(rsnode.child.pop())
            new = cnode
            x.keys.pop(i)
            x.child.pop(j)
        else:
            lsnode = x.child[j]
            lsnode.keys.append(x.keys[j])
            for i in range(len(cnode.keys)):
                lsnode.keys.append(cnode.keys[i])
                if len(lsnode.child) > 0:
                    lsnode.child.append(cnode.child[i])
            if len(lsnode.child) > 0:
                lsnode.child.append(cnode.child.pop())
            new = lsnode
            x.keys.pop(j)
            x.child.pop(i)

        if x == self.root and len(x.keys) == 0:
            self.root = new

    # Delete the sibling
    def delete_sibling(self, x, i, j):
        cnode = x.child[i]
        if i < j:
            rsnode = x.child[j]
            cnode.keys.append(x.keys[i])
            x.keys[i] = rsnode.keys[0]
            if len(rsnode.child) > 0:
                cnode.child.append(rsnode.child[0])
                rsnode.child.pop(0)
            rsnode.keys.pop(0)
        else:
            lsnode = x.child[j]
            cnode.keys.insert(0, x.keys[i - 1])
            x.keys[i - 1] = lsnode.keys.pop()
            if len(lsnode.child) > 0:
                cnode.child.insert(0, lsnode.child.pop())


def main():
  B = BTree(3)

  for i in range(10):
    B.insert((i, 2 * i))

  B.print_tree(B.root)

  if B.search_key(8) is not None:
    print("\nFound")
  else:
    print("\nNot Found")


if __name__ == '__main__':
  main()