# Stacks

# Q1 Valid Parentheses
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example1
Input: s = "()[]{}"
Output: true

Example2
Input: s = "(]"
Output: false
"""
def isValid(s: str) -> bool:
    d = {'(':')', '{':'}','[':']'}
    stack = []
    for i in s:
        if i in d:  
            stack.append(i)
        elif len(stack) == 0 or d[stack.pop()] != i:  
            return False
    return len(stack) == 0 

# Q2 Binary Tree Inorder Traversal
"""
Given the root of a binary tree, 
return the inorder traversal of its nodes' values.
        1
       /  \
           2
          / \
         3 

Input: root = [1,null,2,3]
Output: [1,3,2]
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: TreeNode) -> List[int]:
        
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

# Q3 Baseball Game
"""
You are keeping score for a baseball game with strange rules. The game consists of several rounds, where the scores of past rounds may affect future rounds' scores.

At the beginning of the game, you start with an empty record. You are given a list of strings ops, where ops[i] is the ith operation you must apply to the record and is one of the following:

An integer x - Record a new score of x.
"+" - Record a new score that is the sum of the previous two scores. It is guaranteed there will always be two previous scores.
"D" - Record a new score that is double the previous score. It is guaranteed there will always be a previous score.
"C" - Invalidate the previous score, removing it from the record. It is guaranteed there will always be a previous score.
Return the sum of all the scores on the record. The test cases are generated so that the answer fits in a 32-bit integer.

Example1
Input: ops = ["5","2","C","D","+"]
Output: 30
Explanation:
"5" - Add 5 to the record, record is now [5].
"2" - Add 2 to the record, record is now [5, 2].
"C" - Invalidate and remove the previous score, record is now [5].
"D" - Add 2 * 5 = 10 to the record, record is now [5, 10].
"+" - Add 5 + 10 = 15 to the record, record is now [5, 10, 15].
The total sum is 5 + 10 + 15 = 30.
"""

def calPoints(ops: List[str]) -> int:
    stack = []
    for op in ops:
        if op == '+':
            stack.append(stack[-1] + stack[-2])
        elif op == 'C':
            stack.pop()
        elif op == 'D':
            stack.append(2 * stack[-1])
        else:
            stack.append(int(op))

    return sum(stack)

# Q4 Backspace String Compare
"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example1
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
"""

def backspaceCompare(s: str, t: str) -> bool:
    s_lst = []
    t_lst = []
    for i in s:
        if i == "#" and len(s_lst) > 0:
            s_lst.pop()
        elif i == "#" and len(s_lst) == 0:
            continue
        else:
            s_lst.append(i)
    for i in t:
        if i == "#" and len(t_lst) > 0:
            t_lst.pop()
        elif i == "#" and len(t_lst) == 0:
            continue
        else:
            t_lst.append(i)
    if len(t_lst) != len(s_lst):
        return False
    for i in range(len(s_lst)):
        if s_lst[i] != t_lst[i]:
            return False
        
    return True

# Q5 Remove Outermost Parentheses
"""
A valid parentheses string is either empty "", "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.

For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
A valid parentheses string s is primitive if it is nonempty, and there does not exist a way to split it into s = A + B, with A and B nonempty valid parentheses strings.

Given a valid parentheses string s, consider its primitive decomposition: s = P1 + P2 + ... + Pk, where Pi are primitive valid parentheses strings.

Return s after removing the outermost parentheses of every primitive string in the primitive decomposition of s.

Example1
Input: s = "(()())(())"
Output: "()()()"
Explanation: 
The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
After removing outer parentheses of each part, this is "()()" + "()" = "()()()".
"""

def removeOuterParentheses(s: str) -> str:
    res = []
    curOpen = 0
    for c in s:
        if c == '(':
            if curOpen:
                res.append(c)
            curOpen += 1
        else:
            curOpen -= 1
            if curOpen:
                res.append(c)
    
    return ''.join(res)

# Q6 Remove All Adjacent Duplicates In String
"""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example1
Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
"""
def removeDuplicates(s: str) -> str:
    lst = []
    
    for i in range(len(s)):
        if len(lst) > 0 and s[i] == lst[-1]:
            lst.pop()
        else:
            lst.append(s[i])
    return ''.join(lst)

# Q7 Build an Array With Stack Operations
"""
You are given an array target and an integer n.

In each iteration, you will read a number from list = [1, 2, 3, ..., n].

Build the target array using the following operations:

"Push": Reads a new element from the beginning list, and pushes it in the array.
"Pop": Deletes the last element of the array.
If the target array is already built, stop reading more elements.
Return a list of the operations needed to build target. The test cases are generated so that the answer is unique.

Example1
Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]

Example2
Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: You only need to read the first 2 numbers and stop.
"""
def buildArray(target: List[int], n: int) -> List[str]:
    lst = []
    for i in range(1, n+1):
        if i in target:
            lst.append("Push")
        elif i < target[-1]:
            
            lst.append("Push")
            lst.append("Pop")
            
    return lst

# Q8 Make The String Great
"""
Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2
s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Example1
Input: s = "leEeetcode"
Output: "leetcode"
Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
"""
def makeGood(s: str) -> str:
    lst = []
    for i in s:
        if len(lst) > 0 and lst[-1].swapcase() == i:
            lst.pop()
        else:
            lst.append(i)
            
    return ''.join(lst)

# Q9 Crawler Log Folder
"""
The Leetcode file system keeps a log each time some user performs a change folder operation.

The operations are described below:

"../" : Move to the parent folder of the current folder. (If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

Example1
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.
"""
def minOperations(logs: List[str]) -> int:
    level = 0
    for i in logs:
        if i == "../" and level > 0:
            level -= 1
        elif i != "../" and i != "./":
            level += 1
    return level

# Q10 Maximum Nesting Depth of the Parentheses
"""
A string is a valid parentheses string (denoted VPS) if it meets one of the following:

It is an empty string "", or a single character not equal to "(" or ")",
It can be written as AB (A concatenated with B), where A and B are VPS's, or
It can be written as (A), where A is a VPS.
We can similarly define the nesting depth depth(S) of any VPS S as follows:

depth("") = 0
depth(C) = 0, where C is a string with a single character not equal to "(" or ")".
depth(A + B) = max(depth(A), depth(B)), where A and B are VPS's.
depth("(" + A + ")") = 1 + depth(A), where A is a VPS.
For example, "", "()()", and "()(()())" are VPS's (with nesting depths 0, 1, and 2), and ")(" and "(()" are not VPS's.

Given a VPS represented as string s, return the nesting depth of s.

Example1
Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.
"""
def maxDepth(s: str) -> int:
    d = 0
    high = 0
    for i in s:
        if i == "(":
            d += 1
            if d > high:
                high = d
        if i == ")":
            d -= 1
    return high




