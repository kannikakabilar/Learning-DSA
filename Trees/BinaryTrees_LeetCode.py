# Binary Trees

"""
Most Binary Search Tree problems can be resolved through:

- call recursion on root.left and root.right
(but handle the left and right trees accordingly based on the problem)

- build a helper function if needed
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        
        lst = []
        if root is None:
            return lst
        if root.left is None:
            lst.append(root.val)
            lst += self.inorderTraversal(root.right)
        else:
            lst += self.inorderTraversal(root.left)
            lst.append(root.val)
            lst += self.inorderTraversal(root.right)
            
        return lst

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Root, Left, Right
        trv = []
        if root is None:
            return trv
        else:
            trv.append(root.val)
            return trv + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Left, Right, Root
        trv = []
        if root is None:
            return trv
        else:
            trv.append(root.val)
            return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + trv


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif (p is None and not(q is None)) or (q is None and not(p is None)):
            return False
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree2(root.left,root.right)
    def isSameTree2(self,p,q):
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            # This below line is different
            return self.isSameTree2(p.right,q.left) and self.isSameTree2(p.left,q.right)
        return False


    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or (root.left is None and root.right is None):
            return root
        else:
            tmp = root.left
            root.left = root.right
            root.right = tmp
            self.invertTree(root.left)
            self.invertTree(root.right)
            return root


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root is None:
            return depth
        else:
            depth += 1
            return depth + max(self.maxDepth(root.left), self.maxDepth(root.right))

    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode'):
        while 1 == 1:
            if root.val>p.val and root.val>q.val:
                root=root.left
            elif root.val<p.val and root.val<q.val:
                root=root.right
            else:
                return root


    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        def dfs(r,path):
            if not r.left and not r.right:
                path += str(r.val)
                res.append(path)
                return
            if r.left:
                dfs(r.left, path+str(r.val)+"->")
            if r.right:
                dfs(r.right, path+str(r.val)+"->")
            return
        dfs(root,"")
        return res


    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else:
            total = 0
            tmp = root.left
            if not(tmp is None) and tmp.left is None and tmp.right is None:
                total += tmp.val
            total += self.sumOfLeftLeaves(root.right)
            total += self.sumOfLeftLeaves(root.left)
            return total


    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        if root is None:
            return []
        else:
            def helper(root, m):
                #m = dict()
                if root is None:
                    return m
                
                if root.val in m:
                    m[root.val] += 1
                else:
                    m[root.val] = 1
                helper(root.right, m)
                helper(root.left, m)
                return m
            g = helper(root, dict())
            highest = 0
            tmp = []
            for i in g:
                if g[i] > highest:
                    tmp = [i]
                    highest = g[i]
                elif g[i] == highest:
                    tmp.append(i)
            return tmp


    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        sl = []
        def inorder(root):
            if not root: return
            inorder(root.left)
            sl.append(root.val)
            inorder(root.right)
        inorder(root)
        return min(sl[i+1] - sl[i] for i in range(len(sl)-1))


    def minDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        if root is None:
        #or ((root.left is None) and (root.right is None)):
            return depth
        
        else:
            depth += 1
            if root.left is None:
                return depth + self.minDepth(root.right)
            elif root.right is None:
                return depth + self.minDepth(root.left)
            else:
                return depth + min(self.minDepth(root.left), self.minDepth(root.right))