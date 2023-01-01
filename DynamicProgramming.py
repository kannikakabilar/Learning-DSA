# Climbing Stairs
"""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example1
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example2
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

def climbStairs(self, n: int) -> int:
    if n < 3:
        return n
    else:
        prev1 =  1
        prev2 = 2
        curr = 2
        for i in range(3, n+1):
            tmp = curr
            curr = prev1 + curr
            prev1 = tmp
            
        return curr

# Counting Bits
"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example1
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
"""

def countBits(self, n: int) -> List[int]:
    if n<=1:
        if n==0:
            return [0]
        else:
            return [0,1]
                
        dp = [0]*(n+1)

        dp[1] = 1
        
        dp[2] = 1

        for i in range(3,n+1):
            if i%2==0:
                val = i//2
                dp[i] = dp[val]
                # val its basically i<<2
            else:
                dp[i] = dp[i-1]+1
        return dp


# Is Subsequence
"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example1
Input: s = "abc", t = "ahbgdc"
Output: true
"""

def isSubsequence(self, s: str, t: str) -> bool:
    m = len(t)
    n = len(s)
    
    if n == 0:
        return True
    
    j = 0
    for i in range(m):
        if s[j] == t[i]:
            j += 1
        if j == n:
            return True
            
    return j == n

# Fibonacci Sequence

def fib(self, n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        nm1 = 1
        nm2 = 1
        
        for i in range(2, n):
            tmp = nm2
            nm2 = nm2 + nm1
            nm1 = tmp
            
        return nm2

# Min Cost Climbing Stairs

"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example1
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example2
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
"""

def minCostClimbingStairs(self, cost: List[int]) -> int:
    
    l = [-1] * len(cost)
    l[0] = cost[0]
    l[1] = cost[1]
    for i in range(2, len(cost)):
        l[i] = min(cost[i]+l[i-1], cost[i]+l[i-2])
        
    return min(l[-1], l[-2])

# N-th Tribonacci Number

"""
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.

Example1
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
"""

def tribonacci(self, n: int) -> int:
    t0 = 0
    t1 = 1
    t2 = 1
    
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        for i in range(3, n+1):
            tmp1 = t2
            tmp2 = t1
            t2 = t2 + t1 + t0
            t1 = tmp1
            t0 = tmp2
            
        return t2

# House Robber

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example1
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example2
Input: nums = [2,1,1,2]
Output: 4

"""

def rob(self, nums: List[int]) -> int:
    n=len(nums)
    
    if n==1:
        return nums[0]
    
    prev2=nums[0]
    prev1=max(nums[0],nums[1])
    
    
    for i in range(2,n):
        temp=prev1
        prev1=max(prev2+nums[i],prev1)
        prev2=temp
        
    return prev1

# House Robber II

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example1
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
"""

def rob(self, nums: List[int]) -> int:
    n=len(nums)

    if n==1:
        return nums[0]
    elif n==2:
        return max(nums)

    prev2=nums[0]
    prev1=max(nums[0],nums[1])


    for i in range(2,n-1):
        temp=prev1
        prev1=max(prev2+nums[i],prev1)
        prev2=temp
        
    pre2=nums[1]
    pre1=max(nums[1],nums[2])


    for i in range(3,n):
        temp=pre1
        pre1=max(pre2+nums[i],pre1)
        pre2=temp

    return max(prev1, pre1)


# Jump Game
"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example1
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example2
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
"""

def canJump(self, nums: List[int]) -> bool:
    s=1
    n=len(nums)
    for i in range(0,n):
        s-=1
        if(i==n-1):
            return(True)
        if(s==0 and nums[i]==0):
            return(False)
        if(s<nums[i]):
            s=nums[i]
