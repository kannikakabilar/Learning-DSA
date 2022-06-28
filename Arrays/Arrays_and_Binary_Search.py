# Arrays and Binary Search

# Q1 Convert Sorted Array to Binary Search Tree
"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:
"""
# Definition for a binary tree node in Python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        # Approximately the middle element is set as the root node
        root = len(nums)//2 
        tree = TreeNode(nums[root])
        # And everything to the left of this element will be put into its left sub-tree
        tree.left = Solution.sortedArrayToBST(self, nums[:root])
        # And everything to the right of this element will be put into its right sub-tree
        tree.right = Solution.sortedArrayToBST(self, nums[root+1:])
        
        return tree

# Q2 Search Inset Position
"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example1
Input: nums = [1,3,5,6], target = 5
Output: 2

Example2
Input: nums = [1,3,5,6], target = 2
Output: 1

"""
def searchInsert(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1              # Keeps track of the starting and ending index of the array
        
    while left <= right:                        # Keep decreasing the range between the left and right index
        middle = left + (right-left) // 2       # Since array is sorted, calculating middle helps implement binary search by dividing array in 2 halves
        if nums[middle] == target:              # If target is found in the array
            return middle
        if nums[middle] > target:               # Search for target in the left half
            right = middle - 1
        else:                                   # Search for target in the right half
            left = middle + 1
    return left

"""
(Below might not be implementable)
Applications of Binary Search beyond arrays
2.1. To find if n is a square of an integer
2.2. Find the first value greater than or equal to x in a given array of sorted integers
2.3. Find the frequency of a given target value in an array of integers
2.4. Find the peak of an array which increases and then decreases
2.5. A sorted array is rotated n times. Search for a target value in the array.

Real life applications of Binary Search
3.1. Dictionary
3.2. Debugging a linear piece of code
3.3. Figuring out resource requirements for a large system
3.4. Find values in sorted collection
3.5. Semiconductor test programs
3.6. Numerical solutions to an equation
"""
